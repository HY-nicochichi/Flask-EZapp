from flask_ezapp.controller import Router
from flask_ezapp import glo
from ezapp.helpers import SampleHelper

sample_router = Router('sample', __name__)

@sample_router.get('/')
def hello_world():
    type = glo.request.args.get(key='type', type=str, default='json')
    data = {'message': 'hello world !'}
    if type == 'json':
        return sample_router.send_resp('json', data)
    elif type == 'html':
        return sample_router.send_resp('html', 'sample.html', data=data)
