
def main(x):
    i = 1
    sum1 = 0
    sum2 = 0
    j = x - 1

    while (i <= x):
        if (x%i == 0):
            sum1 = sum1 + 1
        i = i + 1

    while (j >= 1):
        i = 1
        while (i <= j):
            if (j%i == 0):
                sum2 = sum2 + 1
            i = i + 1
        if (sum2 >= sum1):
            return("not anti-prime")
            j = 0
            i = j + 1
        else:
            j = j - 1
            sum2 = 0
    if (sum1 > sum2):
        return("anti-prime")

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
    import sys
    x = int(sys.argv[1])

    print(main(x))

