from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.dialects.mysql import *
from sqlalchemy.ext.declarative import declarative_base 

base = declarative_base()

class users(base):
    __tablename__="users"
    id = Column('id',INT(),nullable=False,primary_key=True)
    name = Column('name',VARCHAR(255),nullable=False)
    email = Column('email',VARCHAR(255),nullable=False,unique=True)
    password = Column('password',VARCHAR(60),nullable=False)
    remember_token = Column('remember_token',VARCHAR(100))
    created_at = Column('created_at',TIMESTAMP(),nullable=False)
    updated_at = Column('updated_at',TIMESTAMP(),nullable=False)

class migrations(base):
    __tablename__="migrations"
    migration = Column('migration',VARCHAR(255),nullable=False)
    batch = Column('batch',INT(),nullable=False)
