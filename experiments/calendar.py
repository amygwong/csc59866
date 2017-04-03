#!/usr/bin/env python
#sleepy-mac.py
#makes my mac very sleepy

import os
cmd = """osascript -e'Tell application "Calendar"
     activate
     tell calendar "Home"
          set theCurrentDate to current date
          make new event at end with properties {description:"Event 1", summary:"First Event", location:"CCNY", start date:theCurrentDate, end date:theCurrentDate +120 * Minutes}
     end tell
     reload calendars
end Tell'






"""
def stupidtrick():
     os.system(cmd)
stupidtrick()
