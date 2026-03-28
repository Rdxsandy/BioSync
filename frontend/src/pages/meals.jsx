import { useEffect, useState } from "react";
import API from "../services/api";

function Meals() {
  const [meals, setMeals] = useState([]);
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchMeals();
  }, []);

  const fetchMeals = async () => {
    try {
      const res = await API.get("/meals");
      setMeals(res.data);
    } catch (err) {
      console.error("Error fetching meals", err);
    }
  };

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const res = await API.post("/meals/analyze", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      alert("Meal analyzed successfully!");

      fetchMeals();
    } catch (err) {
      console.error("Upload error", err);
      alert("AI analysis failed");
    }

    setLoading(false);
  };

  return (
    <div className="p-6 flex-1">
      <h2 className="text-2xl font-bold mb-6">Meals</h2>

      {/* Upload Section */}
      <div className="bg-white p-4 rounded shadow mb-6">
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />

        <button
          onClick={handleUpload}
          className="ml-4 bg-blue-500 text-white px-4 py-2 rounded"
        >
          {loading ? "Analyzing..." : "Upload Meal"}
        </button>
      </div>

      {/* Meals List */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {meals.map((meal) => (
          <div key={meal._id} className="bg-white p-4 rounded shadow">
            <img
              src={`http://localhost:8000/${meal.image_url}`}
              alt="meal"
              className="w-full h-40 object-cover rounded mb-2"
            />

            <h3 className="font-bold">{meal.food_name}</h3>

            <p>Calories: {meal.calories}</p>

            <p className="text-sm text-gray-600">Best Time: {meal.best_time}</p>

            <p className="text-sm mt-2">{meal.advice}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Meals;
