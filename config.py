#!/usr/bin/python3

from functools import wraps
from flask import request, redirect, session, g

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.auth:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function
