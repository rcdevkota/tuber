"""
setup.py
"""
from setuptools import setup

APP = ['tube.py']   # Name of your main Python script
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': None,  # You can set an .icns icon here if you have one
    'packages': ['yt_dlp'],   # Include any packages (like yt_dlp) you use
    'plist': {
        'CFBundleName': 'My YouTube Downloader',
        'CFBundleShortVersionString': '1.0',
        'CFBundleVersion': '1.0',
        'CFBundleIdentifier': 'com.yourcompany.youtube-downloader',
    },
}

setup(
    app=APP,
    name='MyYouTubeDLApp',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
