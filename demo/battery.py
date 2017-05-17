from os import system

# get the battery percentage remaining
def getBatteryPercentage():
    cmd = """ osascript -e 'set battStatus to do shell script "pmset -g ps"
    if battStatus contains "InternalBattery" then
        set {TID, text item delimiters} to {text item delimiters, ";"}
        set battStatus to text items of battStatus
        set text item delimiters to tab
        set battStatus to text 1 thru -2 of last text item of item 1 of battStatus as integer
        set text item delimiters to TID
        say "Battery power is at "
        say battStatus
        say "percent"
    end if
    '"""
    system(cmd)

# get where the computer power is being drawn from and the current battery percentage 
def getBatteryStatus():
    cmd = """ osascript -e 'set battStatus to do shell script "pmset -g ps"
    set ACpower to true
    if battStatus contains "Battery Power" then
        set ACpower to false
    end if
    if ACpower is true then
        say "Drawing power from AC Power"
    else
        say "Drawing power from Battery Power"
    end if
    if battStatus contains "InternalBattery" then
        set {TID, text item delimiters} to {text item delimiters, ";"}
        set battStatus to text items of battStatus
        set text item delimiters to tab
        set battStatus to text 1 thru -2 of last text item of item 1 of battStatus as integer
        set text item delimiters to TID
        say "Battery power is at "
        say battStatus
        say "percent"
    end if
    '"""
    system(cmd)

# notifies user if the battery percentage is less than a certain amount (11)
def checkBattery():
    cmd = """ osascript -e 'set lowBattery to 11
    set battStatus to do shell script "pmset -g ps"
    if battStatus contains "InternalBattery" then
        set {TID, text item delimiters} to {text item delimiters, ";"}
        set battStatus to text items of battStatus
        set text item delimiters to tab
        set battStatus to text 1 thru -2 of last text item of item 1 of battStatus as integer
        set text item delimiters to TID
        if battStatus is less than lowBattery then
            say "Low Battery"
            say battStatus
            say "percent left. Please connect to AC Power Adapter"
        end if
    end if
    '"""
    system(cmd)

#checkBattery()
#getBatteryPercentage()
#getBatteryStatus()
