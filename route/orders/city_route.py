import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...contoller import city_controller
from ...domain import City

city_bp = Blueprint('city', __name__, url_prefix='/city')


@city_bp.get('')
def get_all_city() -> Response:

    return make_response(jsonify(city_controller.find_all()), HTTPStatus.OK)


@city_bp.post('')
def create_city() -> Response:

    content = request.get_json()
    city = City.create_from_dto(content)
    city_controller.create(city)
    return make_response(jsonify(city.put_into_dto()), HTTPStatus.CREATED)


@city_bp.get('/id/<int:city_id>')
def get_city(city_id: int) -> Response:

    return make_response(jsonify(city_controller.find_by_id(city_id)), HTTPStatus.OK)

@city_bp.get('/get_location/<int:city_id>') 
def get_location(city_id): 
    return make_response(jsonify(city_controller.get_locations_in_city(city_id)))


@city_bp.get('/name/<string:city_name>')
def get_city_by_name(city_name: str) -> Response:
 
    return make_response(jsonify(city_controller.find_by_name(city_name)), HTTPStatus.OK)


@city_bp.put('/<int:city_id>')
def update_city(city_id: int) -> Response:
 
    content = request.get_json()
    city = City.create_from_dto(content)
    city_controller.update(city_id, city)
    return make_response("City updated", HTTPStatus.OK)


@city_bp.patch('/<int:city_id>')
def patch_city(city_id: int) -> Response:
  
    content = request.get_json()
    city_controller.patch(city_id, content)
    return make_response("City updated", HTTPStatus.OK)


@city_bp.delete('/<int:city_id>')
def delete_city(city_id: int) -> Response:
    
    city_controller.delete(city_id)
    return make_response("City deleted", HTTPStatus.OK)