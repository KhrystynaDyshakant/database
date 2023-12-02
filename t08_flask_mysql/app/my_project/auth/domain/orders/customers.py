from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from .... import db
from ..i_dto import IDto

class Customers(db.Model, IDto):
 
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    adress = db.Column(db.String(255))
    email = db.Column(db.String(255))

    orders = db.relationship('Orders', backref='customers')


    def __repr__(self) :
        return f"Customers(id={self.id}, name='{self.name}', adress='{self.adress}', email='{self.email}')"

    def put_into_dto(self) :

        return {
            "id": self.id,
            "name": self.name,
            "adress": self.adress,
            "email": self.email
        }
    
    @staticmethod 
    def create_from_dto(dto_dict): 
        obj = Customers( 
            name=dto_dict.get("name"),
            adress=dto_dict.get("adress"), 
            email=dto_dict.get("email"), 
        ) 
        return obj