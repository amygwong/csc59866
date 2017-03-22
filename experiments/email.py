import objc
import applescript
'''
scpt = applescript.AppleScript("set interval to 7
set target to (current date) - interval
set oldCount to 0
tell application "Mail"
set box to mailbox named "INBOX" of account named "Your_mailbox_here"
set maxMessages to count of messages in box
repeat with index from 1 to maxMessages
set currentMessage to message index in box
set msgDate to date received of currentMessage
if msgDate is greater than target then
set oldCount to oldCount + 1
# do something here
end if
end repeat
end tell
")

scpt.run()
'''
scpt = applescript.AppleScript('''
    on run {arg1, arg2}
    say arg1 & " " & arg2
    end run
    
    on foo()
    return "bar"
    end foo
    
    on Baz(x, y)
    return x * y
    end bar
    ''')

print(scpt.run('Hello', 'World')) #-> None
print(scpt.call('foo')) #-> "bar"
print(scpt.call('Baz', 3, 5)) #-> 15
