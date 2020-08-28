"""Generate a text file containing the title of all the videos in a playlist.
"""

# External modules
from pyyoutube import Api
from time import localtime, strftime

# Internal modules that are kept secret
import MyConfigurations

if __name__ == '__main__':
  api = Api(api_key=MyConfigurations.API_KEY)

  playlistIDs = MyConfigurations.PLAYLIST_IDS

  # Remember to comment out the individual playlist keys from MyConfigurations if you don't want to loop through them all
  for key in playlistIDs:
    playlistVideoItems = api.get_playlist_items(playlist_id=playlistIDs[key], count=None).items

    currentTimestamp = strftime(' %Y-%m-%dT%H%M%S', localtime())
    outputFileName = key + currentTimestamp + '.out'

    with open(outputFileName, 'w', encoding='utf8') as outfile:
      for video in playlistVideoItems:
        outfile.write(video.snippet.title + '\n')

