from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask import Flask,render_template, request, flash, redirect, url_for

today = datetime.now()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    drivingLicense = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    joinDate = db.Column(db.Date)
    lessons = db.relationship('Lesson', backref='Lessons')
    reviews = db.relationship('Review', backref='Reviews')
    
class Lesson(db.Model):
    __tablename__ = "lesson"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    startDate = db.Column(db.Date)
    completionDate = db.Column(db.Date)
    cost = db.Column(db.Float)
    car = db.Column(db.String)
    carType = db.Column(db.String)
    postCode = db.Column(db.String)
    customerID = db.Column(db.Integer, db.ForeignKey('customer.id'))
    instructorID = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    review = db.relationship('Review', backref='one_Review')
    

class Instructor(db.Model):
    __tablename__ = "instructor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    drivingLicense = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    joinDate = db.Column(db.Date)
    lessons = db.relationship('Lesson', backref='all_Lessons')
    reviews = db.relationship('Review', backref='all_Reviews')

class Review(db.Model):
    __tablename__ = "review"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    score = db.Column(db.Integer)
    type = db.Column(db.Boolean)
    RVdate = db.Column(db.Date)
    customerID = db.Column(db.Integer, db.ForeignKey('customer.id'))
    InstructorID = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    lessonID = db.Column(db.Integer, db.ForeignKey('lesson.id'))
    
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    joinDate = db.Column(db.Date)
    approvals = db.relationship('Approval', backref='all_Approvals')

class Approval(db.Model):
    __tablename__ = "approval"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    startDate = db.Column(db.Date)
    completionDate = db.Column(db.Date)
    evidence = db.Column(db.LargeBinary)
    approval = db.Column(db.Boolean)    
    userID = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    adminID = db.Column(db.Integer, db.ForeignKey('admin.id'))

@app.route('/')
@app.route('/home')
def home():
    data = Lesson.query.all()
    return render_template('home.html',items = data)

@app.route('/lesson', methods=['GET','POST'])
def lesson():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        startDate = request.form.get('startDate')
        completionDate = request.form.get('endDate')
        cost = request.form.get('cost')
        car = request.form.get('car')
        carType = request.form.get('carType')
        postCode = request.form.get('postCode')

        new_lesson = Lesson(title = title, description = description, startDate = covnertDate(startDate), completionDate = covnertDate(completionDate), cost = cost, car = car, carType = carType, postCode = postCode)
        db.session.add(new_lesson)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('lesson.html')

@app.route('/checkLesson/<int:x>', methods=['GET','POST'])
def checkLesson(x):
    data = Lesson.query.get(x)
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        startDate = request.form.get('startDate')
        completionDate = request.form.get('endDate')
        cost = request.form.get('cost')
        car = request.form.get('car')
        carType = request.form.get('carType')
        postCode = request.form.get('postCode')

        # Update all the text field to database.
        data.title = title
        data.description = description
        data.startDate = covnertDate(startDate)
        data.completionDate = covnertDate(completionDate)
        data.cost = cost
        data.car = car
        data.carType = carType
        data.postCode = postCode

        # Delete the data if button seleted.
        if request.form['submit_button'] == 'Do Something':
            db.session.delete(data)

        db.session.commit()
        return redirect(url_for('home'))
    return render_template('lesson.html', data = data)

@app.route('/register', methods=['GET','POST'])
def register():

    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('uname')
        DriverID = request.form.get('DriverID')
        password1 = request.form.get('password')
        password2 = request.form.get('password1')

        user = Customer.query.filter_by(email=email).first()
        print("Test.........",user)
        if user:
            flash('Email already existed!', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) <2:
            flash('Fist name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Passowrd don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = Customer(email = email, name = firstName, drivingLicense = DriverID, password = generate_password_hash(password1, method='sha256') , joinDate = today)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect(url_for('home'))

    return render_template("register.html", user = current_user)

def covnertTime(x):
    y = datetime.strptime(x,'d/%m/%Y %H:%M:%S')
    return y

def covnertDate(x):
    y = datetime.strptime(x,'%Y-%m-%d')
    return y


if __name__=='__main__':
    app.config['SECRET_KEY'] = 'kds0ndkdfik4ifkf4k9'
    app.run(debug=True, host='0.0.0.0',port='5000')