import ffmpeg
import os

def process_video(file_path, output_dir):
    # Example: Convert video to MP4 with FFmpeg
    output_file = os.path.join(output_dir, "processed.mp4")
    (
        ffmpeg
        .input(file_path)
        .output(output_file, vcodec="libx264", acodec="aac", preset="fast")
        .run()
    )
    return output_file

def generate_thumbnail(file_path, output_dir, time="00:00:05"):
    """
    Generate a thumbnail from the video at a specified time (default: 5 seconds).
    """
    thumbnail_path = os.path.join(output_dir, "thumbnail.jpg")
    (
        ffmpeg
        .input(file_path, ss=time)
        .output(thumbnail_path, vframes=1)
        .run()
    )
    return thumbnail_path
