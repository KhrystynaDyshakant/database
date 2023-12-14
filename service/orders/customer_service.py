import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")

from typing import List

from ...dao import customers_dao
from ...domain import Customers
from ..general_service import GeneralService


class CustomersService(GeneralService):
  
    _dao = customers_dao

    def find_by_name(self, name: str) -> List[Customers]:
        
        objects = self._dao.find_by_name(name)
        return objects

    def find_by_adress(self, adress: str) -> List[Customers]:

        objects = self._dao.find_by_adress(adress)
        return objects
    
    def find_by_email(self, email: str) -> List[Customers]:

        objects = self._dao.find_by_email(email)
        return objects
    
    def get_orders_in_customers(self, customers_id): 
        return customers_dao.get_orders_in_customers(customers_id)
    
    def create_tables_for_cursor(self):
        return self._dao.create_tables_for_cursor()