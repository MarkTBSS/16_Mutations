string = "abracadabra"
print(string[5])
tupleEx = list(string)
print(tupleEx)
tupleEx[5] = 'k'
string = ''.join(tupleEx)
print(string)
print("====================")
string2 = "1234567890"
stringTemp = string2[:5]
print(string2)
print(stringTemp)
stringTemp += "k"
print(stringTemp)
stringTemp += string2[6:]
print(stringTemp)
print("====================")
string3 = "1234567890"
string3 = string3[:5] + "k" + string3[6:]
print(string3)