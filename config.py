import os

class Config:
    SECRET_KEY = "your_secret_key"
    JWT_SECRET_KEY = "your_jwt_secret_key"
    
    # MySQL Config
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "your_mysql_password"
    MYSQL_DB = "streamvidz_db"
    
    # MongoDB Config
    MONGO_URI = "mongodb://localhost:27017/streamvidz"

    # IMDb API
    IMDB_API_KEY = "your_imdb_api_key"

