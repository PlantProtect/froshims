from cs50 import SQL
from flask import Flask,render_template,request,redirect

app =Flask(__name__)

db = SQL("sqlite:///froshims.db")

REGISTERANTS = {}

SPORTS = [
  "Basketball",
  "Soccer",
  "Ultimate Frisbee",
  "PingPong"
]


@app.route("/")
def index():
  return render_template("index.html",sports = SPORTS)


@app.route("/register",methods=["POST"])
def registert():

#validate name
  name = request.form.get("name")
  if not name:
     return render_template("error.html",message="Missing name,Please type name")
#Validate submission
  sport = request.form.get("sport") 
  if not sport:
    return render_template("error.html",message="Miss sport")
  if sport not in SPORTS:
     return render_template("error.html",message="Invalid sport")
  
 #Remeber registerant
  REGISTERANTS[name] =sport

  #Confirm registration
  return redirect("/registrants")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html",registrants=REGISTERANTS)
  