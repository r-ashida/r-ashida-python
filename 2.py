#Write a program to fill in a letter template given below with name 
#and date: 
#letter = ‘’’ Dear <|Name|>
 #You are selected
 #<|Date|>’’’

import datetime
name=input("Enter Your Name: ")
date = 4
letter = f''' Dear {name} You are selected  {datetime.date.today()} '''
print(letter)