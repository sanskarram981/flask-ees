from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sanskar.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class students(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.String(30),nullable=False)
    lname = db.Column(db.String(30),nullable=False)
    year = db.Column(db.String(4),nullable=False)
    password = db.Column(db.String(12),nullable=False)
    date_cr = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} --> {self.year}"

@app.route('/',methods=['GET','POST'])
def home():
    #return "Hello World!!"
    if request.method=='POST':
        fname = request.form['fname']
        lname = request.form['lname']
        year = request.form['year']
        password = request.form['password']
        stud = students(fname=fname,lname=lname,year=year,password=password)
        db.session.add(stud)
        db.session.commit()
    stud1 = students.query.all()
    return render_template("home.html",stud1=stud1)

@app.route("/delete/<int:sno>",methods=['GET','POST'])
def delete(sno):
    stud3 = students.query.filter_by(sno=sno).first()
    db.session.delete(stud3)
    db.session.commit()
    return redirect("/")
    

@app.route("/update/<int:sno>",methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        fname = request.form['fname']
        lname = request.form['lname']
        year = request.form['year']
        password = request.form['password']
        stud4 = students.query.filter_by(sno=sno).first()
        stud4.fname = fname
        stud4.lname = lname
        stud4.year = year
        stud4.password = password
        db.session.add(stud4)
        db.session.commit()
        return redirect("/")
    stud4 = students.query.filter_by(sno=sno).first()
    return render_template("update.html",studk=stud4)

@app.route("/show")
def show():
    stud1 = students.query.all()
    print(stud1)
    return "This is a show page"

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/res_dev")
def res_dev():
    return render_template("res_dev.html")

@app.route('/misc')
def misc():
    return render_template("misc.html")

@app.route("/student_info")
def student_info():
    return render_template("student_info.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/notice_anno")
def notice_anno():
    return render_template("notice_anno.html")

@app.route("/sports_culture")
def sports_culture():
    return render_template("sports_culture.html")

if __name__ == "__main__":
    app.run(debug=True)