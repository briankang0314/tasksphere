from flask_login import UserMixin
from . import db  # Import db from models/__init__.py

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Relationships
    tasks = db.relationship('Task', backref='user', lazy=True)
    meetings = db.relationship('Meeting', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

    @staticmethod
    def get(user_id):
        return User.query.get(int(user_id))

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()
  