function HealthCard({ title, value }) {
  return (
    <div className="bg-white w-full p-4 sm:p-5 rounded-xl shadow-md hover:shadow-lg transition">
      <h3 className="text-gray-500 text-xs sm:text-sm font-medium">{title}</h3>

      <p className="text-xl sm:text-2xl lg:text-3xl font-bold mt-2 text-black">
        {value ?? 0}
      </p>
    </div>
  );
}

export default HealthCard;
