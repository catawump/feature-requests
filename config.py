import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'i-am-a-being-of-pure-energy-with-no-weakness'
