import urllib.request
import urllib.error
import json
import random

email = f"test_{random.randint(1000, 9999)}@test.com"

# Register
print("Registering:", email)
data = json.dumps({"email": email, "password": "password", "name": "Test User", "age": 25, "gender": "other"}).encode('utf-8')
req = urllib.request.Request(
    'https://biosync-2.onrender.com/auth/register',
    data=data,
    headers={'Origin': 'http://localhost:5173', 'Content-Type': 'application/json'},
    method='POST'
)
try:
    with urllib.request.urlopen(req) as res:
        print("Register status:", res.status)
except urllib.error.HTTPError as e:
    print("Register failed:", e.code, e.read().decode())

# Login
print("Logging in:", email)
data = json.dumps({"email": email, "password": "password"}).encode('utf-8')
req = urllib.request.Request(
    'https://biosync-2.onrender.com/auth/login',
    data=data,
    headers={'Origin': 'http://localhost:5173', 'Content-Type': 'application/json'},
    method='POST'
)
try:
    with urllib.request.urlopen(req) as res:
        print("Login status:", res.status)
        print("Login CORS origin:", res.headers.get('Access-Control-Allow-Origin'))
except urllib.error.HTTPError as e:
    print("Login failed:", e.code, e.headers.get('Access-Control-Allow-Origin'))
    print(e.read().decode())
