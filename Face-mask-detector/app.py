from sys import stdout
import logging
from flask import Flask, render_template, Response, request
from camera import Camera
import werkzeug, os, glob
import json
import numpy as np
import base64
import pickle

loaded_model = pickle.load(open('face_mask_detector.model', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run(debug = True)