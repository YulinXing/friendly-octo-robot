def SearchFile(Name):
    FileHandle = open('StudentContact.txt', 'r')
    for Line in FileHandle.readlines():
        if Line[:len(Name)] == Name:
            FileHandle.close()
            return Line
    FileHandle.close()
    return ''


def AddToFile(Info, Name):
    Num = 0
    FileHandle = open('ClassContact.txt','a')
    if Info == '':
        Num += 1
        FileHandle.write(Name + '*No Number')
    else:
        FileHandle.write(Info)
    FileHandle.close()
    return Num

def ProcessArray():
    FileHandle = open('ClassContact.txt', 'w')
    FileHandle.close()
    ClassList = open('ClassList.txt', 'r')
    for Name in ClassList.readlines():
        Info = SearchFile(Name.strip())
        Num = AddToFile(Info, Name.strip())
    return len(ClassList.readlines()) - Num


print(ProcessArray())