# YouTube Playlist Snapshot
Basically, this script takes a snapshot of a non-private YouTube playlist by outputting each video's title and uploader to a text file.

Non-English characters, such as Japanese characters, are supported.

Region-blocked videos are also noted by the console output.

## Setup
### Version Notes
* I used Python version 3.9.0b3
    * Any version past Python 3.6 will probably work. A minimum of Python 3.6 is needed to support f-strings
* I used Python-YouTube version 0.6.0

### Steps
1. Run `pip install python-youtube` (preferably in a virtual environment)
2. [Follow these steps to set up a Google Project and create an API key](https://python-youtube.readthedocs.io/en/latest/getting_started.html)

This script uses Ikaro Kun's Python YouTube API instead of the official Google API to facilitate the gathering of more than 50 videos in a playlist.

## User Guide
1. Rename `MyConfigurationSample.py` to `MyConfiguration.py`
2. Fill in your API key in the new `MyConfiguration.py`
3. Fill in the appropriate two-letter country code in the new `MyConfiguration.py`
4. Fill in your playlists in the new `MyConfiguration.py`
5. Run `python -W ignore Main.py`
    * Ignore warnings about region-locked videos from the third-party API
    * For a playlist with 500 videos, this script may take a whole minute to parse through.
6. Look for text files with the extension `.out` within the subfolders under the `output` folder

## Additional Notes
The `outputSample` folder contains a sample of the output files produced from running this script. All contents within this folder, including the folder itself, are safe to delete once you have cloned the repository.

## Future Plans
* Automate a diff tool between various output files

## Acknowledgments
THANK YOU, Ikaros Kun! Your wrapper and crystal clear documentation made this effort so much easier to work though! Please check out their API here: https://pypi.org/project/python-youtube/

