from flask_ezapp.extension import Extension

ext_dict = {
    'db_orm': True,
    'db_migration': True,
    'server_side_session': True,
    'csrf_protection': True,
    'security_header': True
}

ext = Extension(ext_dict)
