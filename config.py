import os

# Flask App Configuration
DEBUG = True  # Set to False in production
SECRET_KEY = os.getenv("SECRET_KEY", "4f55db8a3dmsh66182f4a18deaedp1b0a6bjsn9c5930f0a56a")

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/streaming_app")

# IMDb API Configuration
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "4f55db8a3dmsh66182f4a18deaedp1b0a6bjsn9c5930f0a56a")  
RAPIDAPI_HOST = "imdb8.p.rapidapi.com"

# MongoDB URI configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/streaming_app")
