import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")
from typing import List

from ..general_dao import GeneralDAO
from ...domain import Location


class LocationDAO(GeneralDAO):

    _domain_type = Location

    def find_by_city_id(self, city_id: int) -> List[object]:
        return self._session.query(self._domain_type).filter(Location.city_id == city_id).all()

    def find_by_street_id(self, street_id: int) -> List[object]:
        return self._session.query(self._domain_type).filter(Location.street_id == street_id).all()
    
    def get_deliverys_in_location(self, location_id): 
        try: 
 
            location = self.find_by_id(location_id) 
 
            if not location: 
                return None 
 
            deliverys_in_location = location.deliverys 
 
            result = [] 
 
            for delivery in deliverys_in_location: 
                result.append({ 
                    "id": delivery.id, 
                    "term": delivery.term, 
                }) 
 
            return result 
        except Exception as e: 
            print(f"Error: {e}") 
            return None