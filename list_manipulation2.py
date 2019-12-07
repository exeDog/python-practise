_userArray = list()
while True:
    _userinput = input('Please enter a number. Type "Done" when finished')
    if _userinput == 'Done':
        break
    try:
        _userinput = float(_userinput)
    except:
        print('You entered a invalid number')
        continue
    _userArray.append(_userinput)

print('The largest number is ',max(_userArray))

print('The smallest number is ',min(_userArray))