import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")
from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import stores_service
from ...domain import Stores
from ..general_controller import GeneralController


class StoresController(GeneralController):

    _service = stores_service

    def find_by_name(self, name: str) -> List[Stores]:

        objects = self._service.find_by_name(name)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_address(self, address: str) -> List[Stores]:

        objects = self._service.find_by_address(address)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def find_products_by_stores_id(self, key: int) -> object:
        obj: Stores = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        return obj.put_into_dto_products()
    
    def find_all_products(self) -> List[object]:
        return list(map(lambda x: x.put_into_dto_products(), self._service.find_all()))
    

    def procedure_insert_stores(self, name, address):
        return self._service.insert_stores(name, address)
    
    def insert_stores_and_products_dependency(self, name_, product_name_):
        return self._service.insert_stores_and_products_dependency(name_, product_name_)
