import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import customers_service
from ...domain import Customers
from ..general_controller import GeneralController


class CustomersController(GeneralController):

    _service = customers_service

    def find_by_name(self, name: str) -> List[Customers]:
      
        objects = self._service.find_by_name(name)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_adress(self, adress: str) -> List[Customers]:
      
        objects = self._service.find_by_adress(adress)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def find_by_email(self, email: str) -> List[Customers]:
    
        objects = self._service.find_by_email(email)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def get_orders_in_customers(self, customers_id): 
        return customers_service.get_orders_in_customers(customers_id)