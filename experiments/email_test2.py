import urllib

FEED_URL = 'https://mail.google.com/mail/feed/atom'

def get_unread_msgs(user, passwd):
    auth_handler = urllib.HTTPBasicAuthHandler()
    auth_handler.add_password(
        realm='New mail feed',
        uri='https://mail.google.com',
        user='{user}@gmail.com'.format(user=user),
        passwd=passwd
    )
    opener = urllib.build_opener(auth_handler)
    urllib.install_opener(opener)
    feed = urllib.request.urlopen(FEED_URL)
    return feed.read()

##########
user = "asdasd"
passwd = "asda"

print (get_unread_msgs(user, passwd))
