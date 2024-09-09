from flask import Blueprint

<<<<<<< HEAD
from controllers.orderController import find_by_email, find_by_id, save, find_all, find_by_customer_id
=======
from controllers.orderController import save, find_all, find_by_id, update, delete
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f


order_blueprint = Blueprint("order_bp", __name__)

order_blueprint.route('/', methods=["POST"])(save)
order_blueprint.route('/', methods=["GET"])(find_all)
<<<<<<< HEAD
order_blueprint.route('/<int:order_id>', methods=['GET'])(find_by_id)
order_blueprint.route('/customer/<int:customer_id>', methods=['GET'])(find_by_customer_id)
order_blueprint.route('/customer-email', methods=["POST"])(find_by_email)
=======

order_blueprint.route('/<int:product_id>', methods=['GET'])(find_by_id)
order_blueprint.route('/<int:product_id>', methods=['PUT'])(update)
order_blueprint.route('/<int:product_id>', methods=['DELETE'])(delete)
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
