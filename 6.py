#Write a program to enter marks of 6 students and display them in 
#sorted order


print("enter percentage:")
nums = list(map(int, input().split()))
nums.sort()
nums.reverse()
print("after sorting percentage:")
print(*nums)