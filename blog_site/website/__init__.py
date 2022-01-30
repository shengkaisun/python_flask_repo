from flask import Flask

app = Flask(__name__)

from website.core.views import core
from website.errors.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)