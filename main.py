from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask import url_for 
from flask import redirect
import json

site = Flask(__name__)




# left off at setting up the database for the webscrapper88******************************


@site.route('/')
def index():
    return render_template('index.html')


site.run(port=5000)