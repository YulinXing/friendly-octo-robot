Decdata = int(input("请输入一个十进制数据："))
num = int(input("请输入一个进制n:"))

def DecConversion(dec,n):
    result = ''
    
    if dec:
        result = DecConversion(dec // n,n)
        return result + str(dec % n)
    else:
        return result

print(DecConversion(Decdata,num))
