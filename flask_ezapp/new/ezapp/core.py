from flask_ezapp import EZapp
from .controllers import routers
from .extension import ext

app = EZapp()

app.app_setup(routers)

ext.init_app(app)
