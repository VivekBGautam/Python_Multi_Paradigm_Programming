def CheckPrime(ListData):
    Count = 0
    for i in range(2,ListData):
        if ListData % i == 0:
            Count += 1

    if Count == 0:
        return True
    else:
        return False