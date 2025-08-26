import { useState } from 'react';
import Login from './components/Login';
import PredictForm from './components/PredictForm';
import Result from './components/Result';

export default function App() {
  const [token, setToken] = useState(localStorage.getItem('token') || '');
  const [result, setResult] = useState(null);

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>Fake News Detector 📰</h1>

      {!token ? (
        <Login setToken={setToken} />
      ) : (
        <>
          <PredictForm token={token} setResult={setResult} />
          {result && <Result result={result} />}
          <button onClick={() => { localStorage.removeItem('token'); setToken(''); }}>
            Logout
          </button>
        </>
      )}
    </div>
  );
}
