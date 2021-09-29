# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:30:57 2021

@author: priya
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<user>')
def welcome(user):
    return render_template('hello_template.html', name = user)

if __name__ == '__main__':
    app.run()