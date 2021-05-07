# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__copyright__ = "Copyright 2021"
__email__ = ""
__date__ = "2021-maio-07"
__version__ = "0.1"
__status__ = "open"

from flask import Flask

app = Flask(__name__)

import routes

""" UPLOAD FILE CONFG """
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = [".pdf", ".PDF", ".txt"]
app.config["UPLOAD_PATH"] = "uploads"
app.config["PDF_MERGED"] = "uploads/PDF_MERGED.pdf"
