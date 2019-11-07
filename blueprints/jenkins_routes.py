#!/usr/bin/python3

import requests
from flask import Blueprint, render_template, redirect

jenkins_routes = Blueprint('jenkins_routes', __name__)

AUTH=('admin', '4linux123')
JENKINS='http://jenkins.example.com:8080'

@jenkins_routes.route('/jenkins')
def get_jenkins():
    response = requests.get('{}/api/json'.format(JENKINS), auth=AUTH)
    data = response.json() if response.status_code == 200 else []
    return render_template('jenkins.html', jobs=data['jobs'])

@jenkins_routes.route('/jenkins/build/<job>')
def build_jenkins(job):
    response = requests.get('{}/crumbIssuer/api/json'.format(JENKINS), auth=AUTH)
    data = response.json()
    
    headers = {data['crumbRequestField'] : data['crumb']}
    response = requests.post('{}/job/{}/build'.format(JENKINS, job), headers=headers, auth=AUTH)
    return redirect('/jenkins')
