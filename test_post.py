import urllib.request
import urllib.error
import json

data = json.dumps({"email": "test@test.com", "password": "password"}).encode('utf-8')
req = urllib.request.Request(
    'https://biosync-2.onrender.com/auth/login',
    data=data,
    headers={
        'Origin': 'http://localhost:5173',
        'Content-Type': 'application/json'
    },
    method='POST'
)

try:
    with urllib.request.urlopen(req) as response:
        print("STATUS:", response.status)
        print("HEADERS:")
        print(response.headers)
        print("BODY:")
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("HTTP ERROR:", e.code)
    print("HEADERS:")
    print(e.headers)
    print("BODY:")
    print(e.read().decode('utf-8'))
except Exception as e:
    print("ERROR:", str(e))
