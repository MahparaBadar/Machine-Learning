from dotenv import load_dotenv, find_dotenv
import os

_ : bool = load_dotenv(".env") # read local .env file

print("Hello World")
print(os.environ.get("name"))


from sqlmodel import Field, SQLModel, create_engine, Session, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

engine = create_engine(os.environ.get("db_keys")) #, echo=True)

SQLModel.metadata.create_all(engine)    

obj1 : Hero = Hero()
obj1.name = "abc"
obj1.age = 21
obj1.secret_name = "uvw"

obj2 : Hero = Hero(name = "xyz", secret_name = "rst", age = 23)


with Session(engine) as session:
        session.add(obj1)
        session.add(obj2)
        
        session.commit()


def select_heroes():
    with Session(engine) as session:
        statement = select(Hero)
        results = session.exec(statement)
        for hero in results:
            print(hero)        

select_heroes()            