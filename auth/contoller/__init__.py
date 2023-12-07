from .orders.stores_controller import StoresController
from .orders.products_controller import ProductsController
# from.orders.stores_has_products_contoller import StoresHasProductsController
from.orders.customers_controller import CustomersController
from.orders.orders_controller import OrdersController
# from.orders.orders_has_products_controller import OrdersHasProductsController
from.orders.city_controller import CityController
from.orders.street_controller import StreetController
from.orders.location_controller import LocationController
from.orders.delivery_controller import DeliveryController


stores_controller = StoresController()
products_controller = ProductsController()
# stores_has_products_controller = StoresHasProductsController()
customers_controller = CustomersController()
orders_controller = OrdersController()
# orders_has_products_controller = OrdersHasProductsController()
city_controller = CityController()
street_controller = StreetController()
location_controller = LocationController()
delivery_controller =  DeliveryController()