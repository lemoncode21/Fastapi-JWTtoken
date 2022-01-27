from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



# Database configuration connect to postgresql
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/user_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# JWT Configuration

SECRET_KEY="lemoncode21"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
