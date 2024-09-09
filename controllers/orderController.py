from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError


def save():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_order = orderService.save(order_data)
    return order_schema.jsonify(new_order), 201

def find_all():
    all_orders = orderService.find_all()

    return orders_schema.jsonify(all_orders), 200


def find_by_id(order_id):
    order = orderService.find_by_id(order_id)
    if not order:
        return jsonify({"message": "Order not found"}), 404

    return order_schema.jsonify(order), 200


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