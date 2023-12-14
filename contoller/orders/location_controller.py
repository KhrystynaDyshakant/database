import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")
from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import location_service
from ...domain import Location
from ..general_controller import GeneralController


class LocationController(GeneralController):

    _service = location_service

    def find_by_city_id(self, city_id: int) -> List[Location]:
      
        objects = self._service.find_by_city_id(city_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def find_by_street_id(self, street_id: int) -> List[Location]:
      
        objects = self._service.find_by_street_id(street_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def get_deliverys_in_location(self, location_id): 
        return location_service.get_deliverys_in_location(location_id)