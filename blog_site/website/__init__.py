from flask import Flask

app = Flask(__name__)

from website.core.views import core
app.register_blueprint(core)
