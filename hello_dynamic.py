# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:27:28 2021

@author: priya
"""

from flask import Flask
app = Flask(__name__)


@app.route('/<name>')
def hello_world(name):
    return "hello %s"%name

if __name__ == '__main__':
    app.run()