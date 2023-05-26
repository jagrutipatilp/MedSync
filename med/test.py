cr=""
f = open("dict.txt", "a")



for a in range(9):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                for e in range(9):
                    for f in range(9):
                        for g in range(9):
                            for h in range(9):
                                cr=a+b+c+d+e+f+g+h+"   "
                                print(cr)
                                f.write(cr)
f.close()
