from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey


import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from sqlalchemy.orm import relationship
from .... import db
from ..i_dto import IDto
from sqlalchemy import Table, Column, Integer, ForeignKey

# Define the association table
orders_has_products= db.Table(
    'orders_has_products',
    db.Column('orders_id', db.Integer, db.ForeignKey('orders.id')),
    db.Column('products_id', db.Integer, db.ForeignKey('products.id')),
    extend_existing=True
)

class Products(db.Model, IDto):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    price = db.Column(db.Integer)
    position = db.Column(db.String(255))

    #  # Визначення відносин багато до багатьох з замовленнями
    # orders = relationship('Orders', secondary=orders_has_products, backref='products', lazy='dynamic')
    # # Додавання зворотньої посилання для легкості використання
    # orders_associations = relationship('OrdersHasProducts', backref='product', lazy='dynamic')
    # # Визначення зворотньої посилання для сторінки магазинів
    # stores_associations = relationship('StoresHasProducts', backref='product', lazy='dynamic')
    # Define the Many-to-Many relationship with Orders
    # orders_1 = db.relationship('Orders', secondary=orders_has_products, back_populates='products_1')
    # Add a direct relationship to Orders
    # orders_associations = db.relationship('OrdersHasProducts', back_populates='product')
    # orders = relationship('Orders', secondary='orders_has_products', back_populates='products')
    # Define the back-reference
    # stores_associations = db.relationship('StoresHasProducts', back_populates='product')


    def __repr__(self) -> str:
        return f"Products(id={self.id}, product_name='{self.product_name}', description='{self.description}', price='{self.price}', posistion='{self.position}')"

    def put_into_dto(self) -> Dict[str, Any]:
  
        return {
            "id": self.id,
            "product_name": self.product_name,
            "description": self.description,
            "price": self.price,
            "position": self.position
        }
    
    @staticmethod 
    def create_from_dto(products_dict: Dict[str, Any]): 
        return Products(**products_dict)