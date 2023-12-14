from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")
from sqlalchemy.orm import relationship
from .... import db
from ..i_dto import IDto

class Street(db.Model, IDto):

    __tablename__ = "street"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    number_street = db.Column(db.String(45))

    locations = db.relationship('Location', backref='street')
 
    def __repr__(self) :
        return f"Street(id={self.id}, name='{self.name}', number_street='{self.number_street}')"

    def put_into_dto(self):
        return {
            "id": self.id,
            "name": self.name,
            "number_street": self.number_street
        }
    
    @staticmethod 
    def create_from_dto(dto_dict): 
        obj = Street( 
            name=dto_dict.get("name"),
            number_street=dto_dict.get("number_street"), 
        ) 
        return obj
