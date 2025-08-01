while True:
    n=input()
    if n=="EXIT":
        exit()
    elif not n.isdigit():
        print("Invalid input")
    else:
        grade=float(n)
        if grade>100 or grade<0:
            print("Invalid input")
        elif grade<40:
            print("F")
        elif grade<60:
            print("D")
        elif grade<75:
            print("C")
        elif grade<90:
            print("B")
        else:
            print("A")