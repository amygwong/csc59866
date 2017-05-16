
#this file is what is executed and contains the loop

from os import system
from commands import commands
from actions import action
from speech_to_text import getUserInput
import time
import cal

#setting everything up for the loop
a = commands()
inp = ""
val = -1
startTime = time.time()



while True:
    sys_says = "Command me"
    inp = getUserInput(sys_says)

    while inp == "" or inp == -1:
        inp = getUserInput("Try Again")

    #handle quiting case
    if inp == "quit" or inp == "quick":
        break

    #handle the command classification
    val = a.getCommand(inp)
    print(val)
    #do the command
    sent = action(val,inp)
    if sent != "" and val != -1:
        a.comList[val].addCommand(sent)
        a.comList[val].writeToFile()

    if time.time()-startTime > 20:
        #do passive checking here
        print("Passive check now")
        cal.checkForEvents()

        #reset the clock
        startTime = time.time()


    cmd1 = """osascript -e'on is_running(appName)
    tell application "System Events" to (name of processes) contains appName
    end is_running


    set safRunning to is_running("iTunes")
    if safRunning then
    tell application "iTunes"
	try
		set whatshappening to (get player state as string)
	end try

	if whatshappening = "paused" then
		tell app "iTunes" to play
	end if

    end tell
    end if
    '

    """
    system(cmd1)

    input("Press Enter to Continue")

    cmd2 = """osascript -e'on is_running(appName)
    tell application "System Events" to (name of processes) contains appName
    end is_running


    set safRunning to is_running("iTunes")
    if safRunning then
    tell application "iTunes"
	try
		set whatshappening to (get player state as string)
	end try

	if whatshappening = "playing" then
		tell app "iTunes" to paused
	end if

    end tell
    end if'

    """
    system(cmd2)
