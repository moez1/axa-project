# AXA Project Backend

## Introduction
This project is the backend service for the AXA project. It provides APIs and handles business logic for the application.

## Requirements
- Python 3.8+
- Flask
- PostgreSQL
- Redis
- Docker (optional, for containerization)

## Installation

### Clone the repository
```sh
git clone https://github.com/yourusername/axa-project-backend.git
```

2. Navigate to the project directory:
    ```sh
    cd axa-project-backend
    ```

## License
This project is licensed under the MIT License.

## Project Structure
```markdown
backend/
    app/
        __init__.py
        database.py
        models.py
        routes.py
        tests/
    Dockerfile
    requirements.txt
    run.py
[docker-compose.yml](http://_vscodecontentref_/2)
```

## Setup
```sh
cd axa-project-backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python run.py
```

## API Endpoints
### Upload CSV
- URL: /upload-csv/
- Method: POST
- Description: Upload a CSV file and store data in the database.
- Response: JSON response indicating success.

### Get Passengers
- URL: /passengers/
- Method: GET
- Description: Retrieve a list of all Titanic passengers.
- Response: JSON response containing a list of passengers.

### Create Passenger
- URL: /passengers/
- Method: POST
- Description: Create a new Titanic passenger.
- Response: JSON response containing the created passenger.

### Update Passenger
- URL: /passengers/<int:id>/
- Method: PUT
- Description: Update an existing Titanic passenger.
- Response: JSON response containing the updated passenger.

### Delete Passenger
- URL: /passengers/<int:id>/
- Method: DELETE
- Description: Delete a Titanic passenger.
- Response: Empty response indicating success.



## API Documentation swagger
The API documentation is available at `http://localhost:5000/apidocs/`.