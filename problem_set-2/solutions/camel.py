ccase=input("camel case?")
for i in ccase:
   if i.isupper():
       print("_",i.lower(),sep="", end="")
   else:
    print(i,sep="", end="")

