from .orders.stores_controller import StoresController
from .orders.products_controller import ProductsController
from.orders.customers_controller import CustomersController
from.orders.orders_controller import OrdersController
from.orders.city_controller import CityController
from.orders.street_controller import StreetController
from.orders.location_controller import LocationController
from.orders.delivery_controller import DeliveryController



stores_controller = StoresController()
products_controller = ProductsController()
customers_controller = CustomersController()
orders_controller = OrdersController()
city_controller = CityController()
street_controller = StreetController()
location_controller = LocationController()
delivery_controller =  DeliveryController()
