import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";

function Register() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    age: "",
    gender: "",
    height: "",
    weight: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleRegister = async (e) => {
    e.preventDefault();

    try {
      await API.post("/auth/register", {
        name: formData.name,
        email: formData.email,
        password: formData.password,
        age: Number(formData.age),
        gender: formData.gender,
        height: Number(formData.height),
        weight: Number(formData.weight),
      });

      alert("Registration successful. Please login.");

      navigate("/");
    } catch (error) {
      console.error(error);
      alert("Registration failed");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 px-4">
      <div className="w-full max-w-md bg-white p-6 sm:p-8 rounded-xl shadow-md">
        <h2 className="text-xl sm:text-2xl font-bold text-center mb-4 text-gray-800">
          Register
        </h2>

        <p className="text-sm text-center mb-6 text-gray-600">
          Already have an account?{" "}
          <a href="/" className="text-blue-500 hover:underline">
            Login
          </a>
        </p>

        <form onSubmit={handleRegister} className="space-y-4">
          <input
            name="name"
            placeholder="Name"
            onChange={handleChange}
            className="w-full border border-gray-300 p-2.5 rounded-md focus:outline-none focus:ring-2 focus:ring-green-400"
          />

          <input
            name="email"
            placeholder="Email"
            onChange={handleChange}
            className="w-full border border-gray-300 p-2.5 rounded-md focus:outline-none focus:ring-2 focus:ring-green-400"
          />

          <input
            name="password"
            type="password"
            placeholder="Password"
            onChange={handleChange}
            className="w-full border border-gray-300 p-2.5 rounded-md focus:outline-none focus:ring-2 focus:ring-green-400"
          />

          <input
            name="age"
            placeholder="Age"
            onChange={handleChange}
            className="w-full border border-gray-300 p-2.5 rounded-md focus:outline-none focus:ring-2 focus:ring-green-400"
          />

          <input
            name="gender"
            placeholder="Gender"
            onChange={handleChange}
            className="w-full border border-gray-300 p-2.5 rounded-md focus:outline-none focus:ring-2 focus:ring-green-400"
          />

          <input
            name="height"
            placeholder="Height (cm)"
            onChange={handleChange}
            className="w-full border border-gray-300 p-2.5 rounded-md focus:outline-none focus:ring-2 focus:ring-green-400"
          />

          <input
            name="weight"
            placeholder="Weight (kg)"
            onChange={handleChange}
            className="w-full border border-gray-300 p-2.5 rounded-md focus:outline-none focus:ring-2 focus:ring-green-400"
          />

          <button
            type="submit"
            className="w-full bg-green-500 text-white p-2.5 rounded-md hover:bg-green-600 transition"
          >
            Register
          </button>
        </form>
      </div>
    </div>
  );
}

export default Register;
