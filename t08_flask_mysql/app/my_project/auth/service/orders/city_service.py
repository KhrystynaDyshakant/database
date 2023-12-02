import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from typing import List

from ...dao import city_dao
from ...domain import City
from ..general_service import GeneralService

class CityService(GeneralService):
  
    _dao = city_dao

    def find_by_name(self, name: str) -> List[City]:
    
        objects = self._dao.find_by_name(name)
        return objects
    
    def get_locations_in_city(self, city_id): 
        return city_dao.get_locations_in_city(city_id)