import { Link } from "react-router-dom";

function Sidebar() {
  return (
    <div className="w-56 sm:w-60 lg:w-64 min-h-screen bg-gray-100 p-4 sm:p-6 border-r">
      <ul className="space-y-3 sm:space-y-4">
        <Link to="/dashboard">
          <li className="font-medium cursor-pointer px-3 py-2 rounded-md hover:bg-blue-50 hover:text-blue-600 transition">
            Dashboard
          </li>
        </Link>

        <Link to="/activity">
          <li className="font-medium cursor-pointer px-3 py-2 rounded-md hover:bg-blue-50 hover:text-blue-600 transition">
            Activity
          </li>
        </Link>

        <Link to="/meals">
          <li className="font-medium cursor-pointer px-3 py-2 rounded-md hover:bg-blue-50 hover:text-blue-600 transition">
            Meals
          </li>
        </Link>

        <Link to="/health">
          <li className="font-medium cursor-pointer px-3 py-2 rounded-md hover:bg-blue-50 hover:text-blue-600 transition">
            Health
          </li>
        </Link>
      </ul>
    </div>
  );
}

export default Sidebar;
