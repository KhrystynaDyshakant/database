import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from typing import List

from ..general_dao import GeneralDAO
from ...domain import Stores


class StoresDAO(GeneralDAO):

    _domain_type = Stores

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Stores.name == name).all()

    def find_by_address(self, address: str) -> List[object]:
        return self._session.query(self._domain_type).filter(Stores.address == address).all()