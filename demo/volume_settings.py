import speech_recognition as sr
from os import system

r = sr.Recognizer()
m = sr.Microphone()

# get volume which is between 0 and 100
def getVolume():
    return system("""osascript -e 'output volume of (get volume settings)'""")

# set volume between 0 and 100
def setVolume(value):
    if int(value) > 100 or int(value) < 0:
        return -1, "Volume should be between 0 and 100. Try Again"
    else:
        cmd = """osascript -e 'set volume output volume "%s"' """ % (value)
        system(cmd)
        return 1

def increaseVolume():
    value = getVolume()
    value += 10
    if value > 100:
        value = 100
    cmd = """osascript -e 'set volume output volume "%s"' """ % (value)
    system(cmd)

def decreaseVolume():
    value = getVolume()
    value -= 10
    if value < 0:
        value = 0
    cmd = """osascript -e 'set volume output volume "%s"' """ % (value)
    system(cmd)

def setFullVolume():
    system("""osascript -e 'set volume output volume "100"' """)

# returns True if volume is muted, false otherwise
def getMuteState():
    return system("""osascript -e 'output muted of (get volume settings)'""")

# set volume to be mute or unmute
def setMuteState(value):
    if value == "true":
        return system("""osascript -e 'set volume output muted true'""")
    else:
        return system("""osascript -e 'set volume output muted false'""")

# menu of volume choices
def volumeChoices(value):
    if value == "get volume":
        system('say ' + str(getVolume()))
    elif value == "set volume":
        setVolume(getUserInput("Change to what volume number between 0 and 100"))
    elif value == "get mute state":
        system('say ' + str(getMuteState()))
    elif value == "set mute state":
        setMuteState(getUserInput("Change mute state to true or false"))
    else:
        print("Command does not exist")

def getUserInput(input):
    system('say ' + input)
    with m as source: audio = r.listen(source)
    try:
        value = r.recognize_google(audio)
        print("You said {}".format(value))
        return value
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")

# testing
'''
print(setVolume("30"))
print(getVolume())
increaseVolume()
decreaseVolume()
print(getVolume())
setFullVolume()
print(getVolume())
    print(setVolume("30"))
    print(setVolume("130"))
    print(getVolume())
    print(getMuteState())
    setMuteState("true")
    print(getMuteState())
    setMuteState("false")
    print(getMuteState())
'''
'''
try:
    cont = True
    while cont:
        value = getUserInput("Command me")
        volumeChoices(value)
        if value == "no":
            cont = False
except KeyboardInterrupt:
    pass
'''
