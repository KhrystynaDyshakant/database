# orders DB
from .orders.stores_dao import StoresDAO
from .orders.products_dao import ProductsDAO
from.orders.customers_dao import CustomersDAO
from.orders.orders_dao import OrdersDAO
from.orders.city_dao import CityDAO
from.orders.street_dao import StreetDAO
from.orders.location_dao import LocationDAO
from.orders.delivery_dao import DeliveryDAO


stores_dao = StoresDAO()
products_dao = ProductsDAO()
customers_dao = CustomersDAO()
orders_dao = OrdersDAO()
city_dao = CityDAO()
street_dao = StreetDAO()
location_dao = LocationDAO()
delivery_dao = DeliveryDAO()
