import os
import yt_dlp

def download_video():
    # Declare a variable for the YouTube link
    youtube_link = input("Enter the YouTube video URL (or type 'exit' to quit): ")
    
    if youtube_link.lower() == 'exit':
        print("Exiting the program.")
        return  # Stop recursion if the user wants to exit

    # Define the path to the Downloads folder
    downloads_folder = os.path.expanduser("~/Downloads")

    # Options to prioritize downloading 4K (2160p) if available, otherwise the best video + best audio
    ydl_opts = {
        'format': 'bestvideo[height<=2160]+bestaudio/best',  # Prioritize 4K or lower if 4K is not available
        'merge_output_format': 'mp4',                        # Final output format as mp4
        'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),  # Save to Downloads folder
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',                         # Convert video to mp4 if needed
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_link])

        print(f"Download completed and saved to: {downloads_folder}")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Ask for another link after the current download finishes
    download_video()

# Start the program
download_video()
