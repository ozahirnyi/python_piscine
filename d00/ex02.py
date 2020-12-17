import sys

if len(sys.argv) == 2:
    try:
        num = int(sys.argv[1])
        if num == 0:
            print("I'm Zero.")
        elif num % 2:
            print("I'm Odd.")
        else:
            print("I'm Even.")
    except:
        print("ERROR")
else:
    print("ERROR")
