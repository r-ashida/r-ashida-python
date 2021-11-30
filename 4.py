#Replace double spaces with single spaces in previous program

mystring = 'hello   how   are you'

correctedstring = " ".join(mystring.split())
print(correctedstring)