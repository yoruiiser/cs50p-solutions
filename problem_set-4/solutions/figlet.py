from pyfiglet import Figlet
from random import choice
from sys  import argv
from sys import exit
figlet=Figlet()
if len(argv)==1 or len(argv)==3:
    if len(argv)==1:
       s=input("INPUT:")
       figlet.setFont(font=choice(figlet.getFonts()))
       print(figlet.renderText(s))
    elif len(argv)==3:
        if argv[1] not in ["-f","--font"] or argv[2] not in figlet.getFonts():
            exit("Invalid Usage")
        else:
            s=input("INPUT:")
            figlet.setFont(font=argv[2])
            print(figlet.renderText(s))
else:
    exit("Invalid Usage")



