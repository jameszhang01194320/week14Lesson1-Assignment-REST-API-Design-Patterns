from . import ma
from marshmallow import fields

class CustomerSchema(ma.Schema): #Inherting our instance of Marshmallow 
    id = fields.Integer(required=False) #This will be auto-incremented
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True) 
    username = fields.String(required=True)
    password = fields.String(required=True)
<<<<<<< HEAD
    admin = fields.Integer(required=True)

    class Meta:
        fields = ("id", "name", "email", "phone", "username", "password", "admin") #all fields that could be coming in and going out when validating data

customer_schema = CustomerSchema() #instantiate a single customer schema
customers_schema = CustomerSchema(many=True, exclude=["password"])
=======

    class Meta:
        fields = ("id", "name", "email", "phone", "username", "password") #all fields that could be coming in and going out when validating data

customer_schema = CustomerSchema() #instantiate a single customer schema
customers_schema = CustomerSchema(many=True, exclude=["password"])
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
