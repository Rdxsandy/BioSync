import os
import sys
import numpy as np

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ml.service import safe_float

def test_safe_float():
    print("Testing safe_float conversion...")
    assert safe_float("12.5") == 12.5
    assert safe_float("Estimated by AI", 2000) == 2000
    assert safe_float(None, 0) == 0
    print("✅ safe_float: Passed.")

def run_ml_logic_tests():
    print("🧠 Starting ML Logic Tests...\n")
    
    # 1. Test Utility Functions
    test_safe_float()

    # 2. Test mock risk calculation logic
    # (Since actual model requires DB, we test the pre-processing logic)
    mock_activities = [
        {"sleep_hours": 8, "exercise_minutes": 30, "steps": 5000},
        {"sleep_hours": 7, "exercise_minutes": 45, "steps": 6000},
        {"sleep_hours": "Estimated", "exercise_minutes": 0, "steps": 1000}
    ]
    
    sleep_vals = [safe_float(a.get("sleep_hours", 0)) for a in mock_activities]
    avg_sleep = np.mean(sleep_vals)
    
    print(f"\nProcessing mock activities: {len(mock_activities)} records.")
    print(f"Calculated average sleep: {avg_sleep:.2f} hours.")
    
    if avg_sleep > 6:
        print("✅ Data processing: Sleep average is within healthy range.")
    else:
        print("⚠️ Data processing: Sleep average is low.")

    print("\n✅ ML Logic Tests Completed.")

if __name__ == "__main__":
    run_ml_logic_tests()
