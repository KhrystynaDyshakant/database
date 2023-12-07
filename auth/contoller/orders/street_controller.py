import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import street_service
from ...domain import Street
from ..general_controller import GeneralController


class StreetController(GeneralController):

    _service = street_service

    def find_by_name(self, name: str) -> List[Street]:
      
        objects = self._service.find_by_name(name)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def find_by_number_street(self, number_street: str) -> List[Street]:
      
        objects = self._service.find_by_number_street(number_street)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def get_locations_in_street(self, street_id): 
        return street_service.get_locations_in_street(street_id)