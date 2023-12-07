
from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey


from .... import db
from ..i_dto import IDto
from .products import stores_has_products

class Stores(db.Model, IDto):

    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)

     # Define the back-reference
    products_associations = db.relationship('Products', secondary=stores_has_products, backref='stores_products')

    def __repr__(self) -> str:
        return f"Stores(id={self.id}, name='{self.name}', address='{self.address}')"

    def put_into_dto_products(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "products": list(map(lambda a: a.put_into_dto(), self.products_associations))
        }

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }
    
    @staticmethod 
    def create_from_dto(stores_dict: Dict[str, Any]): 
        return Stores(**stores_dict)
