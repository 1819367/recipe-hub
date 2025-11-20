import { useEffect } from 'react';

function App() {
  useEffect(() => {
    fetch('/api/test')
      .then(r => r.json())
      .then(data => console.log('API test:', data));
  }, []);

  return (
    <div className="App">
      <h1>Recipe Hub</h1>
      {/* rest of your app */}
    </div>
  );
}

export default App
