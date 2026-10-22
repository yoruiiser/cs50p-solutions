def convert(strut):
    return(strut.replace( ":)","🙂").replace(":(","🙁"))
def main():
    text=input("Drop your message")
    convert(text)
    print(convert(text))

main()

