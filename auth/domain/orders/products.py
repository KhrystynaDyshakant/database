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
    db.Column('orders_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
    db.Column('products_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    extend_existing=True
)

stores_has_products= db.Table(
    'stores_has_products',
    db.Column('stores_id', db.Integer, db.ForeignKey('stores.id'), primary_key=True),
    db.Column('products_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
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
    orders = db.relationship('Orders', secondary=orders_has_products, backref='products_orders')
    stores = db.relationship('Stores', secondary=stores_has_products, backref='products_stores')

    def __repr__(self) -> str:
        return f"Products(id={self.id}, product_name='{self.product_name}', description='{self.description}', price='{self.price}', posistion='{self.position}')"

    def put_into_dto_orders(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "product_name": self.product_name,
            "description": self.description,
            "price": self.price,
            "position": self.position,
            "orders": list(map(lambda a: a.put_into_dto(), self.orders))
        }

    def put_into_dto_stores(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "product_name": self.product_name,
            "description": self.description,
            "price": self.price,
            "position": self.position,
            "stores": list(map(lambda a: a.put_into_dto(), self.stores))
        }

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