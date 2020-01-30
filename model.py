from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Book(Base):
   __tablename__ = 'books'
   id = Column(Integer, primary_key=True)
   bookname = Column(String)
   author = Column(String)
   pages= Column(String)
   description= Column(String)
   image= Column(String)
