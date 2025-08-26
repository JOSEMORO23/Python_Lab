export default function Result({ result }) {
  if (!result) return null;

  return (
    <div style={{
      border: '2px solid #4CAF50',
      backgroundColor: '#f9fff9',
      padding: '1rem',
      borderRadius: '0.5rem',
      marginTop: '1rem',
      maxWidth: '600px'
    }}>
      <h2>Prediction Result</h2>
      <p>
        <strong>Prediction:</strong>{' '}
        <span style={{
          color: result.prediction === 'Fake' ? 'red' : 'green',
          fontWeight: 'bold'
        }}>
          {result.prediction}
        </span>
      </p>
      <p>
        <strong>Confidence:</strong> {result.confidence}%
      </p>
    </div>
  );
}
