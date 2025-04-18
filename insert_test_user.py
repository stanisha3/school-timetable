from database import SessionLocal
from models import Teacher
from auth import get_password_hash

# Create a test user
def insert_test_user():
    db = SessionLocal()
    hashed_password = get_password_hash("testpassword")  # Hash the password
    test_user = Teacher(
        name="Test User",
        email="testuser@example.com",
        hashed_password=hashed_password,
    )
    db.add(test_user)
    db.commit()
    db.close()
    print("Test user inserted successfully!")

if __name__ == "__main__":
    insert_test_user()