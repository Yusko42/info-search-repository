from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(255),
        nullable=False
    )


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    short_name = db.Column(db.String(50), nullable=False)
    founded_date = db.Column(db.Date, nullable=False)

    students = db.relationship(
        'Student',
        backref='university',
        lazy=True
    )

    def __repr__(self):
        return self.short_name


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

    university_id = db.Column(
        db.Integer,
        db.ForeignKey('university.id'),
        nullable=False
    )

    enrollment_year = db.Column(
        db.Integer,
        nullable=False
    )

    def __repr__(self):
        return self.full_name