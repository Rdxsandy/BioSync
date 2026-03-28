import { useEffect, useState } from "react";
import API from "../services/api";

import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";
import HealthCard from "../components/healthcard";
import ActivityChart from "../components/activitychart";

function Dashboard() {
  const [data, setData] = useState(null);

  const fetchDashboard = async () => {
    try {
      const response = await API.get("/dashboard/summary");
      console.log("Dashboard data:", response.data);
      setData(response.data);
    } catch (error) {
      console.error("Dashboard fetch error:", error);
    }
  };

  useEffect(() => {
    fetchDashboard();
  }, []);

  if (!data) {
    return (
      <div className="flex items-center justify-center h-screen">
        <p className="text-lg font-medium">Loading dashboard...</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex flex-col">
      {/* Navbar */}
      <Navbar />

      <div className="flex flex-1">
        {/* Sidebar */}
        <Sidebar />

        {/* Main Dashboard */}
        <div className="flex-1 bg-gray-100 px-4 sm:px-6 lg:px-10 py-6 max-w-7xl w-full mx-auto">
          <h2 className="text-xl sm:text-2xl lg:text-3xl font-bold mb-6 text-gray-800">
            Dashboard
          </h2>

          {/* Health Cards */}
          <div className="grid gap-4 sm:gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
            <HealthCard
              title="Steps Today"
              value={data.activity_today?.steps || 0}
            />

            <HealthCard
              title="Sleep Hours"
              value={data.activity_today?.sleep_hours || 0}
            />

            <HealthCard
              title="Exercise Minutes"
              value={data.activity_today?.exercise_minutes || 0}
            />

            <HealthCard
              title="Calories Today"
              value={data.calories_today || 0}
            />

            <HealthCard
              title="Health Score"
              value={data.weekly_health_trend?.[0]?.score || "N/A"}
            />

            <HealthCard
              title="Risk Prediction"
              value={data.risk_level || "Unknown"}
            />
          </div>

          {/* Activity Charts */}
          <div className="grid gap-6 mt-8 grid-cols-1 md:grid-cols-2 xl:grid-cols-3">
            <ActivityChart
              title="Steps Trend"
              data={data.activity_trends.weekly_steps_trend}
              dataKey="steps"
            />

            <ActivityChart
              title="Sleep Trend"
              data={data.activity_trends.weekly_sleep_trend}
              dataKey="sleep_hours"
            />

            <ActivityChart
              title="Exercise Trend"
              data={data.activity_trends.weekly_exercise_trend}
              dataKey="exercise_minutes"
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
