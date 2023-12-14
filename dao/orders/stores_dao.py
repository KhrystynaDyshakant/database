import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")
from typing import List
import sqlalchemy

from ..general_dao import GeneralDAO
from ...domain import Stores


class StoresDAO(GeneralDAO):

    _domain_type = Stores

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Stores.name == name).all()

    def find_by_address(self, address: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Stores.address == address).all()
    
    def procedure_insert_stores(self, name, address):
        try:
            result = self._session.execute(sqlalchemy.text("CALL laba4.insert_stores(:p1, :p2)"),
                                           {"p1": name, "p2": address})
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None
        

    def insert_stores_and_products_dependency(self, name_, product_name_):
        try:
            result = self._session.execute(
                sqlalchemy.text("CALL laba4.insert_stores_and_products_dependency(:p1, :p2)"),
                {"p1": name_, "p2": product_name_})
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None