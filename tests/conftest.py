"""This module contains test fixtures and configuration for the notification service tests.
Provides common setup and teardown functionality used across test cases.
"""

import os
import sys
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models.task import TaskDB

# Add the project root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

test_engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(scope="function")
def db():
    # Create all tables
    Base.metadata.create_all(bind=test_engine)

    # Create a new session for the test
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Drop all tables after the test
        Base.metadata.drop_all(bind=test_engine)
