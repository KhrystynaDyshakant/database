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
