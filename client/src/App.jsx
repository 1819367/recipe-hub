import { useEffect, useState } from 'react'  // ← ADD useState
//import Header from './Header'                 // ← ADD if you have Header component
import './App.css'

function App() {
  const [message, setMessage] = useState("Loading...");  // ← ADD THIS STATE

useEffect(() => {
  const fetchMessage = async () => {
    try {
      console.log("🔄 Fetching from:", import.meta.env.VITE_API_BASE_URL + "/api/hello");
      const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/api/hello`);
      console.log("📡 Response status:", res.status, res.statusText);
      console.log("📡 Response ok?", res.ok);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      console.log("✅ Data received:", data);
      setMessage(data.message);
    } catch (err) {
      console.error("❌ Fetch error:", err);
      setMessage("Error: " + err.message);
    }
  };
  fetchMessage();
}, []);

  return (
    <div className='recipe-app'>
      {/* <Header /> */}
      <p>Your recipes here!</p>
      <p>API Message: {message}</p>  {/* ← DISPLAY THE RESULT */}
    </div>
  );
}

export default App;
