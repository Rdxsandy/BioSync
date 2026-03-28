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

      // Split numbered tips
      const formattedTips = text
        .split(/\d+\.\s/) // split by "1. 2. 3."
        .filter((tip) => tip.trim() !== "");

      setTips(formattedTips);
    } catch (err) {
      console.error("Error fetching health fact", err);
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Daily Health Tips</h1>

      <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
        {tips.map((tip, index) => (
          <div key={index} className="bg-white p-4 rounded shadow border">
            <p className="text-gray-700">{tip}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Health;
