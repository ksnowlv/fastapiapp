from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = None
SessionLocal = None
Base = declarative_base()

def get_db() :

    global db
    global SessionLocal
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def init_db(mysql_url: str):

    print(f"mysql_url:{mysql_url}")

    engine = create_engine(mysql_url)

    Base.metadata.create_all(bind=engine)
    global SessionLocal
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



