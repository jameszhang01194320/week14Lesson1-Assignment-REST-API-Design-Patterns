from typing import List
from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Customer(Base):
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(primary_key=True) #primary keys auto increment
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(db.String(25), nullable=False)
    username: Mapped[str] = mapped_column(db.String(30), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
<<<<<<< HEAD
    admin: Mapped[int] = mapped_column(db.Integer, nullable=False)
=======
>>>>>>> e53bbe57d456273431e47c43e69a6a86f6b3a18f
    #One-to-Many relationship: One customer can place many orders
    orders: Mapped[List['Order']] = db.relationship(back_populates='customer')