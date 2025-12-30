from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://roshan:roshan123@localhost:5432/jobtracker')


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def check_connection():

    db = SessionLocal()
    try:
        db.execute(text("SELECT 1"))
        print("Connected successfully to PostgreSQL")
    except Exception as e:
        print(f"Connection failed: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    check_connection()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()