from flask import Blueprint, request, jsonify
from services.video_service import process_video
from services.imdb_service import fetch_imdb_metadata
import os

video_routes = Blueprint("videos", __name__)
UPLOAD_FOLDER = "uploads"

@video_routes.route("/upload", methods=["POST"])
def upload_video():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files["file"]
    title = request.form.get("title")
    description = request.form.get("description")
    
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        
        # Process video with FFmpeg
        processed_path = process_video(file_path, UPLOAD_FOLDER)
        
        # Fetch IMDb metadata
        imdb_data = fetch_imdb_metadata(title)
        
        # Save to database (example)
        # Save processed_path and metadata to MySQL
        
        return jsonify({"message": "Video uploaded successfully!"}), 201
