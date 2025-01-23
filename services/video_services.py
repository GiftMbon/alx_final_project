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

