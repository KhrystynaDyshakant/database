import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from typing import List

from ...dao import delivery_dao
from ...domain import Delivery
from ..general_service import GeneralService


class DeliveryService(GeneralService):

    _dao = delivery_dao

    def find_by_term(self, term: str) -> List[Delivery]:

        objects = self._dao.find_by_term(term)
        return objects

    def find_by_location_id(self, location_id: int) -> List[Delivery]:
        
        objects = self._dao.find_by_location_id(location_id)
        return objects
    
    def get_orders_in_delivery(self, delivery_id): 
        return delivery_dao.get_orders_in_delivery(delivery_id)