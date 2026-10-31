import inflect
p=inflect.engine()
names=[]
while True:
    try:
        x=input("NAME:")
        names.append(x)
    except EOFError:
       break
print("\nAdieu, adieu, to",p.join(names),sep=" ",end="")

