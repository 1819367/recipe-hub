import { useEffect, useState } from "react";
import Header from "./components/Header";
import RecipeExcerpt from "./components/RecipeExcerpts";
import "./App.css";

function App() {
  // State for the hello message
  const [message, setMessage] = useState("Loading...");
  // State for recipes
  const [recipes, setRecipes] = useState([]);

  // Fetch hello message
  useEffect(() => {
    const fetchMessage = async () => {
      try {
        const base = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:5000";
        console.log("🔄 Fetching HELLO from:", base + "/api/hello");
        const res = await fetch(`${base}/api/hello`);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        setMessage(data.message);
      } catch (err) {
        console.error("❌ Fetch error (hello):", err);
        setMessage("Error: " + err.message);
      }
    };
    fetchMessage();
  }, []);

  // Fetch recipes
  useEffect(() => {
    const fetchRecipes = async () => {
      try {
        const base = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:5000";
        console.log("🔄 Fetching RECIPES from:", base + "/api/recipes");
        const res = await fetch(`${base}/api/recipes`);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        console.log("✅ Recipes received:", data);
        setRecipes(data);
      } catch (err) {
        console.error("❌ Fetch error (recipes):", err);
      }
    };
    fetchRecipes();
  }, []);

  return (
    <div className="recipe-app">
      <Header />

      <div className="recipe-list">
        {recipes.map(recipe => (
          <RecipeExcerpt
            key={recipe.id}
            recipe={recipe}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
