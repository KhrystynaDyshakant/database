import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from typing import List

from ...dao import stores_dao
from ...domain import Stores
from ..general_service import GeneralService


class StoresService(GeneralService):

    _dao = stores_dao

    def find_by_name(self, name: str) -> List[Stores]:

        objects = self._dao.find_by_name(name)
        return objects


    def find_by_address(self, address: str) -> List[Stores]:
        
        objects = self._dao.find_by_address(address)
        return objects