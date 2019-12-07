str = 'X-DSPAM-Confidence: 0.8475'
_integer = str.find(' ')
print(_integer)
newStr = str[_integer+1:50]
newStr = float(newStr)
print(type(newStr),newStr)
