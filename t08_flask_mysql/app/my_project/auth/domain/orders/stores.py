
from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey


import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from sqlalchemy.orm import relationship
from .... import db
from ..i_dto import IDto

class Stores(db.Model, IDto):

    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)

     # Define the back-reference
    # products_associations = relationship('StoresHasProducts', back_populates='store')
 
    def __repr__(self) -> str:
        return f"Stores(id={self.id}, name='{self.name}', address='{self.address}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }
    
    @staticmethod 
    def create_from_dto(stores_dict: Dict[str, Any]): 
        return Stores(**stores_dict)
