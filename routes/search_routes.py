from flask import Blueprint, request, jsonify
import pymysql
from config import Config

search_routes = Blueprint("search", __name__)

def connect_mysql():
    return pymysql.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )

@search_routes.route("/search", methods=["GET"])
def search_videos():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Search query is required"}), 400
    
    connection = connect_mysql()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    search_query = f"SELECT * FROM videos WHERE title LIKE %s OR description LIKE %s"
    cursor.execute(search_query, (f"%{query}%", f"%{query}%"))
    results = cursor.fetchall()
    connection.close()
    
    return jsonify(results), 200
