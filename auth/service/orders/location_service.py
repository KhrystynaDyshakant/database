import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from typing import List

from ...dao import location_dao
from ...domain import Location
from ..general_service import GeneralService


class LocationService(GeneralService):

    _dao = location_dao

    def find_by_city_id(self, city_id: int) -> List[Location]:

        objects = self._dao.find_by_city_id(city_id)
        return objects

    def find_by_street_id(self, street_id: int) -> List[Location]:
        
        objects = self._dao.find_by_street_id(street_id)
        return objects
    
    def get_deliverys_in_location(self, location_id): 
        return location_dao.get_deliverys_in_location(location_id)