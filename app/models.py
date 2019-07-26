from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Regulation(db.Model):
    __tablename__ = 'Regulation'
    
    Regulation_ID = db.Column(db.Integer, primary_key=True)
    Regulation_Reference = db.Column(db.String)
    Regulation_Start_Date = db.Column(db.String)
    Regulation_End_Date = db.Column(db.String)
    Regulation_Number = db.Column(db.String)
    Regulation_Parent = db.Column(db.String)
    Regulation_Text = db.Column(db.String)
    Regulation_Comment = db.Column(db.String)

class Regulation_Types(db.Model):
    __tablename__ = 'Regulations_Types'

    Regulation_Type_ID = db.Column(db.Integer, primary_key=True)
    Type_ID = db.Column(db.Integer)
    Regulation_ID = db.Column(db.Integer)