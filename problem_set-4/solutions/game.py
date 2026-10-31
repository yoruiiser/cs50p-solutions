import random
import sys
while True:
    try:
        x=input("level?")
        x=int(x)
        if x>0:
            break
    except ValueError:
        pass
y=random.randint(1,x)
while True:
    try:
        z=input("guess?")
        z=int(z)
        if z>0:
            break
    except ValueError:
        pass
while z!=y:
    try:
        if y>z:
           print("Too small!")
        elif z>y:
           print("Too large!")
        z=input("guess?")
        z=int(z)
    except ValueError:
     pass
if z==y:
    print("Just right!")
    sys.exit()
