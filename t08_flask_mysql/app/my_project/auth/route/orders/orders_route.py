import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...contoller import orders_controller
from ...domain import Orders
from ...dao import OrdersDAO
import datetime

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

@orders_bp.get('')
def get_all_orders() -> Response:

    return make_response(jsonify(orders_controller.find_all()), HTTPStatus.OK)


@orders_bp.post('')
def create_orders() -> Response:

    content = request.get_json()
    orders = Orders.create_from_dto(content)
    orders_controller.create(orders)
    return make_response(jsonify(orders.put_into_dto()), HTTPStatus.CREATED)


@orders_bp.get('/id/<int:orders_id>')
def get_orders(orders_id: int) -> Response:
 
    return make_response(jsonify(orders_controller.find_by_id(orders_id)), HTTPStatus.OK)

@orders_bp.route('/orders/<int:orders_id>/products')
def get_products_for_order(orders_id):
    products = OrdersDAO.get_products_for_order(orders_id)
    if products:
        return jsonify([product.put_into_dto() for product in products])
    return jsonify({"message": "Order not found"}), 404

# @orders_bp.get('/id/<int:orders_id>/products')
# def get_products_by_order_id(orders_id: int) -> Response:
#     return make_response(jsonify(orders_controller.find_products_by_order_id(orders_id)), HTTPStatus.OK)


@orders_bp.get('/order_date/<string:order_date>')
def get_orders_by_order_date(order_date: str) -> Response:

    return make_response(jsonify(orders_controller.find_by_order_date(order_date)), HTTPStatus.OK)


@orders_bp.get('/order_status/<string:order_status>')
def get_orders_by_order_status(order_status: str) -> Response:

    return make_response(jsonify(orders_controller.find_by_order_status(order_status)), HTTPStatus.OK)


@orders_bp.get('/delivery_cost/<int:delivery_cost>')
def get_orders_by_delivery_cost(delivery_cost: int) -> Response:

    return make_response(jsonify(orders_controller.find_by_delivery_cost(delivery_cost)), HTTPStatus.OK)


@orders_bp.get('/delivery_id/<int:delivery_id>')
def get_orders_by_delivery_id(delivery_id: int) -> Response:

    return make_response(jsonify(orders_controller.find_by_delivery_id(delivery_id)), HTTPStatus.OK)


@orders_bp.get('/customer_id/<int:customer_id>')
def get_orders_by_customer_id(customer_id: int) -> Response:
 
    return make_response(jsonify(orders_controller.find_by_customer_id(customer_id)), HTTPStatus.OK)


@orders_bp.put('/<int:orders_id>')
def update_orders(orders_id: int) -> Response:
 
    content = request.get_json()
    orders = Orders.create_from_dto(content)
    orders_controller.update(orders_id, orders)
    return make_response("Orders updated", HTTPStatus.OK)


@orders_bp.patch('/<int:orders_id>')
def patch_orders(orders_id: int) -> Response:

    content = request.get_json()
    orders_controller.patch(orders_id, content)
    return make_response("Orders updated", HTTPStatus.OK)


@orders_bp.delete('/<int:orders_id>')
def delete_orders(orders_id: int) -> Response:

    orders_controller.delete(orders_id)
    return make_response("Orders deleted", HTTPStatus.OK)