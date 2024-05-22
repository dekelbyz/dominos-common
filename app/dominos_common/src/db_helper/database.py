from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os


try:
    engine = create_engine(os.environ["CONNECTION_STRING"])
except Exception:
    raise Exception('Please provide a db connection string')

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()


def get_db():
    database: Session = SessionLocal()
    try:
        yield database
    except Exception:
        raise Exception('Failed to connect to db')
    finally:
        database.close()
