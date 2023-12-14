import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")

from typing import List
import sqlalchemy
from ..general_dao import GeneralDAO
from ...domain import Customers


class CustomersDAO(GeneralDAO):
 
    _domain_type = Customers

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Customers.name == name).all()

    def find_by_adress(self, adress: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Customers.adress == adress).all()
    
    def find_by_email(self, email: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Customers.email == email).all()
    
    def get_orders_in_customers(self, customers_id): 
        try: 
 
            customers = self.find_by_id(customers_id) 
 
            if not customers: 
                return None 
 
            orders_in_customers = customers.orders 
 
            result = [] 
 
            for orders in orders_in_customers: 
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
        

    def create_tables_for_cursor(self):
        result = self._session.execute(sqlalchemy.text("CALL laba4.create_tables_for_cursor()"))
        self._session.commit()
        return result.mappings()