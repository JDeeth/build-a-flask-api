from flask_marshmallow import Marshmallow
from models import User, Puppy

ma = Marshmallow()


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


user_schema = UserSchema()


class PuppySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Puppy
        load_instance = True


puppy_schema = PuppySchema()
puppies_schema = PuppySchema(many=True)
