# coding=utf-8
from flask import render_template, flash, request
from . import main


@main.route('/')
def index():
    return render_template('index.html', title='Welcome')


@main.route('/services')
def services():
    return 'Service'


@main.route('/about')
def about():
    return 'About'


@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@main.app_template_test('current_link')
def is_current_link(link):
    return link == request.path
