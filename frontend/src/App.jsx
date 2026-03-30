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

                {/* Render Free Tier Notice */}
                <div className="bg-yellow-50 border border-yellow-200 text-yellow-800 text-xs sm:text-sm px-4 py-2 text-center rounded-md mx-3 mt-2">
                  ⏳ This app is deployed on Render's free tier. The server may
                  take 4-5 minutes to wake up after inactivity, so loading data
                  after login might take a moment.
                </div>

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
