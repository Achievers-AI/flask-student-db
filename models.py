from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

class StudentModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer(),unique = True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    dob = db.Column(db.Date())
    amount_due = db.Column(db.Float())
 
    def __init__(self, student_id,first_name,last_name,dob,amount_due):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.amount_due = amount_due
 
    def __repr__(self):
        return f"{self.first_name}:{self.student_id}"