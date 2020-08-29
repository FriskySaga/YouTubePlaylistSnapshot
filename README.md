# YouTube Playlist Snapshot
Basically, this script takes a snapshot of a non-private YouTube playlist by outputting each video's title and uploader to a text file.

Non-English characters, such as Japanese characters, are supported.

## Setup
Python version 3.9.0b3
Python-YouTube version 0.6.0

1. Run `pip install python-youtube` (preferably in a virtual environment)
2. [Follow these steps to set up a Google Project and create an API key](https://python-youtube.readthedocs.io/en/latest/getting_started.html)

This script uses Ikaro Kun's Python YouTube API instead of the official Google API to facilitate the gathering of more than 50 videos in a playlist.

## User Guide
1. Rename _MyConfigurationSample.py_ to _MyConfiguration.py_
2. Fill in your API key in the new _MyConfiguration.py_
3. Fill in your playlists in the new _MyConfiguration.py_
4. Run `python -W ignore Main.py`
    * Ignore warnings about region-locked videos because we still want to fetch the title & uploader
    * For a playlist with 500 videos, this script may take a whole minute to parse through.
5. Look for text files with the extension `.out` within the subfolder `output`

## Additional Notes
The _outputSample_ folder contains a sample of an output file produced from running this script. This folder and this file are both safe to delete once you've cloned this repository.

## Future Plans
* Automate a diff tool between various output files

## Acknowledgments
THANK YOU, Ikaros Kun! Your wrapper and crystal clear documentation made this effort so much easier to work though! Please check out their API here: https://pypi.org/project/python-youtube/

