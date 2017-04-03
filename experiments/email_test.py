
import sys, feedparser
from os import system
#Here, we import modules needed for this program
newEmail=""
USERNAME="sadf"
PASSWORD="asd"
PROTO="https://"
SERVER="mail.google.com"
PATH="/gmail/feed/atom"
#We assign variables with values. Fill in your username and password
def mail(checker):
    email = feedparser.parse("asd:asd@https://mail.google.com/mail/feed/atom")
    print (email['entries'][0])

#parses your account data and sends it to gmail
    if email > 0:
        newEmail = 1
    else:
        newEmail = 0
    #checks for mail

    if newEmail==1:
         system('say you got mail')

#plays sound if email present


mail(0)
