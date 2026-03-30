import urllib.request
import urllib.error
import json
import random

BASE_URL = "https://biosync-2.onrender.com"

email = f"test_{random.randint(1000, 9999)}@test.com"
password = "password"

# ------------------ Register ------------------
print("Registering:", email)
data = json.dumps({
    "email": email,
    "password": password,
    "name": "Test User",
    "age": 25,
    "gender": "other"
}).encode('utf-8')

req = urllib.request.Request(
    f"{BASE_URL}/auth/register",
    data=data,
    headers={'Content-Type': 'application/json'},
    method='POST'
)

try:
    with urllib.request.urlopen(req) as res:
        print("Register status:", res.status)
except urllib.error.HTTPError as e:
    print("Register failed:", e.code, e.read().decode())


# ------------------ Login ------------------
print("Logging in:", email)
data = json.dumps({
    "email": email,
    "password": password
}).encode('utf-8')

req = urllib.request.Request(
    f"{BASE_URL}/auth/login",
    data=data,
    headers={'Content-Type': 'application/json'},
    method='POST'
)

token = None

try:
    with urllib.request.urlopen(req) as res:
        response_data = json.loads(res.read().decode())
        token = response_data.get("token")
        print("Login successful, token received")
except urllib.error.HTTPError as e:
    print("Login failed:", e.code, e.read().decode())


# ------------------ Add Meal ------------------
print("Adding meal...")
meal_data = json.dumps({
    "meal_name": "Rice and Chicken",
    "calories": 550,
    "protein": 30,
    "carbs": 60,
    "fats": 20
}).encode('utf-8')

req = urllib.request.Request(
    f"{BASE_URL}/meals/add",
    data=meal_data,
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    },
    method='POST'
)

try:
    with urllib.request.urlopen(req) as res:
        print("Meal added:", res.status)
except urllib.error.HTTPError as e:
    print("Add meal failed:", e.code, e.read().decode())


# ------------------ Get Meals ------------------
print("Fetching meals...")
req = urllib.request.Request(
    f"{BASE_URL}/meals",
    headers={
        'Authorization': f'Bearer {token}'
    },
    method='GET'
)

try:
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        print("Meals data:", data)
except urllib.error.HTTPError as e:
    print("Get meals failed:", e.code, e.read().decode())