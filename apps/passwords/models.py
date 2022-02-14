from database.database import db


class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(100))
    email = db.Column(db.String(50))
    password = db.Column(db.String(20))

    def __init__(self, website, email, password):
        self.website = website
        self.email = email
        self.password = password
