import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
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
