from database import db
from models.order import Order
from models.product import Product
from sqlalchemy import select
from datetime import date #need to get todays date for the order

def save(order_data):

    new_order = Order(customer_id=order_data['customer_id'], date=date.today()) #date.today() will generate todays date and store it in the date catagory

    for item_id in order_data['product_ids']:
        query = select(Product).where(Product.id==item_id) #search the product table for a product whose id is the same as the item_id we are looping over
        item = db.session.execute(query).scalar()
        new_order.products.append(item) #creates the connection from Order to the associate id, and populates our order_product table

    db.session.add(new_order)
    db.session.commit()

    db.session.refresh(new_order)
    return new_order

def find_all():
    query = select(Order)
    all_orders = db.session.execute(query).scalars().all()

    return all_orders

# Function to find an order by its ID
def find_by_id(order_id):
    return db.session.get(Order, order_id)

# Function to update an existing order
def update_order(order_id, order_data):
    order = db.session.get(Order, order_id)
    if not order:
        return None

    # Update order details (e.g., order_date, products)
    order.order_date = order_data.get('order_date', order.order_date)

    # Update products if provided
    if 'product_ids' in order_data:
        order.products.clear()  # Clear existing products
        products = db.session.execute(select(Product).filter(Product.id.in_(order_data['product_ids']))).scalars().all()
        order.products.extend(products)

    db.session.commit()
    db.session.refresh(order)
    return order

# Function to delete an order by its ID
def delete_order(order_id):
    order = db.session.get(Order, order_id)
    if not order:
        return None

    db.session.delete(order)
    db.session.commit()
    return order
