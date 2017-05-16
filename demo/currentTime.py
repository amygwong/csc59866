from os import system

# Get and say the current date in format: Day of the Week, Month, Day, Year
def getDate():
    cmd = """ osascript -e 'set myDate to date string of (current date)
	say myDate
    '"""
    system(cmd)

# Get and say the current time in format: HH:MM AM/PM
def getTime():
    cmd = """ osascript -e 'set myTime to time string of (current date)
	say myTime
    '"""
    system(cmd)

#getDate()
#getTime()