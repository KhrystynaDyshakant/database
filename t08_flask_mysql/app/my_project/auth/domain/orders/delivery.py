
from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from .... import db
from ..i_dto import IDto

class Delivery(db.Model, IDto):

    __tablename__ = "delivery"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    term = db.Column(db.String(45))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))

    orders = db.relationship('Orders', backref='delivery')
 
    def __repr__(self) :
        return f"Delivery(id={self.id}, location_id='{self.location_id}', term='{self.term}')"

    def put_into_dto(self) :
        return {
            "id": self.id,
            "location_id": self.location_id,
            "term": self.term
        }
    
    @staticmethod 
    def create_from_dto(dto_dict): 
        obj = Delivery( 
            location_id=dto_dict.get("location_id"),
            term=dto_dict.get("term"), 
        ) 
        return obj
