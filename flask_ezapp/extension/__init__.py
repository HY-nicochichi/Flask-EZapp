from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .server_side_session import ServerSideSession
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman
from datetime import datetime

class Extension():

    def __init__(
        self,
        ext_dict={
            'db_orm': False,
            'db_migration': False,
            'server_side_session': False,
            'csrf_protection': False
        }
    ):
        self.ext_dict = ext_dict
        if self.ext_dict['db_orm'] == True:
            self.db_orm = SQLAlchemy()
            setattr(
                self.db_orm.Model,
                '__abstract__',
                True
            )
            setattr(
                self.db_orm.Model,
                'id',
                self.db_orm.Column(
                    self.db_orm.Integer, primary_key=True
                )
            )
            setattr(
                self.db_orm.Model,
                'created',
                self.db_orm.Column(
                    self.db_orm.DateTime, default=datetime.now, nullable=False
                )
            )
            setattr(
                self.db_orm.Model,
                'updated',
                self.db_orm.Column(
                    self.db_orm.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
                )
            )
            if self.ext_dict['db_migration'] == True:
                self.migrate = Migrate()
            if self.ext_dict['server_side_session'] == True:
                self.server_session = ServerSideSession()
        if ext_dict['csrf_protection'] == True:
            self.csrf_protection = CSRFProtect()
        if ext_dict['security_header'] == True:
            self.security_header = Talisman()

    def init_app(self, app):
        if self.ext_dict['db_orm'] == True:
            self.db_orm.init_app(app)
            if self.ext_dict['db_migration'] == True:
                self.migrate.init_app(app, self.db_orm)
            if self.ext_dict['server_side_session'] == True:
                self.server_session.init_app(app)
        if self.ext_dict['csrf_protection'] == True:
            self.csrf_protection.init_app(app)
        if self.ext_dict['security_header'] == True:
            talisman_dict = app.config['TALISMAN_SECURITY_HEADER']
            self.security_header.init_app(
                app,
                content_security_policy=talisman_dict['content_security_policy'],
                force_https=talisman_dict['content_security_policy'],
                session_cookie_secure=talisman_dict['content_security_policy']
            )
        if self.ext_dict['db_orm'] == True:
            with app.app_context():
                self.db_orm.create_all()
