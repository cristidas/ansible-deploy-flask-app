import os
from flask import Flask, render_template


IS_PRODUCTION = os.environ.get('APP_ENV', 'development') == 'production'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', is_production=IS_PRODUCTION)

