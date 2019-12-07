import urllib.request as ur
from bs4 import BeautifulSoup


_userinput = input('Enter the url')
if '.com' in _userinput:
    try:
        _urlhandler = ur.urlopen(_userinput).read()
    except:
        print('Unable to open URL')
        exit()

    soup = BeautifulSoup(_urlhandler,'html.parser')
    tags =  soup.find_all('a')
    for tag in tags:
        print(tag.next_sibling )

else:
    print('Incorrect URL')
    exit()

