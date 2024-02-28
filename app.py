# import libraries
import os
from flask import (
    Flask,
    render_template)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# ---------------------------------------------------------
# Web site
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/advertising")
def advertising():
    return render_template("advertising.html")


@app.route("/app")
def app_page():
    return render_template("app.html")

@app.route("/appdetail")
def appdetail():
    return render_template("appdetail.html")

@app.route("/consulting")
def consulting():
    return render_template("consulting.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/logocreation")
def logocreation():
    return render_template("logocreation.html")

@app.route("/otherservices")
def otherservices():
    return render_template("otherservices.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/webdevelopment")
def webdevelopment():
    return render_template("webdevelopment.html")

if __name__ == "__main__":
    app.run()

