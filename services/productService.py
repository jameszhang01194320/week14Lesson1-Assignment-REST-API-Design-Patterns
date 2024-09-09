from database import db
from models.product import Product
from sqlalchemy import select


def save(product_data): #save controller will pass the service validated data

    new_product = Product(product_name=product_data['product_name'], price=product_data['price'])
    db.session.add(new_product)
    db.session.commit()

    db.session.refresh(new_product)
    return new_product #returning new product back to the controller


def find_all(page=1, per_page=10):
    query = select(Product)
    all_products = db.paginate(query, page=int(page), per_page=int(per_page))
    return all_products

def search_product(search_term, page=1, per_page=10):  # Adding pagination
    query = select(Product).where(Product.product_name.like(f'%{search_term}%'))
    search_products = db.paginate(query, page=int(page), per_page=int(per_page))
    return search_products
