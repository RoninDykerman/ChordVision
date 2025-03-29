"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from __init__ import app

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'home.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/library')
def library():
    return render_template(
        'library.html',
        year=datetime.now().year
    )

@app.route('/tutorial')
def tutorial():
    return render_template(
        'tutorial.html',
        year=datetime.now().year
    )

@app.route('/legend')
def legend():
    return render_template(
        'legend.html',
        year=datetime.now().year
    )

@app.route('/hotel_california')
def hotel_california():
    return render_template(
        'hotel_california.html',
        year=datetime.now().year
    )

@app.route('/thatll_be_the_day')
def thatll_be_the_day():
    return render_template(
        'thatll_bethe_day.html',
        year=datetime.now().year
    )

@app.route('/la_bamba')
def la_bamba():
    return render_template(
        'la_bamba.html',
        year=datetime.now().year
    )

@app.route('/let_it_be')
def let_it_be():
    return render_template(
        'let_it_be.html',
        year=datetime.now().year
    )

@app.route('/take_it_easy')
def take_it_easy():
    return render_template(
        'take_it_easy.html',
        year=datetime.now().year
    )

@app.route('/come_on_lets_go')
def come_on_lets_go():
    return render_template(
        'come_on_lets_go.html',
        year=datetime.now().year
    )