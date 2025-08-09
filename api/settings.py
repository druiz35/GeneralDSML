import os

# API Settings
API_DEBUG = os.getenv('API_DEBUG', 'True') == 'True'

# For now, user inputs and data will be stored locally
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads/')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Redis configuration
REDIS_QUEUE = os.getenv('REDIS_QUEUE', 'ml_tasks')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_DB_ID = int(os.getenv('REDIS_DB_ID', 0))
REDIS_IP = os.getenv('REDIS_IP', 'redis')
API_SLEEP = int(os.getenv('API_SLEEP', 0.05))