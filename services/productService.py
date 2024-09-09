# services/productService.py

from database import db
from models.product import Product
from sqlalchemy import select

def save(product_data):
    new_product = Product(
        product_name=product_data['product_name'],
        price=product_data['price']
    )
    db.session.add(new_product)
    db.session.commit()
    db.session.refresh(new_product)
    return new_product

def find_all():
    query = select(Product)
    all_products = db.session.execute(query).scalars().all()
    return all_products

def find_by_id(product_id):
    return db.session.get(Product, product_id)

def update(product_id, product_data):
    product = db.session.get(Product, product_id)
    if not product:
        return None

    product.product_name = product_data.get('product_name', product.product_name)
    product.price = product_data.get('price', product.price)

    db.session.commit()
    db.session.refresh(product)
    return product

def delete(product_id):
    product = db.session.get(Product, product_id)
    if not product:
        return None

    db.session.delete(product)
    db.session.commit()
    return product
