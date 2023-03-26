from os import abort
from flask import Flask,render_template,request,redirect
from models import db,StudentModel
from datetime import datetime
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
@app.route('/index', methods = ['GET','POST'])
def index():
    students = StudentModel.query.all()
    return render_template('index.html', students = students)
 
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        student_id = request.form['student_id']
        first_name = request.form['fname']
        last_name = request.form['lname']
        datofb = request.form['dob']
        dob = datetime.strptime(datofb, '%Y-%m-%d')
        amount_due = request.form['amtdue']
        student = StudentModel(student_id=student_id, first_name=first_name, last_name=last_name, dob=dob, amount_due=amount_due)
        db.session.add(student)
        db.session.commit()
        return redirect('/index')
 
 
@app.route('/data', methods = ['GET','POST'])
def RetrieveList():
    students = StudentModel.query.all()
    return render_template('datalist.html',students = students)
 
 
@app.route('/getstudentbyId', methods = ['GET','POST'])
def RetrieveStudent():
    id = request.form['id']
    student = StudentModel.query.filter_by(student_id=id).first()
    if student:
        return render_template('data.html', student = student)
    return f"Student with id ={id} Does not exist"
 
 
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    student = StudentModel.query.filter_by(student_id=id).first()
    if request.method == 'POST':
        if student:
            db.session.delete(student)
            db.session.commit()
            first_name = request.form['fname']
            last_name = request.form['lname']
            datofb = request.form['dob']
            dob = datetime.strptime(datofb, '%Y-%m-%d')
            amount_due = request.form['amtdue']
            student = StudentModel(student_id=id, first_name=first_name, last_name=last_name, dob=dob, amount_due=amount_due)
            db.session.add(student)
            db.session.commit()
            return redirect(f'/index')
        return f"Student with id = {id} Does not exist"
 
    return render_template('update.html', student = student)
 
 
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    student = StudentModel.query.filter_by(student_id=id).first()
    if request.method == 'POST':
        if student:
            db.session.delete(student)
            db.session.commit()
            return redirect('/index')
        abort(404)
 
    return render_template('delete.html')
 
app.run(host='0.0.0.0', port=5000)