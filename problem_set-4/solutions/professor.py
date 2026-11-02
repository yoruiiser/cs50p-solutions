import random


def main():
  score=0
  x=get_level()
  for i in range(10):
      p=3
      a=generate_integer(x)
      b=generate_integer(x)
      try:
       ans=int(input(f"{a} + {b} = "))
      except ValueError:
         ans=-1
      if ans==a+b:
          score=score+1
          continue
      while ans!=a+b and p>0:
         print("EEE")
         p=p-1
         if p>0:
          try:
           ans=int(input(f"{a} + {b} = "))
           if ans==a+b:
            score=score+1
          except ValueError:
             ans=-1
      if p==0:
       print(f"{a} + {b} = {a+b}")
  print()
  print(score)




def get_level():
  while True:
      try:
         lvl=int(input("Level:"))
         if lvl in[1,2,3]:
           return lvl
      except ValueError:
            pass


def generate_integer(level):
    if  level==int(1):
        return random.randint(0,9)
    elif level==int(2):
        return random.randint(10,99)
    elif level==int(3):
        return random.randint(100,999)
    else:
        raise ValueError



if __name__ == "__main__":
    main()
