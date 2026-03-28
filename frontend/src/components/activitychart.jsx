import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

function ActivityChart({ data, dataKey, title }) {
  return (
    <div className="bg-white w-full p-4 sm:p-5 lg:p-6 rounded-xl shadow-md">
      <h3 className="text-base sm:text-lg lg:text-xl font-semibold mb-3 sm:mb-4 text-gray-800">
        {title}
      </h3>

      <div className="w-full h-[220px] sm:h-[250px] lg:h-[280px]">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="date" />

            <YAxis />

            <Tooltip />

            <Line
              type="monotone"
              dataKey={dataKey}
              stroke="#2563eb"
              strokeWidth={3}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default ActivityChart;
