# coding:utf-8

from flask import Flask, render_template, request
from app import app


@app.route('/')
def index():
    client_ip = '127.0.0.1'
    return render_template('index.html', client_ip=client_ip)