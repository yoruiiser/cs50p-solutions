
grocery = {}

while True:
    try:
        item = input().upper()
    except KeyError:
        pass
    except EOFError:
        break

    grocery[item] = grocery.get(item, 0) + 1

for item in sorted(grocery):
    print(grocery[item], item)

