import { Link } from "react-router-dom";

function Sidebar() {
  return (
    <div className="w-56 h-screen bg-gray-100 p-6 border-r">
      <ul className="space-y-4">
        <Link to="/dashboard">
          <li className="font-medium cursor-pointer hover:text-blue-500">
            Dashboard
          </li>
        </Link>

        <Link to="/activity">
          <li className="font-medium cursor-pointer hover:text-blue-500">
            Activity
          </li>
        </Link>

        <Link to="/meals">
          <li className="font-medium cursor-pointer hover:text-blue-500">
            Meals
          </li>
        </Link>

        <Link to="/health">
          <li className="font-medium cursor-pointer hover:text-blue-500">
            Health
          </li>
        </Link>
      </ul>
    </div>
  );
}

export default Sidebar;
