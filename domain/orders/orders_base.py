from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class OrdersBase(db.Model, IDto):
   
    __tablename__ = "orders_base"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    orders_id = db.Column(db.Integer,  nullable=False)
    amount: int = db.Column(db.Integer)
    



    def __repr__(self) -> str:
        return f"Orders Base({self.id}, {self.orders_id}, {self.amount})"

    def put_into_dto(self) -> Dict[str, Any]:
        
        return {
            "id": self.id,
            "orders_id": self.orders_id,
            "amount": self.amount,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> OrdersBase:
        
        obj = OrdersBase(
            orders_id=dto_dict.get("orders_id"),
            amount=dto_dict.get("amount")
        )
        return obj