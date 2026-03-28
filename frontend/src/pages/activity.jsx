import { useEffect, useState } from "react";
import API from "../services/api";
import ActivityChart from "../components/activitychart";

function Activity() {
  const [pastData, setPastData] = useState([]);
  const [futureSteps, setFutureSteps] = useState([]);

  useEffect(() => {
    fetchActivity();
    fetchPrediction();
  }, []);

  const fetchActivity = async () => {
    try {
      const res = await API.get("/activity");

      setPastData(res.data);
    } catch (error) {
      console.error("Error fetching activity:", error);
    }
  };

  const fetchPrediction = async () => {
    try {
      const res = await API.get("/activity/predict-future");

      setFutureSteps(res.data.future_7_days);
    } catch (error) {
      console.error("Prediction error:", error);
    }
  };

  // Merge past + future data
  const mergedData = [
    ...pastData,
    ...futureSteps.map((steps, index) => ({
      date: `Future ${index + 1}`,
      steps: steps,
    })),
  ];

  return (
    <div className="p-6 flex-1">
      <h2 className="text-2xl font-bold mb-6">Activity Trends</h2>

      <ActivityChart
        data={mergedData}
        dataKey="steps"
        title="Steps (Past + AI Prediction)"
      />
    </div>
  );
}

export default Activity;
