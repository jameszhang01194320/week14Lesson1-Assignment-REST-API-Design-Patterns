from flask import request, jsonify 
from models.schemas.productSchema import product_schema, products_schema
from marshmallow import ValidationError
from services import productService
<<<<<<< HEAD
=======
from cache import cache
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f

def save():
    try: 
        product_data = product_schema.load(request.json) #unpack/deserializing (load) and validate (product_schema) incoming request data
    except ValidationError as e:
        return jsonify(e.messages), 400 #sending error message and error status code
    
    new_product = productService.save(product_data) #calling my service

    return product_schema.jsonify(new_product), 201 

<<<<<<< HEAD

def find_all():
    page = request.args.get("page")
    per_page = request.args.get("per_page")
    page = 1 if not page else page
    per_page = 10 if not per_page else per_page
    all_products = productService.find_all(page, per_page)
=======
@cache.cached(timeout=120)
def find_all():
    all_products = productService.find_all()
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
    return products_schema.jsonify(all_products), 200

def search_product():
    search_term = request.args.get("search")
<<<<<<< HEAD
    page = request.args.get("page")
    per_page = request.args.get("per_page")

    page = 1 if not page else page
    per_page = 10 if not per_page else per_page

    if search_term:
        search_products = productService.search_product(search_term, page, per_page)
        if "message" in search_products:
            return jsonify(
                search_products), 200
        return products_schema.jsonify(search_products), 200
    else:
        return jsonify({"message": "Please provide a search term"}), 400
=======
    search_products = productService.search_product(search_term)
    return products_schema.jsonify(search_products), 200

def find_by_id(product_id):
    product = productService.find_by_id(product_id)
    if product:
        return product_schema.jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404

def update(product_id):
    product = productService.find_by_id(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    updated_product = productService.update(product_id, product_data)
    return product_schema.jsonify(updated_product), 200

def delete(product_id):
    product = productService.delete(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify({"message": "Product deleted successfully"}), 200
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
