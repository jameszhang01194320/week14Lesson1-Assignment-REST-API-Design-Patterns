<<<<<<< HEAD
=======
# services/productService.py

>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
from database import db
from models.product import Product
from sqlalchemy import select

<<<<<<< HEAD

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
=======
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
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
