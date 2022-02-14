from database.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(20))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
