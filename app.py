# coding:utf-8

from flask import Flask


app = Flask(__name__, template_folder='templates', static_folder="static")

app.config.from_pyfile("config.py")
