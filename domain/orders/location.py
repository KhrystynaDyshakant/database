from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")
from sqlalchemy.orm import relationship
from .... import db
from ..i_dto import IDto

class Location(db.Model, IDto):

    __tablename__ = "location"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    street_id = db.Column(db.Integer, db.ForeignKey('street.id'))

    deliverys = db.relationship('Delivery', backref='location')


    def __repr__(self):
        return f"Location(id={self.id}, city_id='{self.city_id}', street_id'{self.street_id}')"

    def put_into_dto(self):
   
        return {
            "id": self.id,
            "location_in_city": self.city.put_into_dto(), 
            "location_in_street": self.street.put_into_dto(), 
        }
    
    @staticmethod 
    def create_from_dto(dto_dict): 
        obj = Location( 
            city_id=dto_dict.get("city_id"), 
            street_id=dto_dict.get("street_id"), 
        ) 
        return obj