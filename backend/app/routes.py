from flask import Blueprint, request, jsonify
from app import db
from app.models import TitanicPassenger
from app.schemas import TitanicPassengerSchema
from flasgger import swag_from
from sqlalchemy.exc import OperationalError
from werkzeug.utils import secure_filename
import os
import pandas as pd

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@main.route('/upload-csv/', methods=['POST'])
@swag_from({
    'consumes': ['multipart/form-data'],
    'parameters': [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': 'The CSV file to upload'
        }
    ],
    'responses': {
        201: {
            'description': 'CSV data uploaded successfully'
        },
        400: {
            'description': 'Invalid file format'
        }
    }
})
def upload_csv():
    """
    Handle CSV file upload and store data in the database.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and file.filename.endswith('.csv'):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        
        # Process the CSV file and store data in the database
        data = pd.read_csv(file_path)
        for _, row in data.iterrows():
            passenger = TitanicPassenger(name=row['Name'], sex=row['Sex'], age=row['Age'])
            db.session.add(passenger)
        db.session.commit()
        
        return jsonify({'message': 'CSV data uploaded successfully'}), 201
    else:
        return jsonify({"error": "Invalid file format"}), 400

@main.route('/passengers/', methods=['GET'])
def get_passengers():
    """
    Retrieve a list of all Titanic passengers.
    """
    passengers = TitanicPassenger.query.all()
    return jsonify([p.as_dict() for p in passengers])

@main.route('/passengers/', methods=['POST'])
def create_passenger():
    """
    Create a new Titanic passenger.
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
def update_passenger(id):
    """
    Update an existing Titanic passenger.
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
def delete_passenger(id):
    """
    Delete a Titanic passenger.
    """
    passenger = TitanicPassenger.query.get(id)
    if not passenger:
        return jsonify({'error': 'Passenger not found'}), 404
    db.session.delete(passenger)
    db.session.commit()
    return '', 204