﻿from flask import blueprint

views = blueprint(__name__, "views")

@app.route("/")
def home():
    return "page d'acceuil"
