from flask_marshmallow import Marshmallow
from models import Puppy

ma = Marshmallow()


class PuppySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Puppy
        load_instance = True

puppy_schema = PuppySchema()
