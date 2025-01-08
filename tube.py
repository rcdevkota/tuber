import os
import yt_dlp

def download_video():
    youtube_link = input("Enter the YouTube video URL (or type 'exit' to quit): ")
    if youtube_link.lower() == 'exit':
        print("Exiting the program.")
        return

    downloads_folder = os.path.expanduser("~/Downloads")

    # (1) Force best video up to 2160p that uses h.264 and best audio that uses aac.
    #     If no 2160p h.264 track is available, it will fall back to any lower h.264.
    ydl_opts = {
        'format': (
            # Try H.264 up to 2160p with AAC audio
            'bestvideo[height<=2160][vcodec~=avc1]+bestaudio[acodec~=mp4a]/best'
        ),
        'merge_output_format': 'mp4',  
        'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
        # You do NOT need recode_video if you are only downloading h.264/aac
        # No re-encode is performed, just a container mux.
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4'
        }]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_link])
        print(f"Download completed and saved to: {downloads_folder}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Ask for another link
    download_video()

download_video()
