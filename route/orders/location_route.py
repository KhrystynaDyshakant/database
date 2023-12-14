import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...contoller import location_controller
from ...domain import Location

location_bp = Blueprint('location', __name__, url_prefix='/location')


@location_bp.get('')
def get_all_location() -> Response:

    return make_response(jsonify(location_controller.find_all()), HTTPStatus.OK)


@location_bp.post('')
def create_location() -> Response:

    content = request.get_json()
    location = Location.create_from_dto(content)
    location_controller.create(location)
    return make_response(jsonify(location.put_into_dto()), HTTPStatus.CREATED)


@location_bp.get('/id/<int:location_id>')
def get_location(location_id: int) -> Response:

    return make_response(jsonify(location_controller.find_by_id(location_id)), HTTPStatus.OK)

@location_bp.get('/get_delivery/<int:location_id>') 
def get_delivery(location_id): 
    return make_response(jsonify(location_controller.get_deliverys_in_location(location_id)))


@location_bp.get('/city_id/<int:location_city_id>')
def get_location_by_city_id(location_city_id: str) -> Response:

    return make_response(jsonify(location_controller.find_by_city_id(location_city_id)), HTTPStatus.OK)


@location_bp.get('/street_id/<int:location_street_id>')
def get_location_by_street_id(location_street_id: str) -> Response:

    return make_response(jsonify(location_controller.find_by_street_id(location_street_id)), HTTPStatus.OK)


@location_bp.put('/<int:location_id>')
def update_location(location_id: int) -> Response:
 
    content = request.get_json()
    location = Location.create_from_dto(content)
    location_controller.update(location_id, location)
    return make_response("Location updated", HTTPStatus.OK)


@location_bp.patch('/<int:location_id>')
def patch_location(location_id: int) -> Response:
   
    content = request.get_json()
    location_controller.patch(location_id, content)
    return make_response("Location updated", HTTPStatus.OK)


@location_bp.delete('/<int:location_id>')
def delete_location(location_id: int) -> Response:

    location_controller.delete(location_id)
    return make_response("Location deleted", HTTPStatus.OK)