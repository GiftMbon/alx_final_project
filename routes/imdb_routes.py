import os
import requests
from flask import Blueprint, render_template, request, redirect, url_for
from pymongo import MongoClient

# Blueprint for IMDb-related routes
imdb_routes = Blueprint('imdb_routes', __name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.imdb  # Use the "imdb" database
movies_collection = db.movies  # Use the "movies" collection

# IMDb API configuration
IMDB_API_KEY = "4f55db8a3dmsh66182f4a18deaedp1b0a6bjsn9c5930f0a56a"
IMDB_API_URL = "https://imdb8.p.rapidapi.com/v2/search"


@imdb_routes.route('/imdb/search', methods=['GET', 'POST'])
def search_imdb():
    """
    Search movies using the IMDb API and store the results in MongoDB.
    """
    if request.method == 'POST':
        query = request.form.get('query')  # Get the search query from the form
        response = requests.get(f"{IMDB_API_URL}/{IMDB_API_KEY}/{query}")
        
        if response.status_code == 200:
            data = response.json().get('results', [])
            
            # Insert data into MongoDB
            for movie in data:
                movie['_id'] = movie.get('id')  # Set the IMDb ID as the unique identifier
                movies_collection.update_one({'_id': movie['_id']}, {'$set': movie}, upsert=True)
            
            return render_template('search.html', movies=data)
        else:
            return {"error": "Failed to fetch data from IMDb API"}, 500
    
    return render_template('search.html')


@imdb_routes.route('/imdb/movies')
def list_movies():
    """
    Display all movies stored in MongoDB.
    """
    movies = list(movies_collection.find())  # Fetch all movies from MongoDB
    return render_template('search.html', movies=movies)


@imdb_routes.route('/imdb/movie/<id>')
def movie_details(id):
    """
    Display details for a specific movie.
    """
    movie = movies_collection.find_one({'_id': id})  # Find movie by IMDb ID
    if movie:
        return render_template('movie_details.html', movie=movie)
    else:
        return {"error": "Movie not found"}, 404

