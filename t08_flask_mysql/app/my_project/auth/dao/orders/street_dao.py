import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from typing import List

from ..general_dao import GeneralDAO
from ...domain import Street


class StreetDAO(GeneralDAO):

    _domain_type = Street

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Street.name == name).all()

    def find_by_number_street(self, number_street: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Street.number_street == number_street).all()
    
    def get_locations_in_street(self, street_id): 
        try: 
 
            street = self.find_by_id(street_id) 
 
            if not street: 
                return None 
 
            locations_in_street = street.locations 
 
            result = [] 
 
            for location in locations_in_street: 
                result.append({ 
                    "id": location.id, 
                    "city_id": location.city_id, 
                }) 
 
            return result 
        except Exception as e: 
            print(f"Error: {e}") 
            return None