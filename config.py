import os
_basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:////'+os.path.join(_basedir, 'app.db')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'so-secret-much_WAO'
