
def removevowels(text):
    mylist=[x for x in text if x not in "aeiou"]
    return mylist
text=input("Enter the string:")
finallist=removevowels(text)
print(finallist)
