import time

counter = 1


while (counter <= 100):
    a = str(counter / 3)
    b = str(counter / 4)
    if '.0' in a:
        astrip = int(str(a).rstrip('.0'))
    else:
        astrip = a
    if '.0' in b:
        bstrip = int(str(b).rstrip('.0'))
    else:
        bstrip = b
    acheck = isinstance(astrip, int)
    bcheck = isinstance(bstrip, int)
    counter = counter + 1
    if (acheck == True) and (bcheck == True):
        print('BANG!')
        time.sleep(1)
    elif (acheck == False) and (bcheck == True):
        print('NG')
        time.sleep(1)
    elif (acheck == True) and (bcheck == False):
        print('BA')
        time.sleep(1)
    elif (acheck == False) and (bcheck == False):
        print(counter - 1)
        time.sleep(1)
