array = [1,78,356,57,350,76856]
newarray = []
i = 1
while i < 6:
    newvalue = input('Please enter a number')
    try:
        newvalue = int(newvalue)
    except:
        print('Incorrect value')
        continue
    newarray.append(newvalue)
    i=i+1

def largest():
    return max(newarray)

print('The largest number is',largest())