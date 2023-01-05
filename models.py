
from sqlalchemy import Column,String,Boolean,Integer
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text

from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text


class Item(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False,unique=True)
    description=Column(Text)
    price=Column(Integer,nullable=False)
    on_offer=Column(Boolean,default=False)


    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"

class accounts(Base):
    __tablename__='accounts'
    id=Column(Integer,primary_key=True)
    name=Column(String(25),nullable=False)
    email=Column(String(55),nullable=False,unique=True)
    password=Column(String(200),nullable=False)
    phone = Column(String(20),nullable=False)
    def __repr__(self) -> str:
        return self.name






















# class user(Base):
#     __tablename__='users'
#     id=Column(Integer,primary_key=True)
#     username=Column(String(25),unique=True)
#     password=Column(String(10),nullable=False)
#     email=Column(String(255),unique=True)
#     is_active=Column(Boolean,default=True)
#     def __repr__(self):
#         return f"<User username={self.username} password={self.password} email={self.email}>"
# class login(Base):
#     __tablename__='login'
#     id=Column(Integer,primary_key=True)
#     username=Column(String(25),unique=True)
#     password=Column(String(10),nullable=False)
#     def __repr__(self):
#         return f"<Login username={self.username} password={self.password}>"        
