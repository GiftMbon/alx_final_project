from flask import Response, send_file
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes.video_routes import video_routes

@video_routes.route("/stream/<video_id>")
def stream_video(video_id):
    video_path = get_video_path(video_id)  # Fetch video path from DB
    return send_file(video_path, as_attachment=False)

app = Flask(__name__)
CORS(app)
app.config.from_object("config.Config")
jwt = JWTManager(app)

# Register routes
app.register_blueprint(video_routes, url_prefix="/api/videos")

if __name__ == "__main__":
    app.run(debug=True)

