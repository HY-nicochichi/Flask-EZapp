from flask import Flask, session, request, g, current_app
import inspect

def new():
    print("new new neeeeeeeew !!!!!")

class EZapp(Flask):

    def __init__(self, host_matching=False, subdomain_matching=False, root_path=None):
        static = inspect.stack()[1].filename[:-7]+'static'
        views = inspect.stack()[1].filename[:-7]+'views'
        super().__init__('EZapp', None, static, None, host_matching, subdomain_matching, views, None, False, root_path)
    
    def app_setup(self, router_list):
        file = inspect.stack()[1].filename[:-7]+'setting.py'
        print(file)
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
