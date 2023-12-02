import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from typing import List

from ..general_dao import GeneralDAO
from ...domain import Orders
from ...domain import Products



class OrdersDAO(GeneralDAO):
   
    _domain_type = Orders

    def find_by_order_date(self, order_date: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Orders.order_date == order_date).all()

    def find_by_order_status(self, order_status: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Orders.order_status == order_status).all()
    
    def find_by_delivery_cost(self, delivery_cost: int) -> List[object]:
        return self._session.query(self._domain_type).filter(Orders.delivery_cost == delivery_cost).all()
    
    def find_by_delivery_id(self, delivery_id: int) -> List[object]:
        return self._session.query(self._domain_type).filter(Orders.delivery_id == delivery_id).all()
    
    def find_by_customer_id(self, customer_id: int) -> List[object]:
        return self._session.query(self._domain_type).filter(Orders.customer_id == customer_id).all()
  