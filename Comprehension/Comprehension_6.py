n = int(input("How many strings you want to enter:"))
final=[]
while(n!=0):
    text=input("Enter the string:")
    final.append(text)
    n=n-1
intlist=[x for x in final if x in "123456790" ]
print(intlist)