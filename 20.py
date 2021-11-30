// write a program to calculate the grade of a student to the marks of following scheme

90-100 excellent
80-90   A
70-80   B
60-70   C
50-60   D
less than 50  fail


program:-

s1=int(input("enter the marks of first subject:"))
s2=int(input("enter the marks of second subject:"))
s3=int(input("enter the marks of third subject:"))
s4=int(input("enter the marks of fourth subject:"))
s5=int(input("enter the marks of fifth subject:"))
s6=int(input("enter the marks of sixth subject:"))

avg=(s1+s2+s3+s4+s5+s6)/6
if(avg>90 & avg<=100):
   print("excellent")
elif(avg>=80 & avg<90):
   print("grade A")
elif(avg>=60 & avg<70):
   print("grade B")
elif(avg>=60 & avg<70):
   print("grade c")
elif(avg>=50 & avg<60):
   print("grade D")
else:
   print("fail")