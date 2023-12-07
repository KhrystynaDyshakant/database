from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from .... import db
from ..i_dto import IDto

class City(db.Model, IDto):

    __tablename__ = "city"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))

    locations = db.relationship('Location', backref='city')


    def __repr__(self) :
        return f"City(id='{self.id}', name='{self.name}')"

    def put_into_dto(self):
   
        return {
            "id": self.id,
            "name": self.name,
        }
    
    @staticmethod 
    def create_from_dto(dto_dict): 
        obj = City( 
            name=dto_dict.get("name"), 
        ) 
        return obj
