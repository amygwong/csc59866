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



#Function for making events
def makeEvents(desc, summ, loc):

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


#Function for listing the start times of each event for the day
def listEvents():
    cmd = """osascript -e'property my_calendar : "Home"

    set my_date to (current date) -- or any other date you want

    copy my_date to Start_Date
    set time of Start_Date to 0
    copy my_date to End_Date
    set time of End_Date to 86399 -- 23:59:59 in seconds

    tell application "Calendar"
    tell calendar my_calendar
        -- read all events betwen start and end dates
        set my_List to (every event whose (start date is greater than or equal to Start_Date) and (start date is less than or equal to End_Date))

        repeat with myEvent in my_List -- loop through each event
            --do something
            log (start date of myEvent) as string
        end repeat
    end tell --Calendar
    end tell -- application'

    """

    system(cmd)

def listEvents2():
    cmd = """osascript -e'set {year:y, month:m, day:d, weekday:wd} to (current date)
set str to (wd as string) & ", " & (d as string) & " " & (m as string) & ", " & (y as string) & " 12:00:00 AM"
set today to date str
set tomorrow to today + 60 * 60 * 24

tell application "Calendar"
          tell calendar "Home"
                    set curr to every event whose start date is greater than or equal to today ¬
                              and start date is less than or equal to tomorrow
          end tell
end tell'

    """

    system(cmd)



'''
system('say Hi, Did you say you wanted to make an event? ')
reply = input("Hi, Did you say you wanted to make an event?")

if reply == "yes":
    makeEvent()
else:
    system('say OK, maybe some other time then.')
'''

listEvents2()
