from app import db


class sample(db.Model):
    __tablename__ = "sample"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    User_Name = db.Column(db.String(200), unique=True, nullable=False)
    User_Email = db.Column(db.String(350), nullable=False)
    User_Password = db.Column(db.String(200), nullable=False)
