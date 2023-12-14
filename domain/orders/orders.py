from __future__ import annotations
from typing import Dict, Any

import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")
from sqlalchemy.orm import relationship
from .... import db
from ..i_dto import IDto
from sqlalchemy import Table, Column, Integer, ForeignKey
from .products import orders_has_products

class Orders(db.Model, IDto):

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_date = db.Column(db.Date)
    order_status = db.Column(db.String(255))
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    delivery_cost = db.Column(db.Integer)

    products = db.relationship('Products', secondary=orders_has_products, backref='orders_products')
    
    def __repr__(self) -> str:
        return f"Orders( id={self.id}, order_date='{self.order_date}', order_status'{self.order_status}', delivery_id='{self.delivery_id}', customer_id='{self.customer_id}', delivery_cost='{self.delivery_cost}')"

    def put_into_dto_products(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "order_date": str(self.order_date),
            "order_status": self.order_status,
            "delivery_id": self.delivery_id,
            "customer_id": self.customer_id,
            "delivery_cost": self.delivery_cost,
            "orders_delivery": self.delivery.put_into_dto(), 
            "orders_customer": self.customers.put_into_dto(),
            "products": list(map(lambda a: a.put_into_dto(), self.products))
        }

    def put_into_dto(self) -> Dict[str, Any]:
        print(self.products)
        return {
            "id": self.id,
            "order_date": str(self.order_date),
            "order_status": self.order_status,
            "delivery_id": self.delivery_id,
            "customer_id": self.customer_id,
            "delivery_cost": self.delivery_cost,
            "delivery": self.delivery.put_into_dto()['location'],
            
        }
    
    @staticmethod 
    def create_from_dto(orders_dict: Dict[str, Any]): 
        return Orders(**orders_dict)