#!usr/bin/python3

def exo16():
    val = 0
    count = []
    while True:
        val = val + 1
        for i in range(1, 10):
            if val % i == 0:
                count.append(1)

        if (len(count) >= 9):
             print(val)
             break
        count = []

exo16()
