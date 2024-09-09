from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from cache import cache


def save(): #name the controller the same as the service it recruites

    try:
        customer_data = customer_schema.load(request.json)
    
    except ValidationError as e:
        return jsonify(e.messages), 400 #return error message with a 400 failed response
    
    customer = customerService.save(customer_data)
    return customer_schema.jsonify(customer), 201 #send them the customer object with a 201 successful creation status


@cache.cached(timeout=120)
def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers), 200


# add find_by_id Method
def find_by_id(customer_id):
    customer = customerService.find_by_id(customer_id)

    if not customer:
        return jsonify({"message": "Customer not found"}), 404

    return customer_schema.jsonify(customer), 200

def update(customer_id):
    customer = customerService.find_by_id(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400


    if 'password' not in customer_data:  # If password is not in the request, keep the existing one
        customer_data['password'] = customer.password

    updated_customer = customerService.update(customer_id, customer_data)
    return customer_schema.jsonify(updated_customer), 200


def delete(customer_id):
    customer = customerService.delete(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify({"message": "Customer deleted successfully"}), 200
