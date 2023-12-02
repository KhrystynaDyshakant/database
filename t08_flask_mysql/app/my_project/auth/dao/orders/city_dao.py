import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from typing import List

from ..general_dao import GeneralDAO
from ...domain import City


class CityDAO(GeneralDAO):
   
    _domain_type = City

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(self._domain_type).filter(City.name == name).all()
    
    def get_locations_in_city(self, city_id): 
        try: 
 
            city = self.find_by_id(city_id) 
 
            if not city: 
                return None 
 
            locations_in_city = city.locations 
 
            result = [] 
 
            for location in locations_in_city: 
                result.append({ 
                    "id": location.id, 
                    "street_id": location.street_id, 
                }) 
 
            return result 
        except Exception as e: 
            print(f"Error: {e}") 
            return None