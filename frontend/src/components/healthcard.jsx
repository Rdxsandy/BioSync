function HealthCard({ title, value }) {
  return (
    <div className="bg-white p-4 rounded-lg shadow-md w-56">
      <h3 className="text-gray-500 text-sm">{title}</h3>

      <p className="text-2xl font-bold mt-2 text-black">{value ?? 0}</p>
    </div>
  );
}

export default HealthCard;
