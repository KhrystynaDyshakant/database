import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from typing import List

from ...dao import products_dao
from ...domain import Products
from ..general_service import GeneralService
from ...domain import Orders


class ProductsService(GeneralService):

    _dao = products_dao

    def find_by_name(self, product_name: str) -> List[Products]:

        objects = self._dao.find_by_name(product_name)
        return objects


    def find_by_description(self, description: str) -> List[Products]:

        objects = self._dao.find_by_description(description)
        return objects
    

    def find_by_price(self, price: int) -> List[Products]:

        objects = self._dao.find_by_price(price)
        return objects
    

    def find_by_position(self, position: str) -> List[Products]:
 
        objects = self._dao.find_by_position(position)
        return objects
    
    def find_orders_by_product_id(self, products_id: int) -> List[Orders]:
        objects = self._dao.find_orders_by_product_id(products_id)
        return objects