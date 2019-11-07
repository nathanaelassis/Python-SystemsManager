#!/usr/bin/python3

import requests
from flask import Blueprint, render_template, redirect

gitlab_routes = Blueprint('gitlab_routes', __name__)

TOKEN = 'yVC5mpyyo4vL3vMyh6op'
GITLAB  = 'http://gitlab.example.com/api/v4'
headers = {'Private-Token': TOKEN}

@gitlab_routes.route('/gitlab')
def get_gitlab():
    response = requests.get('{}/users?private_token={}'.format(GITLAB, TOKEN))

    users = response.json() if response.status_code == 200 else [] 
    return render_template('gitlab.html', users=users)
