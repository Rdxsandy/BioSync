import { useEffect, useState } from "react";
import API from "../services/api";

const BASE_URL = import.meta.env.VITE_API_URL;

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

      await API.post("/meals/analyze", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      alert("Meal analyzed successfully!");
      fetchMeals();
      setFile(null);
    } catch (err) {
      console.error("Upload error", err);
      alert("AI analysis failed");
    }

    setLoading(false);
  };

  return (
    <div className="flex-1 px-4 sm:px-6 lg:px-10 py-6 max-w-7xl mx-auto">
      {/* Page Title */}
      <h2 className="text-xl sm:text-2xl lg:text-3xl font-bold mb-6 text-gray-800">
        Meal Analysis
      </h2>

      {/* Upload Section */}
      <div className="bg-white p-4 sm:p-6 rounded-xl shadow-md mb-8 flex flex-col sm:flex-row sm:items-center gap-4">
        <input
          type="file"
          className="border border-gray-300 p-2 rounded-md w-full sm:w-auto"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <button
          onClick={handleUpload}
          className="w-full sm:w-auto bg-blue-500 hover:bg-blue-600 transition text-white px-6 py-2 rounded-md"
        >
          {loading ? "Analyzing..." : "Upload Meal"}
        </button>
      </div>

      {/* Meals Grid */}
      <div className="grid gap-5 sm:gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {meals.map((meal) => (
          <div
            key={meal._id}
            className="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-lg transition"
          >
            <img
              src={`${BASE_URL}/${meal.image_url}`}
              alt="meal"
              className="w-full h-44 sm:h-48 object-cover"
            />

            <div className="p-4 space-y-2">
              <h3 className="text-base sm:text-lg font-semibold text-gray-800">
                {meal.food_name}
              </h3>

              <p className="text-sm text-gray-600">
                Calories: <span className="font-medium">{meal.calories}</span>
              </p>

              <p className="text-sm text-gray-500">
                Best Time: {meal.best_time}
              </p>

              <p className="text-sm text-gray-700 pt-2 leading-relaxed">
                {meal.advice}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Meals;
