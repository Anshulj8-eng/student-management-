from flask import Flask,request, redirect, url_for, session, Response,render_template
app = Flask(__name__)
app.secret_key="supersecret"
students =[]
#home
@app.route("/")
def home():
    return render_template("login.html")
#login
@app.route("/login" , methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username=="anshul" and password=="pass":
        session["user"]=username
        return redirect(url_for("dashboard"))
    else:
        return "Invalid credential"
    
#dashboard
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("home"))
    
    return render_template("dashboard.html", user=session["user"], students=students)

#logout
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("home"))
#add 
@app.route("/add")
def add():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("add_students.html")
#add student
@app.route("/add_students", methods=["POST"])
def add_students():
    name = request.form.get("name")
    roll = request.form.get("roll")
    marks = request.form.get("marks")
    subjects = request.form.get("subjects")

    students.append({
        "name":name,
        "roll":int(roll),
        "marks":int(marks),
        "subjects":subjects
    })
    return redirect(url_for("dashboard"))
if __name__ == "__main__":
    app.run(debug=True)
