from flask import Flask, render_template, request, redirect, url_for, Response
from pymongo import MongoClient
import requests
import subprocess

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient('mongodb://localhost:27017')
db = client['streamvidz']
movies_collection = db['movies']
favorites_collection = db['favorites']

# IMDb API Configuration
RAPIDAPI_KEY = "eb20a01318mshfec66769bdb09e9p1573b4jsne94cfcd220ed"
RAPIDAPI_HOST = "imdb8.p.rapidapi.com"

headers = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST
}

@app.route("/")
def home():
    featured_movies = list(movies_collection.find().limit(8))
    return render_template("index.html", featured_movies=featured_movies)

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        url = "https://imdb8.p.rapidapi.com/title/find"
        params = {"q": query}
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            for movie in results:
                save_movie_to_db(movie)  # Save to MongoDB
            return render_template("search_results.html", results=results)
        else:
            return render_template("search_results.html", error="Error fetching results.")
    return redirect(url_for("home"))

@app.route("/stream/<movie_id>")
def stream(movie_id):
    # Find the movie in the database
    movie = movies_collection.find_one({"id": movie_id})
    
    if not movie:
        return "Movie not found!", 404

    # Replace this with the actual path to the movie file you want to stream
    movie_file_path = f"/path/to/movies/{movie['title']}.mp4"  # Modify based on your storage
    
    # Open the video file and stream it using FFmpeg
    def generate():
        process = subprocess.Popen(
            ['ffmpeg', '-i', movie_file_path, '-f', 'flv', '-'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        while True:
            data = process.stdout.read(1024)
            if not data:
                break
            yield data
    
    return Response(generate(), content_type='video/flv')

def save_movie_to_db(movie):
    movie_document = {
        "id": movie.get("id"),
        "title": movie.get("title"),
        "year": movie.get("year"),
        "image": movie.get("image", {}).get("url", ""),
        "description": movie.get("description", ""),
    }
    movies_collection.update_one(
        {"id": movie.get("id")},
        {"$set": movie_document},
        upsert=True
    )

if __name__ == "__main__":
    app.run(debug=True)

