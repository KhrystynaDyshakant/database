# orders DB
from .orders.stores_dao import StoresDAO
from .orders.products_dao import ProductsDAO
# from.orders.stores_has_products_dao import StoresHasProductsDAO
from.orders.customers_dao import CustomersDAO
from.orders.orders_dao import OrdersDAO
from.orders.city_dao import CityDAO
from.orders.street_dao import StreetDAO
from.orders.location_dao import LocationDAO
from.orders.delivery_dao import DeliveryDAO
# from.orders.orders_has_products_dao import OrdersHasProductsDAO

stores_dao = StoresDAO()
products_dao = ProductsDAO()
# stores_has_products_dao = StoresHasProductsDAO()
customers_dao = CustomersDAO()
orders_dao = OrdersDAO()
city_dao = CityDAO()
street_dao = StreetDAO()
location_dao = LocationDAO()
delivery_dao = DeliveryDAO()
# orders_has_products_dao = OrdersHasProductsDAO()