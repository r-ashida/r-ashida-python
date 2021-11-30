#Write a program to detect double spaces in a string
# Check for spaces in string
import re

str = "how  are you"
print("The original string is : " + test_str)
res = bool(re.search(r"\s", test_str))
print("Does string contain spaces ? " + str(res))