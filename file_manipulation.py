filename = input('Enter the file name')
import statistics
if filename=='na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punkd')
    exit()
try:
    _fhandler = open(filename)
except:
    print('Unable to open file',filename)
    exit()

_numbersArray = []

for line in _fhandler:
    if line.strip().startswith('X-DSPAM-Confidence'):
        line = line.split(':')
        _numbersArray.append(float(line[1]))
print('The avg of these numbers are',statistics.mean(_numbersArray))