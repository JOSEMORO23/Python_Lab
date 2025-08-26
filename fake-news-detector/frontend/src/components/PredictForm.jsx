import { useState } from 'react';

export default function PredictForm({ token, setResult }) {
  const [title, setTitle] = useState('');
  const [text, setText] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ title, text }),
      });

      if (!response.ok) {
        const errData = await response.json();
        setError(errData.detail || 'Error predicting');
        return;
      }

      const data = await response.json();
      setResult(data);
      setTitle('');
      setText('');
    } catch (err) {
      setError('Error connecting to server');
    }
  };

  return (
    <div style={{ border: '1px solid #ccc', padding: '1rem', borderRadius: '0.5rem', maxWidth: '600px' }}>
      <h2>Check News Authenticity</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title:</label><br/>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Text:</label><br/>
          <textarea
            rows="5"
            value={text}
            onChange={(e) => setText(e.target.value)}
            required
          />
        </div>
        <button type="submit">Predict</button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}
