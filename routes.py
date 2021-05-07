# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__copyright__ = "Copyright 2021"
__email__ = ""
__date__ = "2021-maio-07"
__version__ = "0.1"
__status__ = "open"

from server import app
from flask import render_template

""" MAIN PAGES """


@app.route("/")
def index():
    return render_template("index.html", name="index")


@app.route("/works")
def works():
    return render_template("works.html", name="works")


@app.route("/about")
def about():
    return render_template("about.html", name="about")


@app.route("/contact")
def contact():
    return render_template("contact.html", name="contact")


@app.route("/components")
def components():
    return render_template("components.html", name="components")
