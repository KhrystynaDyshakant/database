# Import here Domain Class that are needed for ORM
# orders DB
from .orders.stores import Stores
from .orders.products import Products
# from.orders.stores_has_products import StoresHasProducts
from.orders.customers import Customers
from.orders.orders import Orders
from.orders.city import City
from.orders.street import Street
from.orders.location import Location
from.orders.delivery import Delivery
#from.orders.orders_has_products import OrdersHasProducts

stores = Stores()
products = Products()
customers = Customers()
orders = Orders()
city = City()
street = Street()
location = Location()
delivery = Delivery()
# stores_has_products = StoresHasProducts()
#orders_has_products = OrdersHasProducts()