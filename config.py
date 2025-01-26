import os

#Flask App Configuration
DEBUG = True  # Set to False in production
SECRET_KEY = os.getenv("SECRET_KEY", "eb20a01318mshfec66769bdb09e9p1573b4jsne94cfcd220ed")

#MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/streamvidz")

#IMDb API Configuration
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "eb20a01318mshfec66769bdb09e9p1573b4jsne94cfcd220ed")  
RAPIDAPI_HOST = "imdb8.p.rapidapi.com"

#MongoDB URI configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/streamvidz")
