from flask import Blueprint

from controllers.orderController import save, find_all, find_by_id, update, delete


order_blueprint = Blueprint("order_bp", __name__)

order_blueprint.route('/', methods=["POST"])(save)
order_blueprint.route('/', methods=["GET"])(find_all)

order_blueprint.route('/<int:product_id>', methods=['GET'])(find_by_id)
order_blueprint.route('/<int:product_id>', methods=['PUT'])(update)
order_blueprint.route('/<int:product_id>', methods=['DELETE'])(delete)