from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cams.db3')
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class Regulation(Base):
    __tablename__ = 'Regulation'
    
    Regulation_ID = Column(Integer, primary_key=True)
    Regulation_Reference = Column(String)
    Regulation_Start_Date = Column(String)
    Regulation_End_Date = Column(String)
    Regulation_Number = Column(String)
    Regulation_Parent = Column(String)
    Regulation_Text = Column(String)
    Regulation_Comment = Column(String)

class Regulation_Types(Base):
    __tablename__ = 'Regulations_Types'

    Regulation_Type_ID = Column(Integer, primary_key=True)
    Type_ID = Column(Integer)
    Regulation_ID = Column(Integer)

for instance in session.query(Regulation)\
    .join(Regulation_Types, Regulation.Regulation_ID==Regulation_Types.Regulation_ID)\
    .filter(Regulation_Types.Type_ID == '2')\
    .order_by(Regulation.Regulation_Number):
    print (instance.Regulation_Number)





