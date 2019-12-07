_fhandler = open('mbox-short.txt')
domains = dict()
for line in _fhandler:
    if line.startswith('From'):
        line = line.split()
        if len(line) >= 2:
            emails = line[1]
            charpos = emails.find('@')
            emails = emails[charpos:]
            domains[emails] = domains.get(emails,0)+1

print(domains)
