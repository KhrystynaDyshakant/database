import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import delivery_service
from ...domain import Delivery
from ..general_controller import GeneralController


class DeliveryController(GeneralController):

    _service = delivery_service

    def find_by_term(self, term: str) -> List[Delivery]:
      
        objects = self._service.find_by_term(term)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def find_by_location_id(self, location_id: int) -> List[Delivery]:
      
        objects = self._service.find_by_location_id(location_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def get_orders_in_delivery(self, delivery_id): 
        return delivery_service.get_orders_in_delivery(delivery_id)
