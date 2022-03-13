for a in range(1, 100):
    if (a % 3) == 0 and (a % 5) == 0:
        a = "Python UMS"
    elif(a % 3) == 0:
        a = "Python"
    elif(a % 5) == 0:
        a = "UMS"
    print(a)
