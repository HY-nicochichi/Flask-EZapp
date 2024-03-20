from ezapp.models import SampleModel

class SampleHelper():
    
    def func1(value):
        found = SampleModel.query.filter_by(param1=value).first()
        print(found)

    def func2(value):
        found = SampleModel.query.filter_by(param2=value).all()
        print(found)
