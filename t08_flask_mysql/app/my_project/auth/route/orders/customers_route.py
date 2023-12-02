import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...contoller import customers_controller
from ...domain import Customers

customers_bp = Blueprint('customers', __name__, url_prefix='/customers')


@customers_bp.get('')
def get_all_customers() -> Response:

    return make_response(jsonify(customers_controller.find_all()), HTTPStatus.OK)


@customers_bp.post('')
def create_customers() -> Response:
  
    content = request.get_json()
    customers = Customers.create_from_dto(content)
    customers_controller.create(customers)
    return make_response(jsonify(customers.put_into_dto()), HTTPStatus.CREATED)


@customers_bp.get('/id/<int:customers_id>')
def get_customers(customers_id: int) -> Response:

    return make_response(jsonify(customers_controller.find_by_id(customers_id)), HTTPStatus.OK)

@customers_bp.get('/get_orders/<int:customers_id>') 
def get_orders(customers_id): 
    return make_response(jsonify(customers_controller.get_orders_in_customers(customers_id)))


@customers_bp.get('/name/<string:customers_name>')
def get_customers_by_name(customers_name: str) -> Response:

    return make_response(jsonify(customers_controller.find_by_name(customers_name)), HTTPStatus.OK)


@customers_bp.get('/adress/<string:customers_adress>')
def get_customers_by_adress(customers_adress: str) -> Response:

    return make_response(jsonify(customers_controller.find_by_adress(customers_adress)), HTTPStatus.OK)


@customers_bp.get('/email/<string:customers_email>')
def get_customers_by_email(customers_email: str) -> Response:

    return make_response(jsonify(customers_controller.find_by_email(customers_email)), HTTPStatus.OK)


@customers_bp.put('/<int:customers_id>')
def update_customers(customers_id: int) -> Response:
  
    content = request.get_json()
    customers = Customers.create_from_dto(content)
    customers_controller.update(customers_id, customers)
    return make_response("Customers updated", HTTPStatus.OK)


@customers_bp.patch('/<int:customers_id>')
def patch_customers(customers_id: int) -> Response:
 
    content = request.get_json()
    customers_controller.patch(customers_id, content)
    return make_response("Customers updated", HTTPStatus.OK)


@customers_bp.delete('/<int:customers_id>')
def delete_customers(customers_id: int) -> Response:
 
    customers_controller.delete(customers_id)
    return make_response("Customers deleted", HTTPStatus.OK)