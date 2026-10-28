months={
   "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
    }
while True:
    date=input("date?")
    try:
        x,y,z=date.split("/")
        y=int(y)
        x=int(x)
        z=int(z)
        if x>12 or y>31:
         continue
        else:
         break
    except ValueError:
      pass
    try:
        x,y,z=date.split(" ")
        y=y.strip(",")
        y=int(y)
        z=int(z)
        if "," not in date:
           raise ValueError
        elif x not in months or y>31:
            continue
        else:
            break
    except ValueError:
            pass
if x in months:
   print(f"{z}-{months[x]}-{y:02}",end="")
else:
   print(f"{z}-{x:02}-{y:02}",end="")


