import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";

import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";
import HealthCard from "../components/healthcard";
import ActivityChart from "../components/activitychart";

function Dashboard() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const fetchDashboard = async () => {
    try {
      const response = await API.get("/dashboard/summary");

      console.log("Dashboard data:", response.data);

      // backend now returns { message, data }
      setData(response.data.data);
    } catch (err) {
      console.error("Dashboard fetch error:", err);
      // 401 is handled by the api.js interceptor (redirects to login)
      // For other errors, show an error message
      if (err.response?.status !== 401) {
        setError(err.response?.data?.detail || "Failed to load dashboard. Please try again.");
      }
    }
  };

  useEffect(() => {
    fetchDashboard();
  }, []);

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center h-screen gap-4">
        <p className="text-lg font-semibold text-red-600">⚠ {error}</p>
        <button
          onClick={() => navigate("/")}
          className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition"
        >
          Go to Login
        </button>
      </div>
    );
  }

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
              value={data.health_score || "N/A"}
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
              data={data.activity_trends?.weekly_steps_trend || []}
              dataKey="steps"
            />

            <ActivityChart
              title="Sleep Trend"
              data={data.activity_trends?.weekly_sleep_trend || []}
              dataKey="sleep_hours"
            />

            <ActivityChart
              title="Exercise Trend"
              data={data.activity_trends?.weekly_exercise_trend || []}
              dataKey="exercise_minutes"
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
