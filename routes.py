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


""" OTHER PAGES """


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html", name="thankyou")


@app.route("/sorry")
def sorry():
    return render_template("sorry.html", name="sorry")


@app.route("/merger_one")
def merger_one():
    return render_template("merger_one.html", name="merger_one")


@app.route("/merger_many")
def merger_many():
    return render_template("merger_many.html", name="merger_many")


@app.route("/splitter")
def split():
    return render_template("splitter.html", name="splitter")


########################################################
@app.route("/send_msg", methods=["POST"])
def send_msg():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            func.write_to_txt(data)
            func.write_to_csv(data)
            return redirect("thankyou")
        except:
            return redirect("sorry")
    else:
        return redirect("sorry")


@app.route("/upload_many/<string:qnt>", methods=["POST"])
def upload_many(qnt):
    if request.method == "POST":
        if qnt == "one":
            try:
                list_files = []
                for r in range(10):
                    u = str(r + 1)
                    uploaded = request.files[u]
                    file = secure_filename(request.files[u].filename)
                    if file != "":
                        file_ext = path.splitext(file)[1]
                        if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                            abort(400)
                        file_path = path.join(app.config["UPLOAD_PATH"], file)
                        uploaded.save(file_path)
                        list_files.append(file_path)
                if list_files:
                    if func.merge_pdf(list_files):
                        return send_from_directory(
                            app.config["UPLOAD_PATH"],
                            "PDF_MERGED.pdf",
                            as_attachment=True,
                        )
                    else:
                        return redirect("sorry")
                else:
                    return redirect("sorry")
            except:
                return redirect("sorry")
        elif qnt == "many":
            try:
                uploaded = request.files.getlist("files")
                list_files = []
                for u in uploaded:
                    file = secure_filename(u.filename)
                    if file != "":
                        file_ext = path.splitext(file)[1]
                        if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                            abort(400)
                        file_path = path.join(app.config["UPLOAD_PATH"], file)
                        u.save(file_path)
                        list_files.append(file_path)
                if list_files:
                    if func.merge_pdf(list_files):
                        return send_from_directory(
                            app.config["UPLOAD_PATH"],
                            "PDF_MERGED.pdf",
                            as_attachment=True,
                        )
                    else:
                        return redirect("sorry")
                else:
                    return redirect("sorry")
            except:
                return redirect("sorry")
            else:
                return redirect("sorry")
        else:
            return redirect("sorry")
    else:
        return redirect("sorry")


@app.route("/upload_one", methods=["POST"])
def upload_one():
    if request.method == "POST":
        try:
            uploaded = request.files["file"]
            file = secure_filename(uploaded.filename)
            if file != "":
                file_ext = path.splitext(file)[1]
                if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                    abort(400)
                file_path = path.join(app.config["UPLOAD_PATH"], file)
                uploaded.save(file_path)
            if func.split_pdf(file_path):
                try:
                    return send_from_directory(
                        app.config["UPLOAD_PATH"], "split.zip", as_attachment=True
                    )
                except:
                    redirect("sorry")
                else:
                    redirect("sorry")
            else:
                return redirect("sorry")
        except:
            redirect("sorry")
        else:
            redirect("sorry")
    else:
        return redirect("sorry")
