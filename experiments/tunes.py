from os import system

#Takes a song title as input and plays the song in itunes
def playTrack(song):
    cmd = """osascript -e'tell application "iTunes"
        play track "%s"
        end tell'

    """ % (song)
    system(cmd)

#Takes a song title as input and tries to play the song
#If song exists then it will be played in itunes
#Otherwise computer will tell user the song does not exist
def playTrack2(song):
    cmd = """osascript -e'tell application "iTunes"
    try
        play track "%s"
    on error the error_message number the error_number
        say "The Track you wish to play does not exist"
        -- display dialog "Error: " & the error_number & ". " & the error_message buttons {"Cancel"} default button 1
    end try
end tell'

    """ % (song)
    system(cmd)

#Takes a playlist title as input and plays the playlist in itunes according to the first song in that playlist
def playPlaylist(playlist):
    cmd = """osascript -e'tell application "iTunes"
        play playlist "%s"
        end tell'

    """ % (playlist)
    system(cmd)

#Takes a song title and playlist title as input and plays that particular song from that playlist in itunes
def playPlaylist2(song, playlist):
    cmd = """osascript -e'tell application "iTunes"
   play track "%s" of playlist "%s"
   end tell'

    """ % (song, playlist)
    system(cmd)

#Takes a playlist title as input and tries to play it
#If playlist exists then it will be played in itunes
#Otherwise computer will tell user the playlist does not exist
def playPlaylist3(playlist):
    cmd = """osascript -e'tell application "iTunes"
    try
        play playlist "%s"
    on error the error_message number the error_number
        say "The playlist you wish to play does not exist"
        -- display dialog "Error: " & the error_number & ". " & the error_message buttons {"Cancel"} default button 1
    end try
end tell'

    """ % (playlist)
    system(cmd)

#Takes a song title and playlist title as input and tries to play the song from the playlist
#If song exists then it will be played in itunes
#Otherwise computer will tell user the song does not exist
def playPlaylist4(song, playlist):
    cmd = """osascript -e'tell application "iTunes"
    try
        play track "%s" of playlist "%s"
    on error the error_message number the error_number
        say "The Track you wish to play does not exist"
        -- display dialog "Error: " & the error_number & ". " & the error_message buttons {"Cancel"} default button 1
    end try
end tell'

    """ % (song, playlist)
    system(cmd)

#Stops playing
def itunesStop():
    cmd = """osascript -e'tell app "iTunes" to stop'

    """
    system(cmd)

#Pauses song in itunes
def itunesPause():
    cmd = """osascript -e'tell app "iTunes" to pause'

    """
    system(cmd)

#Continues playing song in itunes
def itunesPlay():
    cmd = """osascript -e'tell app "iTunes" to play'

    """
    system(cmd)

#Plays next track
def itunesNext():
    cmd = """osascript -e'tell app "iTunes" to play next track'

    """
    system(cmd)

#Plays previous track
def itunesPrevious():
    cmd = """osascript -e'tell app "iTunes" to play previous track'

    """
    system(cmd)


#playPlaylist2("Dance with the Devil", "Recently Added")
playTrack2("Dance with the Devil")
#itunesPrevious()
