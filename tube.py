import os
import yt_dlp
import subprocess
import shlex

def download_video():
    # Prompt for the YouTube URL
    youtube_link = input("Enter the YouTube video URL (or type 'exit' to quit): ")
    if youtube_link.lower() == 'exit':
        print("Exiting.")
        return

    # Define the path to the Downloads folder
    downloads_folder = os.path.expanduser("~/Downloads")
    
    # Basic yt_dlp options to grab up to 4K
    ydl_opts = {
        'format': 'bestvideo[height<=2160]+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
        # keepvideo not strictly necessary here, but included for demonstration
        'keepvideo': True,
    }

    # Download the video
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_link, download=True)
            # info dict contains metadata about the downloaded video

        # The *expected* final merged file path is typically:
        downloaded_path = ydl.prepare_filename(info)
        # Because we used `merge_output_format`, it ends with .mp4 (e.g. "Video Title.mp4")
        
        print(f"Downloaded file: {downloaded_path}")

        # Now check if the video is already H.264, and if not, re-encode
        reencode_video_if_needed(downloaded_path)
        
    except Exception as e:
        print(f"An error occurred: {e}")

    # Ask for another link
    download_video()

def reencode_video_if_needed(file_path):
    """Check if the video track is H.264; if not, re-encode to H.264 + AAC."""
    codec_name = get_video_codec(file_path)
    print(f"Detected video codec: {codec_name}")
    
    if codec_name.lower() == 'h264':
        print("The video is already H.264. No re-encode needed.")
        return
    
    # Otherwise, re-encode using FFmpeg
    # We'll put the new file next to the original, with a suffix like '_h264.mp4'
    new_file_path = file_path.rsplit('.', 1)[0] + '_h264.mp4'

    # Example ffmpeg command:
    # ffmpeg -i <input> -c:v libx264 -c:a aac -crf 18 -preset medium <output>
    command = [
        'ffmpeg',
        '-y',               # overwrite output if it exists
        '-i', file_path,    
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-crf', '18',
        '-preset', 'medium',
        new_file_path
    ]

    print(f"Re-encoding to H.264 -> {new_file_path}")
    subprocess.run(command, check=True)
    print("Re-encode completed.")

def get_video_codec(file_path):
    """Use ffprobe to detect the video codec of the first video stream."""
    # ffprobe -v error -select_streams v:0 -show_entries stream=codec_name \
    #         -of default=noprint_wrappers=1:nokey=1 <file>
    command = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=codec_name',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        file_path
    ]
    
    try:
        # Run ffprobe and capture the codec name
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        codec_name = result.stdout.strip()
        return codec_name
    except subprocess.CalledProcessError as e:
        print(f"Failed to probe video codec: {e}")
        return ""

# Start the script
download_video()
