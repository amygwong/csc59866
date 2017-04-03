#!/usr/bin/env python

from imapclient import IMAPClient
from os import system
import time



DEBUG = True

HOSTNAME = 'imap.gmail.com'
USERNAME = 'asdas'
PASSWORD = 'adsad'
MAILBOX = 'Inbox'

NEWMAIL_OFFSET = 1   # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 60 # check mail every 60 seconds


def loop():
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)

    if DEBUG:
        print('Logging in as ' + USERNAME)
        select_info = server.select_folder(MAILBOX)
        print('%d messages in INBOX' % select_info['EXISTS'])

    folder_status = server.folder_status(MAILBOX, 'UNSEEN')
    newmails = int(folder_status['UNSEEN'])

    if DEBUG:
        print ("You have") + newmails + ("new emails!")

    if newmails > NEWMAIL_OFFSET:
        system('say You have new mail.')
    else:
        system('say You do not have new mail.')

    time.sleep(MAIL_CHECK_FREQ)

loop()
