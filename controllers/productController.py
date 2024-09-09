from flask import request, jsonify 
from models.schemas.productSchema import product_schema, products_schema
from marshmallow import ValidationError
from services import productService
from cache import cache

def save():
    try: 
        product_data = product_schema.load(request.json) #unpack/deserializing (load) and validate (product_schema) incoming request data
    except ValidationError as e:
        return jsonify(e.messages), 400 #sending error message and error status code
    
    new_product = productService.save(product_data) #calling my service

    return product_schema.jsonify(new_product), 201 

@cache.cached(timeout=120)
def find_all():
    all_products = productService.find_all()
    return products_schema.jsonify(all_products), 200

def search_product():
    search_term = request.args.get("search")
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