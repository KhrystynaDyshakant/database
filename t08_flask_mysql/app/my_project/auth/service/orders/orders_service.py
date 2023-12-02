import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from typing import List
import datetime

from ...dao import orders_dao
from ...domain import Orders
from ..general_service import GeneralService
from ...domain import Products


class OrdersService(GeneralService):
   
    _dao = orders_dao

    def find_by_order_date(self, order_date: str) -> List[Orders]:
     
        objects = self._dao.find_by_order_date(order_date)
        return objects


    def find_by_order_status(self, order_status: str) -> List[Orders]:
  
        objects = self._dao.find_by_order_status(order_status)
        return objects
    

    def find_by_delivery_cost(self, delivery_cost: int) -> List[Orders]:

        objects = self._dao.find_by_delivery_cost(delivery_cost)
        return objects
    

    def find_by_delivery_id(self, delivery_id: int) -> List[Orders]:

        objects = self._dao.find_by_delivery_id(delivery_id)
        return objects
    
    
    def find_by_customer_id(self, customer_id: int) -> List[Orders]:

        objects = self._dao.find_by_customer_id(customer_id)
        return objects
    
    def find_products_by_order_id(self, orders_id: int) -> List[Products]:
        objects = self._dao.find_products_by_order_id(orders_id)
        return objects