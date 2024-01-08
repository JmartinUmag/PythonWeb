from sqlalchemy import create_engine, Column, Integer, String
from sqlachemy.orm import declarative_base, relationship

engine = create_engine("postgres://user:pass@localhost/db", echo=True)

Base= declarative_base()

class User(Base):
    __tablename__ = "users"

    id= Column(Integer, primary_key=True)
    name = Column(String(32))
    fullname = Column(String(64))

    adresses = relationship("Adress", back_populates="user")

    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.fullname}')>"

class Adress(Base):
    __tablename__ = "addresses"

    id= Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id")) #Llave foranea de la tabla users

    def __repr__(self):
        return f"<Adress(email_address='{self.email_address}')>"

with engine.connect() as connection:
    #Esto crea la base de datos
    Base.metadata.create_all(connection)
    
    user = User(name="ed", fullname="Ed Jones")
    adress = Adress(email_address="test@test.com")
    user.adresses.append(adress)

    sesion = Session()
    session.add(user)
    session.commit()



#Forma antigua
# with engine.connect() as connection:
#     connection.execute("CREATE TABLE mytable(x int, y int)")
#     connection.execute("INSERT INTO mytable(x,y) VALUES(1,1)")
#     reult = connection.execute("SELECT * FROM mytable")
#     #existe fetchone() y fetchall()
#     print(result.fetchall())