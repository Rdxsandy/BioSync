import { useEffect, useState } from "react";
import API from "../services/api";

function Health() {
  const [tips, setTips] = useState([]);

  useEffect(() => {
    fetchHealthFact();
  }, []);

  const fetchHealthFact = async () => {
    try {
      const res = await API.get("/health/daily-fact");

      const text = res.data.health_fact;

      const formattedTips = text
        .split(/\d+\.\s/)
        .filter((tip) => tip.trim() !== "");

      setTips(formattedTips);
    } catch (err) {
      console.error("Error fetching health fact", err);
    }
  };

  return (
    <div className="flex-1 px-4 sm:px-6 lg:px-10 py-6 max-w-6xl mx-auto">
      {/* Page Title */}
      <h1 className="text-xl sm:text-2xl lg:text-3xl font-bold text-gray-800">
        Daily Health Tips
      </h1>

      {/* Tips Grid */}
      <div className="mt-6 grid gap-4 sm:gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
        {tips.map((tip, index) => (
          <div
            key={index}
            className="bg-white p-4 sm:p-5 rounded-xl shadow-md border hover:shadow-lg transition"
          >
            <p className="text-gray-700 text-sm sm:text-base leading-relaxed">
              {tip}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Health;
