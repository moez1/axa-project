from flask import Blueprint, request, jsonify
from app import db
from app.models import TitanicPassenger
from app.schemas import TitanicPassengerSchema
from flasgger import swag_from
from sqlalchemy.exc import OperationalError

main = Blueprint('main', __name__)

@main.route('/upload-csv/', methods=['POST'])
@swag_from({
    'responses': {
        201: {
            'description': 'CSV data uploaded successfully'
        }
    }
})
def upload_csv() -> jsonify:
    """
    Handle CSV file upload and store data in the database.

    Returns:
        Response: JSON response indicating success.
    """
    # Logic to handle CSV upload
    return jsonify({'message': 'CSV data uploaded successfully'}), 201

@main.route('/passengers/', methods=['GET'])
def get_passengers() -> jsonify:
    """
    Retrieve a list of all Titanic passengers.

    Returns:
        Response: JSON response containing a list of passengers.
    """
    passengers = TitanicPassenger.query.all()
    return jsonify([p.as_dict() for p in passengers])

@main.route('/passengers/', methods=['POST'])
def create_passenger() -> jsonify:
    """
    Create a new Titanic passenger.

    Returns:
        Response: JSON response containing the created passenger.
    """
    data = request.get_json()
    schema = TitanicPassengerSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    passenger = TitanicPassenger(name=data['name'], sex=data['sex'], age=data['age'])
    db.session.add(passenger)
    db.session.commit()
    return jsonify(passenger.as_dict()), 201

@main.route('/passengers/<int:id>/', methods=['PUT'])
def update_passenger(id: int) -> jsonify:
    """
    Update an existing Titanic passenger.

    Args:
        id (int): The ID of the passenger to update.

    Returns:
        Response: JSON response containing the updated passenger.
    """
    data = request.get_json()
    schema = TitanicPassengerSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    passenger = TitanicPassenger.query.get(id)
    if not passenger:
        return jsonify({'error': 'Passenger not found'}), 404
    passenger.name = data['name']
    passenger.sex = data['sex']
    passenger.age = data['age']
    db.session.commit()
    return jsonify(passenger.as_dict())

@main.route('/passengers/<int:id>/', methods=['DELETE'])
def delete_passenger(id: int) -> str:
    """
    Delete a Titanic passenger.

    Args:
        id (int): The ID of the passenger to delete.

    Returns:
        Response: Empty response indicating success.
    """
    passenger = TitanicPassenger.query.get(id)
    if not passenger:
        return jsonify({'error': 'Passenger not found'}), 404
    db.session.delete(passenger)
    db.session.commit()
    return '', 204