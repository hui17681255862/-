from flask import render_template

from . import index_blu


@index_blu.route("/index")
@index_blu.route("/")
def index():
    return render_template("index/index.html")
