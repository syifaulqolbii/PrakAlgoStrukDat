data = [2, 3, 5]
for k in range(2, 1000):
    if k in data:
        print(k)
    elif (k % 2) == 1:
        if (k % 3) != 0:
            if(k % 5) != 0:
                print(k)
