from flask import Flask, request, session, g, redirect, url_for, abort, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

import ConferenceSoftware.henry
import ConferenceSoftware.nick
import ConferenceSoftware.main
