def main():
    x=input("WORD:?")
    print(shorten(x),sep="",end="")


def shorten(word):
               word=word.replace("A","").replace("E","").replace("I","").replace("O","").replace("U","").replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
               return word


if __name__ == "__main__":
    main()

