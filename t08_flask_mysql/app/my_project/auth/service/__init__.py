from flask import Flask

from .orders.stores_service import StoresService
from .orders.products_service import ProductsService
# from.orders.stores_has_products_service import StoresHasProductsService
from.orders.customer_service import CustomersService
from.orders.orders_service import OrdersService
from.orders.city_service import CityService
from.orders.street_service import StreetService
from.orders.location_service import LocationService
from.orders.delivery_service import DeliveryService
# from.orders.orders_has_products_service import OrdersHasProductsService

stores_service = StoresService()
products_service = ProductsService()
# stores_has_products_service = StoresHasProductsService()
customers_service = CustomersService()
orders_service = OrdersService()
city_service = CityService()
street_service = StreetService()
location_service = LocationService()
delivery_service = DeliveryService()
# orders_has_products_service = OrdersHasProductsService()
