import plistlib

def find_duplicates(fileName):
    plist = plistlib.readPlist(fileName)
    tracks = plist['Tracks']
    track_names = {}
    for trackId, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']

            if name in track_names:

                if duration//1000 == track_names[name][0]//1000:
                    count = track_names[name][1]
                    track_names[name] = (duration, count+1)

             else:
                 track_names[name] = (duration, 1)
        except:
            pass