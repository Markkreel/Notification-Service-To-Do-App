from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base

TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

test_engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def get_test_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()
