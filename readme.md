# YouTube Video Downloader

A simple Python script to download the best video and audio from YouTube using the `yt-dlp` library.

This script prioritizes downloading the highest quality video (up to 4K) and audio separately, then merges them into a single file. If 4K resolution is not available, it will download the best available video and audio.

## Features

- Downloads the best video and audio from YouTube.
- Prioritizes 4K resolution if available.
- Saves the downloaded video in the **Downloads** folder by default.
- Cross-platform support (Windows, macOS, Linux).
- Requires `FFmpeg` for merging video and audio streams.

## Prerequisites

Before running the script, ensure you have the following installed:

1. **Python 3**: Download and install from [here](https://www.python.org/downloads/).
2. **yt-dlp**: Install using pip:

    ```bash
    pip install yt-dlp
    ```

3. **FFmpeg**: Required to merge video and audio.

    - **macOS**: Install via Homebrew:

      ```bash
      brew install ffmpeg
      ```

    - **Linux** (Debian/Ubuntu):

      ```bash
      sudo apt install ffmpeg
      ```

    - **Windows**: Download FFmpeg from [here](https://ffmpeg.org/download.html) and add it to your PATH.

## Usage

1. Clone or download this repository to your local machine.

2. Run the Python script:

    ```bash
    python youtube_downloader.py
    ```

3. Enter the YouTube video URL when prompted.

4. The script will download the best video and audio available, then save it to your **Downloads** folder.

### Changing the Downloads Folder Path

By default, the video is saved in the **Downloads** folder. If you want to change this folder:

- On **Windows**, replace the `downloads_folder` path in the script with:

    ```python
    downloads_folder = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
    ```

- On **macOS/Linux**, the default path is already set to the user’s Downloads folder.

## Example

```bash
Enter the YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Download completed and saved to: /Users/YourUsername/Downloads
