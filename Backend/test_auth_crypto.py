import os
import sys

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from auth.utils import hash_password, verify_password, create_access_token

def test_auth_crypto():
    print("🔐 Starting Authentication Cryptography Tests...\n")

    # 1. Test Password Hashing & Verification
    test_password = "secure_password_123"
    hashed = hash_password(test_password)
    
    print(f"Hashed Password: {hashed[:15]}...")
    
    # 2. Verify Correct Password
    assert verify_password(test_password, hashed) == True
    print("✅ Password Verification: Correct password matches.")
    
    # 3. Verify Incorrect Password
    assert verify_password("wrong_password", hashed) == False
    print("✅ Password Verification: Incorrect password fails.")

    # 4. Test JWT Token Creation
    test_data = {"user_id": "test_id_123", "email": "test@example.com"}
    token = create_access_token(test_data)
    
    print(f"\nGenerated JWT Token: {token[:20]}...")
    
    if len(token) > 50:
        print("✅ JWT Generation: Successfully created a secure token.")
    else:
        print("❌ JWT Generation: Token length seems too short.")

    print("\n✅ Authentication Cryptography Tests Completed.")

if __name__ == "__main__":
    test_auth_crypto()
