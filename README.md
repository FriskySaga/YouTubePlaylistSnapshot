# YouTube Playlist Snapshot
Basically, this script takes a snapshot of a non-private YouTube playlist by outputting its video titles to a text file.

Non-English characters, such as Japanese characters, are supported.

## Setup
Python version 3.9.0b3
Python-YouTube version 0.6.0

1. Run `pip install python-youtube` (preferably in a virtual environment)
2. [Follow these steps to set up a Google Project and create an API key](https://python-youtube.readthedocs.io/en/latest/getting_started.html)

This script uses the Python YouTube API instead of the official Google API to facilitate the gathering of more than 50 videos in a playlist.

## User Guide
1. Rename _MyConfigurationSample.py_ to _MyConfiguration.py_
2. Fill in your API key in the new _MyConfiguration.py_
3. Fill in your playlists in the new _MyConfiguration.py_
4. Run `python Main.py`
5. Look for text files with the extension `.out`

## Resources
* https://pypi.org/project/python-youtube/
* https://python-youtube.readthedocs.io/en/latest/getting_started.html

## Future Plans
* Automate a diff tool between various output files
* Add option to show the video uploader's channel name

