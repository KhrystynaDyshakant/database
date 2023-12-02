import sys 
sys.path.append("C:/Users/admin/Desktop/database4")

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...contoller import products_controller
from ...domain import Products

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.get('')
def get_all_products() -> Response:

    return make_response(jsonify(products_controller.find_all()), HTTPStatus.OK)


@products_bp.post('')
def create_products() -> Response:

    content = request.get_json()
    products = Products.create_from_dto(content)
    products_controller.create(products)
    return make_response(jsonify(products.put_into_dto()), HTTPStatus.CREATED)


@products_bp.get('/id/<int:products_id>')
def get_products(products_id: int) -> Response:

    return make_response(jsonify(products_controller.find_by_id(products_id)), HTTPStatus.OK)

@products_bp.get('/id/<int:products_id>/orders')
def get_orders_by_product_id(products_id: int) -> Response:
    return make_response(jsonify(products_controller.find_orders_by_product_id(products_id)), HTTPStatus.OK)

@products_bp.get('/product_name/<string:product_name>')
def get_products_by_name(product_name: str) -> Response:
 
    return make_response(jsonify(products_controller.find_by_name(product_name)), HTTPStatus.OK)


@products_bp.get('/description/<string:products_description>')
def get_products_by_description(products_description: str) -> Response:
  
    return make_response(jsonify(products_controller.find_by_description(products_description)), HTTPStatus.OK)


@products_bp.get('/price/<int:products_price>')
def get_products_by_price(products_price: int) -> Response:
   
    return make_response(jsonify(products_controller.find_by_price(products_price)), HTTPStatus.OK)


@products_bp.get('/position/<string:products_position>')
def get_products_by_position(products_position: str) -> Response:
   
    return make_response(jsonify(products_controller.find_by_position(products_position)), HTTPStatus.OK)


@products_bp.put('/<int:products_id>')
def update_products(products_id: int) -> Response:
 
    content = request.get_json()
    products = Products.create_from_dto(content)
    products_controller.update(products_id, products)
    return make_response("Products updated", HTTPStatus.OK)


@products_bp.patch('/<int:products_id>')
def patch_products(products_id: int) -> Response:
  
    content = request.get_json()
    products_controller.patch(products_id, content)
    return make_response("Products updated", HTTPStatus.OK)


@products_bp.delete('/<int:products_id>')
def delete_products(products_id: int) -> Response:
    
    products_controller.delete(products_id)
    return make_response("Products deleted", HTTPStatus.OK)