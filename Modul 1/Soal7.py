def faktorPrima(l):
    list = []
    loop = 2
    while loop <= l:
        if(l % loop) == 0:
            l /= loop
            list.append(loop)
        else:
            loop += 1
    return list


print(faktorPrima(10))
