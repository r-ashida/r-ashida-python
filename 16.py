#Write a program to find out whether a student is pass or fail, if it 
#requires total 40% and at least 33% in each subject to pass. Assume 
#3 subjects and take marks as an input from the user.

s1=int(input("enter the marks of first subject:"))
s2=int(input("enter the marks of second subject:"))
s3=int(input("enter the marks of third subject:"))

avg=(s1+s2+s3+s4+s5+s6)/6
if(avg>40 & s1>33 &s2>33 &s3>33):
   print("pass")
else:
   print("fail")