import functools

from flaskr.db import get_db

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash


#Create a blueprint named auth and configure it with a prefix to add to the URLs it is related to.
bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=("GET", "POST"))
def register():

    if (request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        error = None

        #If cases to check if the parameters are satisfied
        if not username:
            error = "Username is required"
        elif not password:
            error = "Password is required"

