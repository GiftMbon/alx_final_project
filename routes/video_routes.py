from flask import Blueprint, request, jsonify, Response, send_file
from services.video_service import process_video
from services.imdb_service import fetch_imdb_metadata
import os

video_routes = Blueprint("videos", __name__)
UPLOAD_FOLDER = "uploads"

@video_routes.route("/upload", methods=["POST"])
def upload_video():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files["file"]
    title = request.form.get("title")
    description = request.form.get("description")

     file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 201
        
        # Process video with FFmpeg
        processed_path = process_video(file_path, UPLOAD_FOLDER)
        
        # Fetch IMDb metadata
        imdb_data = fetch_imdb_metadata(title)
        #Generate Thumbnail
        thumbnail_path = generate_thumbnail(file_path, UPLOAD_FOLDER)

        # Save to database
        # Save processed_path and metadata to MySQL
        
        return jsonify({
            "message": "Video uploaded successfully!",
            "video_url": processed_path,
            "thumbnail_url": thumbnail_path,
            }), 201

# Create a Flask Blueprint for video routes
video_routes = Blueprint("video_routes", __name__)

# Directory where your videos are stored
VIDEO_DIR = "uploads"

@video_routes.route('/stream/<filename>', methods=['GET'])
def stream_video(filename):
    file_path = os.path.join(VIDEO_DIR, filename)

    if not os.path.exists(file_path):
        return {"error": "File not found"}, 404

    range_header = request.headers.get('Range', None)
    if not range_header:
        # If no range is specified, send the entire file
        return send_file(file_path, mimetype='video/mp4')

    # Parse the Range header
    start, end = parse_range_header(range_header, os.path.getsize(file_path))
    
    return partial_response(file_path, start, end)


def parse_range_header(range_header, file_size):
    """
    Parses the 'Range' header to extract the start and end byte positions.
    """
    # Example: "Range: bytes=0-1023"
    range_match = range_header.split("=")[1]  # Strip "bytes="
    start, end = range_match.split("-")
    start = int(start) if start else 0
    end = int(end) if end else file_size - 1
    return start, end


def partial_response(file_path, start, end):
    """
    Create a partial response with the requested byte range.
    """
    with open(file_path, 'rb') as f:
        # Seek to the requested start position
        f.seek(start)
        
        # Read the requested byte range
        chunk = f.read(end - start + 1)

    # Build the response
    response = Response(
        chunk,
        status=206,  # HTTP 206 Partial Content
        mimetype="video/mp4",
        direct_passthrough=True,
    )
    response.headers.add("Content-Range", f"bytes {start}-{end}/{os.path.getsize(file_path)}")
    response.headers.add("Accept-Ranges", "bytes")
    return response
        
