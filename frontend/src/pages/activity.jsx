import { useEffect, useState } from "react";
import API from "../services/api";
import ActivityChart from "../components/activitychart";

function Activity() {
  const [activities, setActivities] = useState([]);
  const [futureData, setFutureData] = useState([]);

  const [form, setForm] = useState({
    steps: "",
    sleep_hours: "",
    water_intake: "",
    exercise_minutes: "",
  });

  const [editingId, setEditingId] = useState(null);

  useEffect(() => {
    fetchActivities();
    fetchPrediction();
  }, []);

  const fetchActivities = async () => {
    try {
      const res = await API.get("/activity");
      setActivities(res.data);
    } catch (error) {
      console.error("Error fetching activity:", error);
    }
  };

  const fetchPrediction = async () => {
    try {
      const res = await API.get("/activity/predict-future");
      setFutureData(res.data.future_7_days || []);
    } catch (error) {
      console.error("Prediction error:", error);
    }
  };

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      if (editingId) {
        await API.put(`/activity/${editingId}`, form);
        setEditingId(null);
      } else {
        await API.post("/activity", form);
      }

      setForm({
        steps: "",
        sleep_hours: "",
        water_intake: "",
        exercise_minutes: "",
      });

      fetchActivities();
    } catch (error) {
      console.error("Submit error:", error);
    }
  };

  const handleEdit = (activity) => {
    setEditingId(activity._id);

    setForm({
      steps: activity.steps || "",
      sleep_hours: activity.sleep_hours || "",
      water_intake: activity.water_intake || "",
      exercise_minutes: activity.exercise_minutes || "",
    });
  };

  const handleDelete = async (id) => {
    try {
      await API.delete(`/activity/${id}`);
      fetchActivities();
    } catch (error) {
      console.error("Delete error:", error);
    }
  };

  const mergedData = [
    ...activities,
    ...futureData.map((item, index) => ({
      date: `Future ${index + 1}`,
      steps: item[0],
      sleep_hours: item[1],
      exercise_minutes: item[2],
    })),
  ];

  return (
    <div className="flex-1 px-4 sm:px-6 lg:px-10 py-6 max-w-7xl mx-auto">
      {/* Title */}
      <h2 className="text-2xl font-bold mb-6 text-gray-800">
        Activity Tracker
      </h2>

      {/* Activity Form */}
      <form
        onSubmit={handleSubmit}
        className="bg-white shadow rounded-xl p-6 mb-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4"
      >
        <input
          type="number"
          name="steps"
          placeholder="Steps"
          value={form.steps}
          onChange={handleChange}
          className="border p-2 rounded"
        />

        <input
          type="number"
          name="sleep_hours"
          placeholder="Sleep Hours"
          value={form.sleep_hours}
          onChange={handleChange}
          className="border p-2 rounded"
        />

        <input
          type="number"
          name="water_intake"
          placeholder="Water Intake (L)"
          value={form.water_intake}
          onChange={handleChange}
          className="border p-2 rounded"
        />

        <input
          type="number"
          name="exercise_minutes"
          placeholder="Exercise Minutes"
          value={form.exercise_minutes}
          onChange={handleChange}
          className="border p-2 rounded"
        />

        <button
          type="submit"
          className="col-span-1 md:col-span-2 lg:col-span-4 bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
        >
          {editingId ? "Update Activity" : "Add Activity"}
        </button>
      </form>

      {/* Activity Table */}
      <div className="bg-white shadow rounded-xl p-6 mb-10 overflow-x-auto">
        <h3 className="text-lg font-semibold mb-4">Your Activities</h3>

        <table className="w-full text-sm">
          <thead>
            <tr className="text-left border-b">
              <th>Date</th>
              <th>Steps</th>
              <th>Sleep</th>
              <th>Water</th>
              <th>Exercise</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>
            {activities.map((activity) => (
              <tr key={activity._id} className="border-b">
                <td>{new Date(activity.date).toLocaleDateString()}</td>
                <td>{activity.steps}</td>
                <td>{activity.sleep_hours}</td>
                <td>{activity.water_intake}</td>
                <td>{activity.exercise_minutes}</td>

                <td className="flex gap-2">
                  <button
                    onClick={() => handleEdit(activity)}
                    className="bg-yellow-500 text-white px-3 py-1 rounded"
                  >
                    Edit
                  </button>

                  <button
                    onClick={() => handleDelete(activity._id)}
                    className="bg-red-500 text-white px-3 py-1 rounded"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Charts */}
      <h2 className="text-xl font-bold mb-6 text-gray-800">Activity Trends</h2>

      <div className="grid gap-6 grid-cols-1 md:grid-cols-2 xl:grid-cols-3">
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
