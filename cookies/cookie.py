# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:11:33 2021

@author: priya
"""

from flask import Flask, render_template,request, make_response, redirect, url_for
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')
    
@app.route('/setcookie', methods = ['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
    resp = make_response()
    resp.set_cookie('userid',user)
    return redirect(url_for('getcookie'))
    
    
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userid')
    return '<h1> welcome '+ name + '</h1>'
    

if __name__ == '__main__':
    app.run()