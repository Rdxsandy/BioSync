import os
from database.db import db
from auth.service import register_user, login_user
from activity.service import create_activity, predict_future_activity
from ml.service import predict_risk_from_db
from schema.user_schema import UserCreate

def run_system_tests():
    print("🚀 Starting BioSync System Tests...\n")

    # 1. Database Connection Check
    try:
        db.command("ping")
        print("✅ Database: Connected successfully.")
    except Exception as e:
        print(f"❌ Database: Connection failed! {e}")
        return

    # 2. Authentication Test
    test_user = UserCreate(
        name="Test Engineer",
        email="evaluator@hbtu.ac.in",
        password="secure_password123",
        age=22,
        gender="male",
        height=175,
        weight=70
    )
    
    print("\n--- Testing Authentication ---")
    reg_res = register_user(test_user)
    print(f"Registration: {reg_res}")
    
    log_res = login_user(test_user.email, test_user.password)
    print(f"Login: {log_res}")
    
    if "error" in log_res:
        print("⚠️ Authentication failed. Skipping further tests.")
        return

    # 3. Activity Logging Test
    print("\n--- Testing Activity Logging ---")
    user = db["users"].find_one({"email": test_user.email})
    user_id = str(user["_id"])
    
    mock_activity = {
        "user_id": user_id,
        "steps": 8500,
        "sleep_hours": 7.5,
        "exercise_minutes": 45
    }
    log_res = create_activity(mock_activity)
    print(f"Logged Activity: {log_res}")

    # 4. ML Risk Prediction Test
    print("\n--- Testing ML Risk Assessment ---")
    risk_level = predict_risk_from_db(user_id)
    print(f"Calculated Health Risk: {risk_level}")

    # 5. Time-Series Prediction Test
    print("\n--- Testing Time-Series Prediction (LSTM) ---")
    prediction = predict_future_activity(user_id)
    if "error" in prediction:
        print(f"LSTM Prediction: {prediction['error']} (Expected for new user)")
    else:
        print(f"LSTM Prediction: Successfully generated 7-day forecast.")

    print("\n✅ System Tests Completed.")

if __name__ == "__main__":
    run_system_tests()
