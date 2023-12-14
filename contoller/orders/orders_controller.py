import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")

from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import orders_service
from ...domain import Orders
from ..general_controller import GeneralController
from ...domain import Products


class OrdersController(GeneralController):
 
    _service = orders_service

    def find_by_order_date(self, order_date: str) -> List[Orders]:
  
        objects = self._service.find_by_order_date(order_date)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_order_status(self, order_status: str) -> List[Orders]:
    
        objects = self._service.find_by_order_status(order_status)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def find_by_delivery_cost(self, delivery_cost: int) -> List[Orders]:
       
        objects = self._service.find_by_delivery_cost(delivery_cost)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def find_by_delivery_id(self, delivery_id: int) -> List[Orders]:
       
        objects = self._service.find_by_delivery_id(delivery_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def find_by_customer_id(self, customer_id: int) -> List[Orders]:
       
        objects = self._service.find_by_customer_id(customer_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def find_products_by_order_id(self, key: int) -> List[Products]:
        obj: Orders = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        return obj.put_into_dto_products()
    
    def find_all_products(self) -> List[object]:
        return list(map(lambda x: x.put_into_dto_products(), self._service.find_all()))