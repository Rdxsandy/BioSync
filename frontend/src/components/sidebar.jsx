function Sidebar() {
  return (
    <div className="w-56 h-screen bg-gray-100 p-6 border-r">
      <ul className="space-y-4">
        <li className="font-medium cursor-pointer hover:text-blue-500">
          Dashboard
        </li>

        <li className="font-medium cursor-pointer hover:text-blue-500">
          Activity
        </li>

        <li className="font-medium cursor-pointer hover:text-blue-500">
          Meals
        </li>

        <li className="font-medium cursor-pointer hover:text-blue-500">
          Health
        </li>
      </ul>
    </div>
  );
}

export default Sidebar;
