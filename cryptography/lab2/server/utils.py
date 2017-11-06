import random

from flask import jsonify

s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_session_key(length):
    return ''.join(random.sample(s, length))


def json(data, error=None):
    return jsonify({'data': data, 'error': error})