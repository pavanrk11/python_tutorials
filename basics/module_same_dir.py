name = "Pavan"

def f0():

    s = "I love India"

    def f1():
        nonlocal s
        s = "Me too"
        # print(s)

    def f2():
        nonlocal s
        s = "Me too 1"
        # print(s)


    f1()
    f2()
    # print(s)

f0()


