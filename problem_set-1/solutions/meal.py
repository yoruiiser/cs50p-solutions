def main():
    time = input("What's the time? ")
    final_time = convert(time)

    if 7 <= final_time <= 8:
        print("breakfast time")
    elif 12 <= final_time <= 13:
        print("lunch time")
    elif 18 <= final_time <= 19:
        print("dinner time")
    else:
        print("  ")


def convert(time):
    x, y = time.split(":")

    if " " in time:
        p, z = y.split(" ")
    else:
        p = y
        z = None

    x = float(x)
    p = float(p)

    if x == 12 and z == "a.m.":
        x = 0
    elif x == 12 and z == "p.m.":
        x = 12
    elif z == "p.m.":
        x += 12

    return x + p / 60


if __name__ == "__main__":
    main()

