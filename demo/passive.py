from os import system

# System command to shut down without confirmation
def checkUpdates():

    cmd = """osascript -e'tell application "System Events" to tell (first application process whose ¬
frontmost is true) to set returnValue to title of ((first menu item whose title ¬
begins with "App Store") of menu "Apple" of menu bar 1)
display notification returnValue
'
    """
    system(cmd)
