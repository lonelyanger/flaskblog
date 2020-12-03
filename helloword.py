from flask import Flask
from flask import request
from flask import redirect
from flask import make_response
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')    
    response.set_cookie('answer', '42')     
    return response
    # return '<h1>Bad Request</h1>',400
# def index():
#     user_agent=request.headers.get('User-Agent')

#     return '<p>Your browser is{}</p>'.format(user_agent)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,{}!</h1>'.format(name)


app.run(debug=True)