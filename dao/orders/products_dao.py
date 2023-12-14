import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")

from typing import List
import sqlalchemy
from ..general_dao import GeneralDAO
from ...domain import Products
from ...domain import Orders
from my_project import db
from ...domain import Products



class ProductsDAO(GeneralDAO):

    _domain_type = Products

    def find_by_name(self, product_name: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Products.product_name == product_name).all()

    def find_by_description(self, description: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Products.description == description).all()
    
    def find_by_price(self, price: int) -> List[object]:
        return self._session.query(self._domain_type).filter(Products.price == price).all()
    
    def find_by_position(self, position: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Products.position == position).all()
    
    def insert_data(self):
        try:
            result = self._session.execute(sqlalchemy.text("CALL laba4.insert_products()"))
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None
    
    def make_operation(self, operation):
        try:
            result = self._session.execute(
                sqlalchemy.text("CALL laba4.make_operation_products(:p1)"),
                {"p1": operation}
            )

            # Fetch the result from the result set
            result_set = result.fetchall()

            # Close the result set
            result.close()

            # Commit the transaction
            self._session.commit()

            # Return the extracted data
            return result_set[0][0] if result_set else None

        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None