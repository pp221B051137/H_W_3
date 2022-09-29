from ast import pattern
import re
empty_=[]
# pattern = "r'[456]\d{15}'"
pattern = r'(^[456]{1}\d{3})(?! _)(-?)(\d{4})(?! _)(-?)(\d{4})(?! _)(-?)(\d{4})$'
# list_1 = ['4123456789123456','4123356789123456','5123356789123456','8123356789123456']
y = input()
# for y in list_1:
x = re.findall(pattern,y)
# print(x)
if x == empty_:
    print("Invalid")
else:
    print("Valid")