from datetime import timedelta
from .extension import ext_dict

if ext_dict['db_orm'] == True:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sampledb.sqlite3'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    if ext_dict['server_side_session'] == True:
        BEAKER_SESSION = {
            'session.key': 'session_id',
            'session.type': 'ext:database',
            'session.url': 'sqlite:///localdb/sampledb.sqlite3',
            'session.table_name': 'sessions',
            'session.httponly': True,
            'session.cookie_expires': timedelta(days=10.0),
            'session.auto': True,
            'session.secret': 'Sample_Secret_Key'
        }
if ext_dict['csrf_protection'] == True:
    SECRET_KEY = 'Sample_Secret_Key'
if ext_dict['security_header'] == True:
    TALISMAN_SECURITY_HEADER = {
        'force_https': False,
        'session_cookie_secure': False,
        'content_security_policy': {
            'default-src': [
                '\'self\'',
                '\'unsafe-inline\'',
                '\'unsafe-eval\'',
                'stackpath.bootstrapcdn.com',
                'code.jquery.com',
                'cdn.jsdelivr.net'
            ]
        }
    }
