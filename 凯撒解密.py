def caesar_encrypt(realtext, step):
    outText = []
    cryptText = []


    bigletter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    smalletter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for eachletter in realtext:
        if eachletter in bigletter:
            index = bigletter.index(eachletter)
            crypting = (index - step) % 26
            cryptText.append(crypting)
            newletter = bigletter[crypting]
            outText.append(newletter)
        elif eachletter in smalletter:
            index = smalletter.index(eachletter)
            crypting = (index - step) % 26
            cryptText.append(crypting)
            newletter = smalletter[crypting]
            outText.append(newletter)
    return outText

print("欢迎使用凯撒解密系统")
a = input("请输入需要解密的内容")
b = int(input("请输入约定的解密位数"))
code = caesar_encrypt(a,b)
print("".join(code))


input("Press <Enter>")