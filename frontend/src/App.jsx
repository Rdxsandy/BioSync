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
      {/* Responsive App Container */}
      <div className="min-h-screen mx-auto min-w-[230px] max-w-[570px] sm:max-w-[720px] lg:max-w-[1200px]">
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

          <Route path="/dashboard" element={<Dashboard />} />

          <Route path="/register" element={<Register />} />

          <Route path="/activity" element={<Activity />} />

          <Route path="/meals" element={<Meals />} />

          <Route path="/health" element={<Health />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
