import re
import statistics

_fhandler = open('mbox-short.txt')
count = []
for line in _fhandler:
    line = line.rstrip()
    query = re.findall('^New .*: ([0-9]+)', line)
    if len(query) > 0:
        for number in query:
            count.append(float(number))

print(statistics.mean(count))