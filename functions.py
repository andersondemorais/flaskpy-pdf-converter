# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__copyright__ = "Copyright 2021"
__email__ = ""
__date__ = "2021-maio-07"
__version__ = "0.1"
__status__ = "open"

from pprint import pformat
import csv
from datetime import date
import time
from os import path, remove, mkdir
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
import zipfile
from shutil import rmtree

from server import app


def write_to_txt(data):
    with open("database/database.txt", mode="a") as database:
        data["date"] = (
            date.today().strftime("%d/%m/%y")
            + "_"
            + time.strftime("%H:%M:%S", time.localtime())
        )
        txt = pformat(data)
        file = database.write("\n" + txt)


def write_to_csv(data):
    with open("database/database.csv", mode="a", newline="") as database:
        date_time = (
            date.today().strftime("%d/%m/%y")
            + "_"
            + time.strftime("%H:%M:%S", time.localtime())
        )
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = csv.writer(
            database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        file.writerow([email, subject, message, date_time])


def merge_pdf(files):
    for file in files:
        if not path.exists(file):
            return False
    try:
        if path.exists(app.config["PDF_MERGED"]):
            remove(app.config["PDF_MERGED"])
        merger = PdfFileMerger()
        for file in files:
            pdf = PdfFileReader(file)
            merger.append(pdf)
            remove(file)
        merger.write(app.config["PDF_MERGED"])
        return True
    except:
        pass
    else:
        return False


def split_pdf(file):
    if not path.exists(file):
        return False
    try:
        split = path.join(app.config["UPLOAD_PATH"], "split")
        if path.exists(split):
            rmtree(split)
        mkdir(split)
        split_zip_path = path.join(app.config["UPLOAD_PATH"], "split.zip")
        if path.exists(split_zip_path):
            remove(split_zip_path)
        split_zip = zipfile.ZipFile(split_zip_path, "w")

        with split_zip:
            with open(file, "rb") as f:
                reader = PdfFileReader(f)
                for p in range(reader.numPages):
                    writer = PdfFileWriter()
                    writer.addPage(reader.getPage(p))
                    page = "PAG_{}.pdf".format(p + 1)
                    page = path.join(split, page)
                    with open(page, "wb") as pdf:
                        writer.write(pdf)
                    split_zip.write(page)
            remove(file)
        rmtree(split)
        return True
    except:
        pass
    else:
        return False
