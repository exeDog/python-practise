_hours = input('Enter number of hours')

try:
    _hours = int(_hours)
except:
    _hours = -1

def computePay(hours):
    if hours <= 40:
        return hours*10
    else:
        return (40*10)+((hours-40)*(1.5*10))

if _hours == -1 or _hours < 0:
    print('Invalid number')

else:
    print('Your pay is',computePay(_hours))