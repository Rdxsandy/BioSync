import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/login";
import Dashboard from "./pages/dashboard";
import Register from "./pages/register";
import BrandHeader from "./components/BrandHeader";
import Activity from "./pages/activity";
import Meals from "./pages/meals";
import Health from "./pages/health";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <>
              <BrandHeader />
              <Login />
            </>
          }
        />
        <Route path="/meals" element={<Meals />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/register" element={<Register />} />
        <Route path="/activity" element={<Activity />} />
        <Route path="/health" element={<Health />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
