"""Generate a text file containing the title of all the videos in a playlist.
"""

# External modules
from os import mkdir
from os.path import isdir, join
from pyyoutube import Api
from time import localtime, strftime

# Internal modules that are kept secret
import MyConfigurations

if __name__ == '__main__':
  api = Api(api_key=MyConfigurations.API_KEY)

  playlistIDs = MyConfigurations.PLAYLIST_IDS
  displayUploader = MyConfigurations.DISPLAY_UPLOADER

  if not isdir('output'):
    mkdir('output')

  # Remember to comment out the individual playlist keys from MyConfigurations if you don't want to loop through them all
  for key in playlistIDs:
    playlistVideoItems = api.get_playlist_items(playlist_id=playlistIDs[key], count=None).items

    currentTimestamp = strftime(' %Y-%m-%dT%H%M%S', localtime())
    outputFileName = key + currentTimestamp + '.out'
    outputFilePath = join('output', outputFileName)

    with open(outputFilePath, 'w', encoding='utf8') as outfile:
      for index, playlistVideo in enumerate(playlistVideoItems):

        try:
          video = api.get_video_by_id(video_id=playlistVideo.contentDetails.videoId).items[0]

          outfile.write(video.snippet.title + '\n')
          if displayUploader:
            outfile.write(f'{video.snippet.channelTitle}\n\n')

        except Exception as e:
          print(f'Exception occurred on "{playlistVideo.snippet.title}" within playlist {key} at index {index}: {e}')

