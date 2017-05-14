from os import system

# close tabs to to the left
def safariCloseLeft():

    cmd = """osascript -e'tell application "Safari" to tell window 1 to close (tabs where index ≤ (get index of current tab))'
    """
    system(cmd)

# close tabs to to the right
def safariCloseLeft():

    cmd = """osascript -e'tell application "Safari" to tell window 1 to close (tabs where index ≥ (get index of current tab))'
    """
    system(cmd)

# copies url to clipboard
def safariCopyUrl():

    cmd = """osascript -e'tell application "Safari" to set u to URL of document 1
        set the clipboard to u'
    """
    system(cmd)

# selects the first tab in Safari
def safariFirstTab():

    cmd = """osascript -e'tell window 1 of application "Safari" to set current tab to tab 1'
    """
    system(cmd)


# selects the last tab in Safari
def safariLastTab():

    cmd = """osascript -e'tell window 1 of application "Safari" to set current tab to tab -1'
    """
    system(cmd)

# select the tab to the left
def safariMoveLeft():

    cmd = """osascript -e'tell application "Safari" to tell window 1 to set current tab to tab ((get index of current tab) - 1)'
    """
    system(cmd)

# select the tab to the right
def safariMoveRight():

    cmd = """osascript -e'tell application "Safari" to tell window 1 to set current tab to tab ((get index of current tab) + 1)'
    """
    system(cmd)




safariFirstTab()
