inpt=input("Enter the String:")
mylist=[x.upper() for x in inpt if x not in "aeiou"]
print(mylist)