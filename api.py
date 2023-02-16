#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def root():
    return json.dumps("Hello World!")


@app.route('/redirect')
def redirect():
    return app.redirect(location=request.args.get('dest'), code=302)


@app.route('/print/<info>')
def print(info: str):
    return jsonify(info)


app.run()
