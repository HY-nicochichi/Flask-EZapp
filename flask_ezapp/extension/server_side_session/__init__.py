from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware

class ServerSideSessionInterface(SessionInterface):

    def open_session(self, app, request):
        return request.environ['beaker.session']
        
    def save_session(self, app, session, response):
        session.save()

class ServerSideSession(object):
    
    def init_app(self, app):
        self.app = app
        self._session_conf = app.config['BEAKER_SESSION']
        app.wsgi_app = SessionMiddleware(app.wsgi_app, self._session_conf)
        app.session_interface = ServerSideSessionInterface()
