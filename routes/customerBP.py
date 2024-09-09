from flask import Blueprint
<<<<<<< HEAD
from controllers.customerController import save, find_all
=======
from controllers.customerController import save, find_all, find_by_id, update, delete
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f


customer_blueprint = Blueprint('customer_bp', __name__)

#url_prefix for this blueprint is /customers

customer_blueprint.route('/', methods=['POST'])(save) #triggers the save function on POST request to /customers
customer_blueprint.route('/', methods=['GET'])(find_all)
<<<<<<< HEAD

=======
customer_blueprint.route('/<int:customer_id>', methods=['GET'])(find_by_id)
customer_blueprint.route('/<int:customer_id>', methods=['PUT'])(update)  # add new
customer_blueprint.route('/<int:customer_id>', methods=['DELETE'])(delete)
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
