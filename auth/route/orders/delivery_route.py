import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...contoller import delivery_controller
from ...domain import Delivery

delivery_bp = Blueprint('delivery', __name__, url_prefix='/delivery')


@delivery_bp.get('')
def get_all_delivery() -> Response:
  
    return make_response(jsonify(delivery_controller.find_all()), HTTPStatus.OK)


@delivery_bp.post('')
def create_delivery() -> Response:
   
    content = request.get_json()
    delivery = Delivery.create_from_dto(content)
    delivery_controller.create(delivery)
    return make_response(jsonify(delivery.put_into_dto()), HTTPStatus.CREATED)


@delivery_bp.get('/id/<int:delivery_id>')
def get_delivery(delivery_id: int) -> Response:
    
    return make_response(jsonify(delivery_controller.find_by_id(delivery_id)), HTTPStatus.OK)

@delivery_bp.get('/get_orders/<int:delivery_id>') 
def get_orders(delivery_id): 
    return make_response(jsonify(delivery_controller.get_orders_in_delivery(delivery_id)))


@delivery_bp.get('/term/<string:delivery_term>')
def get_delivery_by_term(delivery_term: str) -> Response:
  
    return make_response(jsonify(delivery_controller.find_by_term(delivery_term)), HTTPStatus.OK)


@delivery_bp.get('/location_id/<int:delivery_location_id>')
def get_delivery_by_location_id(delivery_location_id: int) -> Response:
   
    return make_response(jsonify(delivery_controller.find_by_location_id(delivery_location_id)), HTTPStatus.OK)


@delivery_bp.put('/<int:delivery_id>')
def update_delivery(delivery_id: int) -> Response:
   
    content = request.get_json()
    delivery = Delivery.create_from_dto(content)
    delivery_controller.update(delivery_id, delivery)
    return make_response("Delivery updated", HTTPStatus.OK)


@delivery_bp.patch('/<int:delivery_id>')
def patch_delivery(delivery_id: int) -> Response:
    
    content = request.get_json()
    delivery_controller.patch(delivery_id, content)
    return make_response("Delivery updated", HTTPStatus.OK)


@delivery_bp.delete('/<int:delivery_id>')
def delete_delivery(delivery_id: int) -> Response:
    
    delivery_controller.delete(delivery_id)
    return make_response("Delivery deleted", HTTPStatus.OK)