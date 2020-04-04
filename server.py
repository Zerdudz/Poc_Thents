from flask import Flask, render_template, request, url_for, send_file, redirect
import requests, datetime, json
from io import BytesIO

app = Flask(__name__)

# PAGES
@app.route('/')
def accueil():
    return render_template("index.html")
