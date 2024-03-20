from ezapp.extension import ext

class SampleModel(ext.db_orm.Model):

    __tablename__ = 'sample'
    param1 = ext.db_orm.Column(ext.db_orm.Integer, nullable=False, unique=True)
    param2 = ext.db_orm.Column(ext.db_orm.String(255), nullable=False)
