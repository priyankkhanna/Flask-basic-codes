# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:42:46 2021

@author: priya
"""

from flask import Flask,redirect, url_for
app = Flask(__name__)

@app.route('/admin/administrator')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as guest'%guest

@app.route('/<name>')
def hello_user(name):
    if(name == 'admin'):
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))


if __name__ == '__main__':
    app.run()