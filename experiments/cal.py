from os import system




def makeEvent():
    system('say What description would you like for your event?')
    desc = input("What description would you like for your event?")

    system('say What summary would you like for your event?')
    summ = input("What description would you like for your event?")

    system('say Where will this event take place?')
    loc = input("Where will this event take place? ")

    cmd = """osascript -e'Tell application "Calendar"
         activate
         tell calendar "Home"
              set theCurrentDate to current date
              make new event at end with properties {description:"%s", summary:"%s", location:"%s", start date:theCurrentDate, end date:theCurrentDate +120 * Minutes}
         end tell
         reload calendars
    end Tell'

    """ % (desc, summ, loc)

    system(cmd)




system('say Hi, Did you say you wanted to make an event? ')
reply = input("Hi, Did you say you wanted to make an event?")

if reply == "yes":
    makeEvent()
else:
    system('say OK, maybe some other time then.')
