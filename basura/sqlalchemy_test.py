from sqlalchemy import create_engine
from app.db.models import Base

DATABASE_URL= "postgresql://postgres:1008@localhost:5432/BD"

engine = create_engine(DATABASE_URL)


def main():
    create_tables()

def create_tables():
    Base.metadata.create_all(engine)

if __name__=="__main__":
    main()