## **StreamVidz**

##SCREENSHOT OF HOMEPAGE
![Screenshot 2025-01-26 223234](https://github.com/user-attachments/assets/cabe0e5a-94f4-4cb5-88b0-db2e667eefaa)


StreamVidz is a movie streaming web application built with Flask and MongoDB. It integrates with the IMDb API via RapidAPI to fetch movie data, stores it in MongoDB, and allows users to search for movies and stream search results using FFmpeg. The homepage displays a selection of featured movies with their posters and titles.

##Features
1. Fetch Movies from IMDb API
Fetch movie data (titles, posters, descriptions) from the IMDb API via RapidAPI and store it in MongoDB.
2. Featured Movies on Homepage
Display up to 8 featured movies on the homepage in a grid format with their posters and titles.
3. Search Functionality
Users can search for movies via a search bar. The app fetches search results from IMDb, displays them, and stores the results in MongoDB.
4. Stream Search Results
Search results are integrated with FFmpeg to allow seamless video streaming.
5. Favorites Management
Users can add or remove movies from a favorites list, which is stored in MongoDB.
6. Responsive UI
A modern, dark-themed interface with a responsive design for mobile and desktop views.

##Technologies Used
1. Backend: Flask (Python)
2. Database: MongoDB
3. AFrontend: HTML, CSS
4. API Integration: IMDb API via RapidAPI
5. Video Streaming: FFmpeg.

##Installation
#Prerequisites
1. Python 3
2. MongoDB installed
3. FFmpeg installed on your system
4. A RapidAPI account and IMDb API key


#Steps
1. Clone the repository:
git clone https://github.com/GiftMbon/alx_final_project.git
cd alx_final_project
2. Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate
3. Install the required dependencies:
pip install -r requirements.txt
4. Set up your MongoDB:
-Ensure MongoDB is running locally or remotely.
-Update the MongoDB URI in the config.py file or set it as an environment variable:
MONGO_URI = "mongodb://localhost:27017/streamvidz"
5. Configure your RapidAPI key:
-Replace your_api_key_here in app.py with your RapidAPI IMDb API key.
6. Run the application:
python3 app.py
7. Access the application:
-Open your browser and navigate to http://127.0.0.1:5000.

##API Integration
-IMDb API: Used to fetch movie data (title, description, poster, etc.).
-FFmpeg: Used to stream video results from movie URLs.
 
##Troubleshooting
-Invalid API Key: Ensure your RapidAPI IMDb API key is correct and hasn’t expired.
-MongoDB Connection Errors: Verify that your MongoDB URI is correctly configured and the database is running.
-FFmpeg Issues: Ensure FFmpeg is installed and available in your system’s PATH.

##License

