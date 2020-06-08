from flask import Blueprint

from App.ext import db
from App.models import Students

blue = Blueprint("blue", __name__, url_prefix="/db/")


def init_blue(app):
    app.register_blueprint(blue)


@blue.route("/")
def index():
    return "hello"


@blue.route("/addstudent")
def add_student():
    student = Students()
    student.name = "jonathan"
    db.session.add(student)
    db.session.commit()
    return "Add Student Success"


@blue.route("/delstudent")
def delete_student():
    student = Students.query.limit(1).all()
    print(student)
    # db.session.delete(student)
    # db.session.commit()

    return "Delete Student Success"
