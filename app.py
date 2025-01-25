from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from flask_pymongo import PyMongo
import requests
import os
import config

app = Flask(__name__)
app.config.from_object(config)  # Load configuration from config.py

# Initialize PyMongo with app
mongo = PyMongo(app)

# Access the MongoDB collection
db = mongo.db
videos_collection = db.videos  # Reference to the "videos" collection

# MongoDB Configuration
client = MongoClient("mongodb://localhost:27017/")
db = client["streaming_app"]
favorites_collection = db["favorites"]

# IMDb API Configuration
RAPIDAPI_KEY = "4f55db8a3dmsh66182f4a18deaedp1b0a6bjsn9c5930f0a56a"
RAPIDAPI_HOST = "imdb8.p.rapidapi.com"

headers = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')
        url = "https://imdb8.p.rapidapi.com/title/find"
        params = {"q": query}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            return render_template('search_results.html', results=results)
        else:
            return render_template('search_results.html', error="Error fetching results from IMDb.")
    return redirect(url_for('home'))

@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    movie = {
        "id": request.form.get("id"),
        "title": request.form.get("title"),
        "image": request.form.get("image"),
        "year": request.form.get("year")
    }
    if movie["id"] and not favorites_collection.find_one({"id": movie["id"]}):
        favorites_collection.insert_one(movie)
    return redirect(url_for('favorites'))

@app.route('/favorites')
def favorites():
    favorites = list(favorites_collection.find())
    return render_template('favorites.html', favorites=favorites)

@app.route('/remove_favorite/<movie_id>', methods=['POST'])
def remove_favorite(movie_id):
    favorites_collection.delete_one({"id": movie_id})
    return redirect(url_for('favorites'))

if __name__ == '__main__':
    app.run(debug=True)

