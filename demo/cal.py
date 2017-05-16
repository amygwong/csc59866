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

def listAllEvents():
    cmd = """osascript -e'set my_date to (current date) -- or any other date you want

    copy my_date to Start_Date
    set time of Start_Date to 0
    copy my_date to End_Date
    set time of End_Date to 86399 -- 23:59:59 in seconds


tell application "Calendar"
   set the_calendar to calendar "Home"
   set {start_dates, the_summaries} to {start date, summary} of (every event of the_calendar whose (start date is greater than or equal to Start_Date) and (start date is less than or equal to End_Date))
end tell
set c to count start_dates
set text_list to {}
repeat with i from 1 to c
   set this_date to item i of start_dates
   set this_summary to item i of the_summaries
   set end of text_list to "Event " & i & " starts at " & (time string of this_date) & linefeed & linefeed & "Summary for this event is " & this_summary & linefeed & linefeed
end repeat
set the_text to text_list as string
set text_text2 to "You have " & c & " events for today."
say text_text2
say the_text
'


    """

    system(cmd)
