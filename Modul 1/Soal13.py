angka = {1: "satu ", 2: "dua ", 3: "tiga ", 4: "empat ", 5: "lima ",
         6: "enam ", 7: "tujuh ", 8: "delapan ", 9: "sembilan "}
b = "puluh "
c = "ratus "
d = "ribu "
e = "juta "
f = "milyar "
g = "triliun"


def katakan(k):
    y = str(k)
    n = len(y)
    if n <= 3:
        if n == 1:
            if y == "0":
                return ""
            else:
                return angka[int(y)]
        elif n == 2:
            if y[0] == "1":
                if y[1] == "1":
                    return "sebelas"
                elif y[0] == "0":
                    k = y[1]
                    return katakan(k)
                elif y[1] == "0":
                    return "sepuluh"
                else:
                    return angka[int(y[1])] + "belas"
            elif y[0] == "0":
                k = y[1]
                return katakan(k)
            else:
                k = y[1]
                return angka[int(y[0])] + b + katakan(k)
        else:
            if y[0] == "1":
                k = y[1:]
                return "seratus " + katakan(k)
            elif y[0] == "0":
                k = y[1:]
                return katakan(k)
            else:
                k = y[1:]
                return angka[int(y[0])] + c + katakan(k)
    elif 3 < n <= 6:
        p = y[-3:]
        q = y[:-3]
        if q == "1":
            return "seribu " + katakan(p)
        elif q == "000":
            return katakan(p)
        else:
            return katakan(q) + d + katakan(p)
    elif 6 < n <= 9:
        r = y[-6:]
        s = y[:-6]
        return katakan(s) + e + katakan(r)
    elif 9 < n <= 12:
        t = y[-9:]
        u = y[:-9]
        return katakan(u) + f + katakan(t)
    else:
        v = y[-12:]
        w = y[:-12]
        return katakan(w) + g + katakan(v)


print(katakan(100000))
