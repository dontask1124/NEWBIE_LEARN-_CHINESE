import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class user(db.Document):
    User_ID = db.IntField(max_length= 30, unique=True)
    First_Name = db.StringField(max_length= 30)
    Last_Name = db.StringField(max_length= 30)
    Username = db.StringField(max_length= 30)
    Password = db.StringField(max_length= 30)

    
    def set_password(self, passWord):
        self.passWord = generate_password_hash(passWord)
    
    def get_password(self , passWord):
        return check_password_hash(self.passWord, passWord) 
    
class vocabulary(db.Document):
    vocab_ID =  db.StringField(max_length =30 , unique = True)
    tieng_Viet = db.StringField(max_length =100)
    phien_Am = db.StringField(max_length =100)
    tieng_Trung = db.StringField(max_length =100)
    phan_Loai = db.StringField(max_length =70)
    y_Nghia = db.StringField(max_length =300)