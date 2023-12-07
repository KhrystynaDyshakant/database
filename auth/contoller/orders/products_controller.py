import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import products_service
from ...domain import Products
from ..general_controller import GeneralController
from ...domain import Orders


class ProductsController(GeneralController):
 
    _service = products_service

    def find_by_name(self, product_name: str) -> List[Products]:

        objects = self._service.find_by_name(product_name)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_description(self, description: str) -> List[Products]:

        objects = self._service.find_by_description(description)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def find_by_price(self, price: int) -> List[Products]:
   
        objects = self._service.find_by_price(price)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def find_by_position(self, position: str) -> List[Products]:

        objects = self._service.find_by_position(position)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_orders_by_product_id(self, key: int) -> object:
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        return obj.put_into_dto_orders()
    
    def find_stores_by_product_id(self, key: int) -> object:
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        return obj.put_into_dto_stores()
    
    def find_all_orders(self) -> List[object]:
        return list(map(lambda x: x.put_into_dto_orders(), self._service.find_all()))
    
    def find_all_stores(self) -> List[object]:
        return list(map(lambda x: x.put_into_dto_stores(), self._service.find_all()))