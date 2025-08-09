# Copilot Instructions for GeneralMLAPI

## Project Overview
- This repository provides a Flask-based API for serving machine learning models (regression/classification) and handling file uploads.
- The project is organized into two main components:
  - `api/`: Flask app, endpoints, middleware, templates, static files, and API-specific logic.
  - `model/`: ML service logic, model loading, and prediction routines.

## Key Architectural Patterns
- **Blueprints**: All routes are registered via a Flask `Blueprint` (`api/views.py`).
- **ML Service**: The ML model is loaded and managed via `current_app.ml_service` and invoked through the `/predict` endpoint.
- **File Uploads**: Handled in the root (`/`) route, with files saved to a directory defined in `settings.UPLOAD_FOLDER`.
- **Middleware**: Prediction logic is abstracted in `middleware.py` (see `model_predict`).
- **Templates/Static**: Jinja2 templates in `api/templates/`, static assets in `api/static/`.

## Developer Workflows
- **Run the API**: Start the Flask app from `api/app.py` (ensure dependencies in `api/requirements.txt` are installed).
- **Testing**: 
  - Unit and integration tests are in `tests/unittests/` and `tests/stress_tests/`.
  - Use standard `pytest` for unittests; stress tests use Locust (`locust.py`).
- **ML Model Integration**: Place model code in `model/ml_service.py`. The API expects a `predict` method.
- **Configuration**: All config (e.g., upload folder) is in `api/settings.py`.

## Project-Specific Conventions
- **Error Handling**: API endpoints return JSON error messages and HTTP status codes on failure.
- **Allowed File Types**: Controlled by `utils.allowed_file()`.
- **File Paths**: Use `os.path.join(settings.UPLOAD_FOLDER, ...)` for file storage.
- **Route Naming**: Use `app_router` for all blueprint routes.
- **ML Service Availability**: Always check `current_app.ml_service` before prediction.

## Integration Points
- **External Calls**: The `/predict` endpoint is designed for programmatic access (e.g., from Colab or other clients).
- **CORS**: If integrating with external clients, ensure CORS is enabled/configured as needed.
- **Docker**: Both `api/` and `model/` have Dockerfiles for containerized deployment.

## Example: Calling the Predict Endpoint
```python
import requests
files = {'file': open('yourfile.csv', 'rb')}
response = requests.post('http://localhost:5000/predict', files=files)
print(response.json())
```

## Key Files/Directories
- `api/views.py`: Main API routes and upload logic
- `api/middleware.py`: ML prediction logic
- `model/ml_service.py`: ML model code
- `api/settings.py`: Configuration
- `tests/`: All tests

---
For any new endpoints or features, follow the established patterns in `api/views.py` and keep business logic in middleware or model modules.
