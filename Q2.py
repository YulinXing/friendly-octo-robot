import random


def GetTemp():
    return random.uniform(0, 100)


def CheckSensor():
    LowTemp = 20
    HighTemp = 50
    while True:
        ID = float(input('ID:'))
        if 1 <= ID <= 10 and ID == int(ID):
            break
    Temp = GetTemp()
    print('Temp: ', Temp)
    if Temp >= HighTemp:
        print('Alarm')
    elif Temp <= LowTemp:
        print('Cold')
    else:
        print('Normal')


CheckSensor()