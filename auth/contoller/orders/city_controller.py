import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import city_service
from ...domain import City
from ..general_controller import GeneralController


class CityController(GeneralController):
   
    _service = city_service

    def find_by_name(self, name: str) -> List[City]:
      
        objects = self._service.find_by_name(name)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
    
    def get_locations_in_city(self, city_id): 
        return city_service.get_locations_in_city(city_id)
