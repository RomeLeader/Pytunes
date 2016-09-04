import plistlib
#import numpy as np

def get_artists(libraryFile):
    library = plistlib.readPlist(libraryFile)
    tracks = library['Tracks']
    artists = {}
    for ID, track in tracks.items():
        try:
            name = track['Name']
            artist = track['Artist']
            if artist in artists:
                count = artists[artist][1]
                artists[artist] = (artist, count+1)
            else:
                artists[artist] = (artist, 1)
        except:
            pass

    artist_count = []
    for k, v in artists.items():
        if v[1] > 1:
            artist_count.append((v[1]), k)

    f = open("artists.txt", 'w')
    for val in artist_count:
        f.write("[%d] %s\n" % (val[0], val[1]))
    f.close()

get_artists('pybrary.xml')

