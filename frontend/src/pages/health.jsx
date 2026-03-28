
import { useEffect, useState } from "react";
import axios from "axios";

function Health() {

  const [fact, setFact] = useState("");

  useEffect(() => {

    const token = localStorage.getItem("token");   // get stored JWT

    axios.get("http://localhost:8000/health/daily-fact", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    .then((res) => {
      setFact(res.data.health_fact);
    })
    .catch((err) => {
      console.log(err);
    });

  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Daily Health Fact</h1>

      <div
        style={{
          marginTop: "20px",
          padding: "20px",
          background: "#f4f4f4",
          borderRadius: "10px",
          maxWidth: "500px"
        }}
      >
        {fact ? fact : "Loading today's health tip..."}
      </div>
    </div>
  );
}

export default Health;
