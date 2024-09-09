from flask import Blueprint

<<<<<<< HEAD
from controllers.productController import save, find_all, search_product
=======
from controllers.productController import save, find_all, search_product, find_by_id, update, delete
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f

product_blueprint = Blueprint("product_bp", __name__)

#where we put our url_endpoints
<<<<<<< HEAD
product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/', methods=['GET'])(find_all)
product_blueprint.route('/search', methods=['GET'])(search_product)
=======
product_blueprint.route('/', methods=['POST'])(save) # add new
product_blueprint.route('/', methods=['GET'])(find_all)
product_blueprint.route('/search', methods=['GET'])(search_product)
product_blueprint.route('/<int:product_id>', methods=['GET'])(find_by_id)
product_blueprint.route('/<int:product_id>', methods=['PUT'])(update)
product_blueprint.route('/<int:product_id>', methods=['DELETE'])(delete)
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
