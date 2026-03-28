import { useEffect, useState } from "react";
import API from "../services/api";
import ActivityChart from "../components/activitychart";

function Activity() {
  const [pastData, setPastData] = useState([]);
  const [futureData, setFutureData] = useState([]);

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
      setFutureData(res.data.future_7_days);
    } catch (error) {
      console.error("Prediction error:", error);
    }
  };

  const mergedData = [
    ...pastData,
    ...futureData.map((item, index) => ({
      date: `Future ${index + 1}`,
      steps: item[0],
      sleep_hours: item[1],
      exercise_minutes: item[2],
    })),
  ];

  return (
    <div className="p-6 flex-1">
      <h2 className="text-2xl font-bold mb-6">Activity Trends</h2>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <ActivityChart
          data={mergedData}
          dataKey="steps"
          title="Steps (AI Prediction)"
        />

        <ActivityChart
          data={mergedData}
          dataKey="sleep_hours"
          title="Sleep Hours (AI Prediction)"
        />

        <ActivityChart
          data={mergedData}
          dataKey="exercise_minutes"
          title="Exercise Minutes (AI Prediction)"
        />
      </div>
    </div>
  );
}

export default Activity;
