# from app import db, login
# from flask_login import UserMixin
# from datetime import datetime
# from werkzeug.security import generate_password_hash, check_password_hash






# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(20), unique=True, nullable=False)
#     body = db.Column(db.String(255))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         db.session.add(self)
#         db.session.commit()

#     def __repr__(self):
#         return f"<Post|{self.title}>"


# class Address(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True, nullable=False)
#     address = db.Column(db.String(100), unique=True, nullable=False)
#     phonenumber = db.Column(db.String(15), unique=True, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         db.session.add(self)
#         db.session.commit()

#     def __repr__(self):
#         return f"<Address {self.id} | {self.name}>"


#     def __str__(self):
#         return f"""
#         Name: {self.name}
#         Address: {self.address}
#         Phone: {self.phonenumber}
#         """

  
