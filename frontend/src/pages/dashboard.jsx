import { useEffect, useState } from "react";
import API from "../services/api";

import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";
import HealthCard from "../components/healthcard";

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
    <div>
      {/* Navbar */}
      <Navbar />

      <div className="flex">
        {/* Sidebar */}
        <Sidebar />

        {/* Main Dashboard */}
        <div className="p-6 flex-1 bg-gray-100 min-h-screen">
          <h2 className="text-2xl font-bold mb-6">Dashboard</h2>

          {/* Health Cards */}
          <div className="grid grid-cols-3 gap-6">
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
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
