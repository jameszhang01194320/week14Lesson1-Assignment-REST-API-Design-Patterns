from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError

<<<<<<< HEAD
def save(token_id):
=======

def save():
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
<<<<<<< HEAD
    if token_id == order_data['customer_id']:
        new_order = orderService.save(order_data)
        return order_schema.jsonify(new_order), 201
    else:
        return jsonify({"message": "You can't order things for other users... scumbag!"}), 401

def find_all():
    page = request.args.get("page")
    per_page = request.args.get("per_page")
    page = 1 if not page else page
    per_page = 10 if not per_page else per_page
    all_orders = orderService.find_all(page, per_page)
    return orders_schema.jsonify(all_orders), 200

def find_by_id(order_id): #dynamic route takes in parameters
    order = orderService.find_by_id(order_id)
=======
    
    new_order = orderService.save(order_data)
    return order_schema.jsonify(new_order), 201

def find_all():
    all_orders = orderService.find_all()

    return orders_schema.jsonify(all_orders), 200


def find_by_id(order_id):
    order = orderService.find_by_id(order_id)
    if not order:
        return jsonify({"message": "Order not found"}), 404
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f

    return order_schema.jsonify(order), 200


<<<<<<< HEAD
def find_by_customer_id(customer_id, token_id):
    if customer_id == token_id:
        orders = orderService.find_by_customer_id(customer_id)
        return orders_schema.jsonify(orders), 200
    else:
        return jsonify({"message": "Cannot view other customers orders!"}), 401

def find_by_email():
    email = request.json['email']
    if email:
        orders = orderService.find_by_email(email)
        return orders_schema.jsonify(orders), 200
    else:
        return jsonify({"message": "Please insert an email"})
=======
# update
def update(order_id):
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_order = orderService.update_order(order_id, order_data)
    if not updated_order:
        return jsonify({"message": "Order not found"}), 404

    return order_schema.jsonify(updated_order), 200


# delete
def delete(order_id):
    deleted_order = orderService.delete_order(order_id)
    if not deleted_order:
        return jsonify({"message": "Order not found"}), 404

    return jsonify({"message": f"Order with ID {order_id} deleted successfully."}), 200
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
