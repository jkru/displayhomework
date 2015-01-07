from flask import Flask, request, render_template
from flask import redirect, url_for, flash, session, jsonify
#from gethw import get_english, get_science, get_math, get_world
import gethw
import os
from urllib import urlopen

app = Flask(__name__)

FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "asdf") 
app.secret_key = FLASK_SECRET_KEY

@app.route("/")
def home():
    math = "https://sites.google.com/a/kealing.org/ms-girardeau-sixth-grade-math/homework-assignments"
    world = "https://sites.google.com/a/austinisd.org/mr-shoaf-s-classroom/world-cultures"
    science = "https://sites.google.com/a/austinisd.org/mcdonald-6th-grade-science/home/science-assignments"
    english = "http://stewartkealing.weebly.com/magnet-6th-grade-english.html"

    math_link = gethw.get_math(math)
    english_info = gethw.get_english(english)

    english_info = english_info.replace(u"&rsquo;","'").replace(u"&ldquo;","'").replace(u"&rdquo;","'")
    english_info = english_info.replace(u"&ndash;","-")
    english_info = english_info.split("&nbsp;")
    science_info = gethw.get_science(science).split("\n")

    return render_template("index.html",math_link=math_link,english_info=english_info,science_info=science_info)

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run (host="0.0.0.0",port=PORT)
