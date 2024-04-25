import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'\xbd\x92\xd9\xb7\x95\xcf\xfb|\xbb\x8fM\xe3\x91\x9cCx'"
    
    MONGODB_SETTINGS = {'db': 'VOCAB_TIENG_TRUNG'}