from database import db #services interact directly with the db
from models.customer import Customer #need this to create customer objects
<<<<<<< HEAD
from sqlalchemy import select#so we can query our db

def save(customer_data):

    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'], username=customer_data['username'], password=customer_data['password'], admin=customer_data['admin'])
=======
from sqlalchemy import select #so we can query our db


def save(customer_data):

    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'], username=customer_data['username'], password=customer_data['password'])
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
    db.session.add(new_customer)
    db.session.commit() #adding our new customer to our db
    print("Commited new product to our db")
    db.session.refresh(new_customer)
    return new_customer


<<<<<<< HEAD
def find_all(page=1, per_page=10):
    query = select(Customer)
    all_customers = db.paginate(query, page=int(page), per_page=int(per_page)) #our paginated query is dependant on a page number and how many we wish to show per page

    return all_customers

=======
def find_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()

    return all_customers


def find_by_id(customer_id):
    customer = db.session.get(Customer, customer_id)
    return customer


def update(customer_id, customer_data):
    customer = db.session.get(Customer, customer_id)
    if not customer:
        return None  # non-existent, None

    customer.name = customer_data['name']
    customer.email = customer_data['email']
    customer.phone = customer_data['phone']
    customer.username = customer_data['username']
    customer.password = customer_data['password']

    db.session.commit()
    db.session.refresh(customer)
    return customer


def delete(customer_id):
    customer = db.session.get(Customer, customer_id)
    if not customer:
        return None  # non-existent

    db.session.delete(customer)
    db.session.commit()
    return customer  # return deleted












>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
