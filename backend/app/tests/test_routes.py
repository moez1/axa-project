import pytest
import sys
import os
from typing import Generator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from app import create_app, db
from app.models import TitanicPassenger
from flask import url_for
from flask.testing import FlaskClient

@pytest.fixture
def app() -> Generator:
    """
    Create and configure a new app instance for each test.

    Yields:
        Flask: The Flask app instance.
    """
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SERVER_NAME": "localhost"  # Add this line
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app) -> FlaskClient:
    """
    Create a test client for the app.

    Args:
        app (Flask): The Flask app instance.

    Returns:
        FlaskClient: The test client.
    """
    return app.test_client()

def test_upload_csv(client: FlaskClient) -> None:
    """
    Test the CSV upload endpoint.

    Args:
        client (FlaskClient): The test client.

    Raises:
        AssertionError: If the response status code or message is incorrect.
    """
    data = {
        'file': (open('c:/Users/lenovo/Documents/AXA-project/backend/app/tests/test_data.csv', 'rb'), 'test_data.csv')  # Ensure this file exists
    }
    response = client.post(url_for('main.upload_csv'), data=data, content_type='multipart/form-data')
    assert response.status_code == 201
    assert response.json['message'] == 'CSV data uploaded successfully'

def test_get_passengers(client: FlaskClient) -> None:
    """
    Test the get passengers endpoint.

    Args:
        client (FlaskClient): The test client.

    Raises:
        AssertionError: If the response status code or data is incorrect.
    """
    passenger = TitanicPassenger(name='John Doe', sex='male', age=30)
    db.session.add(passenger)
    db.session.commit()

    response = client.get(url_for('main.get_passengers'))
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == 'John Doe'

def test_create_passenger(client: FlaskClient) -> None:
    """
    Test the create passenger endpoint.

    Args:
        client (FlaskClient): The test client.

    Raises:
        AssertionError: If the response status code or data is incorrect.
    """
    data = {
        'name': 'Jane Doe',
        'sex': 'female',
        'age': 25
    }
    response = client.post(url_for('main.create_passenger'), json=data)
    assert response.status_code == 201
    assert response.json['name'] == 'Jane Doe'

def test_update_passenger(client: FlaskClient) -> None:
    """
    Test the update passenger endpoint.

    Args:
        client (FlaskClient): The test client.

    Raises:
        AssertionError: If the response status code or data is incorrect.
    """
    passenger = TitanicPassenger(name='John Doe', sex='male', age=30)
    db.session.add(passenger)
    db.session.commit()

    data = {
        'name': 'John Smith',
        'sex': 'male',
        'age': 35
    }
    response = client.put(url_for('main.update_passenger', id=passenger.id), json=data)
    assert response.status_code == 200
    assert response.json['name'] == 'John Smith'

def test_delete_passenger(client: FlaskClient) -> None:
    """
    Test the delete passenger endpoint.

    Args:
        client (FlaskClient): The test client.

    Raises:
        AssertionError: If the response status code is incorrect.
    """
    passenger = TitanicPassenger(name='John Doe', sex='male', age=30)
    db.session.add(passenger)
    db.session.commit()

    response = client.delete(url_for('main.delete_passenger', id=passenger.id))
    assert response.status_code == 204
    assert db.session.get(TitanicPassenger, passenger.id) is None