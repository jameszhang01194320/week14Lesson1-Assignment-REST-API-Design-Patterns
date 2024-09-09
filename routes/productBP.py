from flask import Blueprint

from controllers.productController import save, find_all, search_product, find_by_id, update, delete

product_blueprint = Blueprint("product_bp", __name__)

#where we put our url_endpoints
product_blueprint.route('/', methods=['POST'])(save) # add new
product_blueprint.route('/', methods=['GET'])(find_all)
product_blueprint.route('/search', methods=['GET'])(search_product)
product_blueprint.route('/<int:product_id>', methods=['GET'])(find_by_id)
product_blueprint.route('/<int:product_id>', methods=['PUT'])(update)
product_blueprint.route('/<int:product_id>', methods=['DELETE'])(delete)
