import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from typing import List

from ..general_dao import GeneralDAO
from ...domain import Delivery


class DeliveryDAO(GeneralDAO):

    _domain_type = Delivery

    def find_by_term(self, term: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Delivery.term == term).all()

    def find_by_location_id(self, location_id: int) -> List[object]:
        return self._session.query(self._domain_type).filter(Delivery.location_id == location_id).all()
    
    def get_orders_in_delivery(self, delivery_id): 
        try: 
 
            delivery = self.find_by_id(delivery_id) 
 
            if not delivery: 
                return None 
 
            orders_in_delivery = delivery.orders 
 
            result = [] 
 
            for orders in orders_in_delivery: 
                result.append({ 
                    "id": orders.id, 
                    "order_date": orders.order_date,
                    "order_status": orders.order_status,
                    "delivery_cost": orders.delivery_cost,   
                }) 
 
            return result 
        except Exception as e: 
            print(f"Error: {e}") 
            return None