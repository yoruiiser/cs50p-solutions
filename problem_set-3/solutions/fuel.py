while True:
    try:
        f=input("fraction?")
        x,y=f.split("/")
        x=int(x)
        y=int(y)
        if x<0 or y<0 or x>y:
            raise ValueError
        else:
            pass
        percentage=int(x)/int(y)*int(100)

    except (ValueError,ZeroDivisionError):
       pass
    else:
       break


def fuel(p):
    if p>=int(99):
     print("F")
    elif p<=int(1):
     print("E")
    else:
      p=round(p,ndigits=None)
      print(p,"%",sep="", end="")



fuel(percentage)

