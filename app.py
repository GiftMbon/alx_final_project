from flask import Response, send_file
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes.video_routes import video_routes


app = Flask(__name__)
CORS(app)
app.config.from_object("config.Config")
jwt = JWTManager(app)

# Register routes
app.register_blueprint(video_routes, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)

