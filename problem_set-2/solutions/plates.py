
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    def length(s):
        if len(s) > 1 and len(s) < 7:
            return True
        else:
            return False


    def letters(s):
        if s[0:2].isalpha():
            return True
        else:
            return False



    def middle(s):
        digit=False
        for i in s:
            if i.isdigit():
                digit=True
            elif digit:
                return False
        return True


    def firstdigit(s):
        for i in s:
            if i.isdigit():
                if i=="0":
                 return False
                else:
                    return True
       
        return True



    def punctuation(s):
        for i in s:
            if not i.isalnum():
                return False
        return True



    if length(s) and letters(s) and middle(s) and punctuation(s) and firstdigit(s):
        return True
    else:
        return False


main()

