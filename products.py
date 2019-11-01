f = open('PRODUCTS.txt', 'r')
lines = f.readlines()
PCode = ['' for i in range(int(len(lines) / 3))]
PDescription = ['' for i in range(int(len(lines) / 3))]
PRetailPrice = ['' for i in range(int(len(lines) / 3))]
C = 0
D = 1
R = 2
for i in range(int(len(lines) / 3)):
    PCode[i] = lines[C].strip()
    PDescription[i] = lines[D].strip()
    PRetailPrice[i] = float(lines[R].strip())
    C += 3
    D += 3
    R += 3
f.close()
    
    
PCode1 = ['' for i in range(int(len(lines) / 3))]
PDescription1 = ['' for i in range(int(len(lines) / 3))]
PRetailPrice1 = ['' for i in range(int(len(lines) / 3))]
f = open('PRODUCTS2.txt', 'r')
lines = f.readlines()
f.close()
for String in range(len(lines)):
    SpaceNum = 0
    for Char in range(len(lines[String])):
        if lines[String][Char] == ' ':
            SpaceNum += 1
            if SpaceNum == 1:
                PCode1[String] = lines[String][:Char]
                FirstSpace = Char
            elif SpaceNum == 2:
                PDescription1[String] = lines[String][FirstSpace + 1:Char]
                PRetailPrice1[String] = float(lines[String][Char + 1:].strip())
                break


def ProductCodeSearch(SearchCode):
    for ThisIndex in range(len(PCode)):
        if PCode[ThisIndex] == SearchCode:
            return ThisIndex
    return -1