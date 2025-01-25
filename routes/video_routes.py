import os
from flask import Blueprint, render_template, request, send_file, redirect, url_for

# Define the Blueprint for video-related routes
video_routes = Blueprint('video_routes', __name__)

# Directory to store uploaded videos
UPLOAD_FOLDER = 'uploads'

# Ensure the uploads directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@video_routes.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')


@video_routes.route('/search')
def search():
    """
    Handle the search functionality for videos.
    Filters videos in the uploads folder based on the query.
    """
    query = request.args.get('query', '').lower()  # Get the search query
    results = []  # Initialize results list

    if query:
        # List all files in the uploads folder
        all_videos = os.listdir(UPLOAD_FOLDER)
        # Filter files containing the query string (case insensitive)
        results = [video for video in all_videos if query in video.lower()]

    # Render the index page with the search results
    return render_template('index.html', results=results)


@video_routes.route('/upload', methods=['GET', 'POST'])
def upload_video():
    """
    Handle video uploads.
    - GET: Render the upload form.
    - POST: Save the uploaded video to the uploads folder.
    """
    if request.method == 'POST':
        file = request.files.get('file')  # Get the uploaded file
        if file:
            # Save the file to the uploads directory
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            return redirect(url_for('video_routes.index'))  # Redirect to the main page

    # Render the upload page
    return render_template('upload.html')


@video_routes.route('/stream/<filename>')
def stream_video(filename):
    """
    Stream a video file from the uploads directory.
    """
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        # Send the video file as a response
        return send_file(file_path, mimetype='video/mp4')
    except FileNotFoundError:
        # Return a 404 error if the file is not found
        return {"error": "File not found"}, 404

