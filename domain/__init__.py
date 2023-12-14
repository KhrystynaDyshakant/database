
# orders DB
from .orders.stores import Stores
from .orders.products import Products
from.orders.customers import Customers
from.orders.orders import Orders
from.orders.city import City
from.orders.street import Street
from.orders.location import Location
from.orders.delivery import Delivery
from.orders.orders_base import OrdersBase

stores = Stores()
products = Products()
customers = Customers()
orders = Orders()
city = City()
street = Street()
location = Location()
delivery = Delivery()
orders_base = OrdersBase()
