def gambarPersegiEmpat(t, l):
    for i in range(t):
        if i == 0 or i == t-1:
            print('@'*l)
        else:
            print('@' + ' '*(l-2) + '@')


print(gambarPersegiEmpat(5, 4))
