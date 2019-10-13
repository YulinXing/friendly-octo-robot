def EggsIntoBoxes(Num):
    return Num // 6, Num % 6


NumberOfBoxes, EggsLeftOver = EggsIntoBoxes(13)
print(NumberOfBoxes, EggsLeftOver)