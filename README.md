# CSC59866: Capstone 
Computer Assistance System For Visually Challenged 
By: Shawn Mathew, Anthony Tan and Amy Wong

NOTE: To see the number of commits made by each member, please click on commits link underneath the <> Code tab. Do not look at the Graphs tab.

**Running Locally**
Make sure you have the latest Git and Python(3.6+) version installed!

`$ git clone https://github.com/amygwong/csc59866.git`

Create and use a virtual environment:
```
$ pyvenv venv
$ source venv/bin/activate
(venv) $
```
Once you are in the virutal environment, go into the cloned folder and install the required programs.
```
(venv)$ cd csc59866
(venv)$ pip install -r requirements.txt
```
To deactivate the virtual environment:
```
(venv) $ deactivate
$
```
To run the program:
```
(venv) $ cd demo
(venv) $ python3 demo.py
```
The list of commands is shown below, but can also be found in `/demo/commandsVal.txt`.

```
Universal open and close applications: This can be done for any application that is located in the application folder. Example: Open Mail
Calendar: Create and List/Read Events
Folder: Create, Delete
Preview: Find and open file (image/document/pdf)
Mail: Sync, Create and Send Draft, Read New Mail
System: Log Out, Restart and Shutdown Computer
Volume Control: Up, Down
Safari: Close, Move, and Select Tabs, Copy Url to Clipboard
iTunes: Play Song
Get Information: Time, Date, Battery Percentage and Status
Find Gender of Voice: This command has a 50% accuracy rate in identifying the gender of the user based on the voice input.
```
