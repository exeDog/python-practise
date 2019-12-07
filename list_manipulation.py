_fhandler = open('romeo.txt').read().split()
_wordslist = list()
for word in _fhandler:
    if word not in _wordslist:
        _wordslist.append(word)
_wordslist.sort()
print('wordlist',_wordslist)
