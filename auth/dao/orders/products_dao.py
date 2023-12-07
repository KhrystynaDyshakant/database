import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from typing import List

from ..general_dao import GeneralDAO
from ...domain import Products
from ...domain import Orders
from my_project import db
from ...domain import Products



class ProductsDAO(GeneralDAO):

    _domain_type = Products

    def find_by_name(self, product_name: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Products.product_name == product_name).all()

    def find_by_description(self, description: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Products.description == description).all()
    
    def find_by_price(self, price: int) -> List[object]:
        return self._session.query(self._domain_type).filter(Products.price == price).all()
    
    def find_by_position(self, position: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Products.position == position).all()
    