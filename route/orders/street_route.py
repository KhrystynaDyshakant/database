import sys 
sys.path.append("C:/Users/admin/Desktop/databasemany")
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...contoller import street_controller
from ...domain import Street

street_bp = Blueprint('street', __name__, url_prefix='/street')

@street_bp.get('')
def get_all_street() -> Response:
  
    return make_response(jsonify(street_controller.find_all()), HTTPStatus.OK)


@street_bp.post('')
def create_street() -> Response:
 
    content = request.get_json()
    street = Street.create_from_dto(content)
    street_controller.create(street)
    return make_response(jsonify(street.put_into_dto()), HTTPStatus.CREATED)


@street_bp.get('/id/<int:street_id>')
def get_street(street_id: int) -> Response:

    return make_response(jsonify(street_controller.find_by_id(street_id)), HTTPStatus.OK)

@street_bp.get('/get_location/<int:street_id>') 
def get_location(street_id): 
    return make_response(jsonify(street_controller.get_locations_in_street(street_id)))


@street_bp.get('/name/<string:street_name>')
def get_street_by_name(street_name: str) -> Response:

    return make_response(jsonify(street_controller.find_by_name(street_name)), HTTPStatus.OK)


@street_bp.get('/number_street/<string:street_number_street>')
def get_street_by_number_street(street_number_street: str) -> Response:

    return make_response(jsonify(street_controller.find_by_number_street(street_number_street)), HTTPStatus.OK)


@street_bp.put('/<int:street_id>')
def update_street(street_id: int) -> Response:

    content = request.get_json()
    street = Street.create_from_dto(content)
    street_controller.update(street_id, street)
    return make_response("Street updated", HTTPStatus.OK)


@street_bp.patch('/<int:street_id>')
def patch_street(street_id: int) -> Response:

    content = request.get_json()
    street_controller.patch(street_id, content)
    return make_response("Street updated", HTTPStatus.OK)


@street_bp.delete('/<int:street_id>')
def delete_street(street_id: int) -> Response:

    street_controller.delete(street_id)
    return make_response("Street deleted", HTTPStatus.OK)