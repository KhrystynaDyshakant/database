import sys 
sys.path.append("C:/Users/admin/Desktop/database4")
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...contoller import stores_controller
from ...domain import Stores


stores_bp = Blueprint('stores', __name__, url_prefix='/stores')

@stores_bp.get('')
def get_all_stores() -> Response:
  
    return make_response(jsonify(stores_controller.find_all()), HTTPStatus.OK)

@stores_bp.get('/products')
def get_all_products() -> Response:
  
    return make_response(jsonify(stores_controller.find_all_products()), HTTPStatus.OK)

@stores_bp.post('')
def create_stores() -> Response:
   
    content = request.get_json()
    stores = Stores.create_from_dto(content)
    stores_controller.create(stores)
    return make_response(jsonify(stores.put_into_dto()), HTTPStatus.CREATED)


@stores_bp.get('/id/<int:stores_id>')
def get_stores(stores_id: int) -> Response:
    
    return make_response(jsonify(stores_controller.find_by_id(stores_id)), HTTPStatus.OK)

@stores_bp.get('/id/<int:stores_id>/products')
def get_products_by_stores_id(stores_id: int) -> Response:
    
    return make_response(jsonify(stores_controller.find_products_by_stores_id(stores_id)), HTTPStatus.OK)

@stores_bp.get('/name/<string:stores_name>')
def get_stores_by_name(stores_name: str) -> Response:
  
    return make_response(jsonify(stores_controller.find_by_name(stores_name)), HTTPStatus.OK)


@stores_bp.get('/address/<string:stores_address>')
def get_stores_by_address(stores_address: str) -> Response:
   
    return make_response(jsonify(stores_controller.find_by_address(stores_address)), HTTPStatus.OK)


@stores_bp.put('/<int:stores_id>')
def update_stores(stores_id: int) -> Response:
   
    content = request.get_json()
    stores = Stores.create_from_dto(content)
    stores_controller.update(stores_id, stores)
    return make_response("Stores updated", HTTPStatus.OK)


@stores_bp.patch('/<int:stores_id>')
def patch_stores(stores_id: int) -> Response:
    
    content = request.get_json()
    stores_controller.patch(stores_id, content)
    return make_response("Stores updated", HTTPStatus.OK)


@stores_bp.delete('/<int:stores_id>')
def delete_stores(stores_id: int) -> Response:
    
    stores_controller.delete(stores_id)
    return make_response("Stores deleted", HTTPStatus.OK)