import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from typing import List

from ...dao import street_dao
from ...domain import Street
from ..general_service import GeneralService


class StreetService(GeneralService):

    _dao = street_dao

    def find_by_name(self, name: str) -> List[Street]:

        objects = self._dao.find_by_name(name)
        return objects


    def find_by_number_street(self, number_street: str) -> List[Street]:
        
        objects = self._dao.find_by_number_street(number_street)
        return objects
    
    def get_locations_in_street(self, street_id): 
        return street_dao.get_locations_in_street(street_id)