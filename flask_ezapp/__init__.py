from flask import Flask, session, request, g, current_app
import inspect, subprocess

def new():
    remote = 'https://github.com/HY-nicochichi/ezapp'
    subprocess.run(['git', 'clone', remote])

class EZapp(Flask):

    def __init__(self, host_matching=False, subdomain_matching=False, root_path=None):
        static = inspect.stack()[1].filename[:-7]+'static'
        views = inspect.stack()[1].filename[:-7]+'views'
        localdb = inspect.stack()[1].filename[:-7]+'localdb'
        super().__init__('EZapp', None, static, None, host_matching, subdomain_matching, views, localdb, False, root_path)
    
    def app_setup(self, router_list):
        file = inspect.stack()[1].filename[:-7]+'setting.py'
        self.config.from_pyfile(file)
        for router in router_list:
            self.register_blueprint(router)

class Globals():
    def __init__(self):
        self.session = session
        self.request = request
        self.args = g
        self.app = current_app

glo = Globals()
