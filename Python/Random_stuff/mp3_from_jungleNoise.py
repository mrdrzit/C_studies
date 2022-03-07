import os
import requests as re

sourceA = [0] * 10
sourceB = [0] * 10
fileExt = '.mp3'

sourceA[0] = 'https://cdn.mynoise.net/Data/SUMATRA/0a'+fileExt
sourceB[0] = 'https://cdn.mynoise.net/Data/SUMATRA/0b'+fileExt
sourceA[1] = 'https://cdn.mynoise.net/Data/SUMATRA/1a'+fileExt
sourceB[1] = 'https://cdn.mynoise.net/Data/SUMATRA/1b'+fileExt
sourceA[2] = 'https://cdn.mynoise.net/Data/SUMATRA/2b'+fileExt
sourceB[2] = 'https://cdn.mynoise.net/Data/SUMATRA/2a'+fileExt
sourceA[3] = 'https://cdn.mynoise.net/Data/SUMATRA/3b'+fileExt
sourceB[3] = 'https://cdn.mynoise.net/Data/SUMATRA/3a'+fileExt
sourceA[4] = 'https://cdn.mynoise.net/Data/SUMATRA/4a'+fileExt
sourceB[4] = 'https://cdn.mynoise.net/Data/SUMATRA/4b'+fileExt
sourceA[5] = 'https://cdn.mynoise.net/Data/SUMATRA/5b'+fileExt
sourceB[5] = 'https://cdn.mynoise.net/Data/SUMATRA/5a'+fileExt
sourceA[6] = 'https://cdn.mynoise.net/Data/SUMATRA/6a'+fileExt
sourceB[6] = 'https://cdn.mynoise.net/Data/SUMATRA/6b'+fileExt
sourceA[7] = 'https://cdn.mynoise.net/Data/SUMATRA/7a'+fileExt
sourceB[7] = 'https://cdn.mynoise.net/Data/SUMATRA/7b'+fileExt
sourceA[8] = 'https://cdn.mynoise.net/Data/SUMATRA/8b'+fileExt
sourceB[8] = 'https://cdn.mynoise.net/Data/SUMATRA/8a'+fileExt
sourceA[9] = 'https://cdn.mynoise.net/Data/SUMATRA/9b'+fileExt
sourceB[9] = 'https://cdn.mynoise.net/Data/SUMATRA/9a'+fileExt

os.chdir('C:\\Users\\uzuna\\Desktop\\')

# doc = re.get(sourceB[4])
# with open('myfile.mp3', 'wb') as f:
#   f.write(doc.content)

with re.Session() as req:
  idx = 0
  musics = len(sourceB) + len(sourceA)

  for music in musics:
    if (idx > 9):
      print(f"Downloading File {music}")
      download = re.get(sourceA[idx])
      idx += 1
      if download.status_code == 200:
        with open("ambienceA_"+str(idx)+".mp3", 'wb') as f:
          f.write(download.content)
      else:
        print(f"Download Failed For File {music}")
    else:
      print(f"Downloading File {music}")
      download = re.get(sourceB[idx])
      idx += 1
      if download.status_code == 200:
        with open("ambienceA_"+str(idx)+".mp3", 'wb') as f:
          f.write(download.content)
      else:
        print(f"Download Failed For File {music}")
