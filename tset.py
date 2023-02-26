import string

metin = "cats AND*Dogs-are Awesome?"

yeniMetin = ""
for i in metin:
    if i not in string.punctuation:
        yeniMetin += i
yeniMetin1=yeniMetin.capitalize()
yeniMetin1=yeniMetin1.replace(" ","")
#print(yeniMetin1)

a=["a,c,c","v,f,f,s"]
print(len(a))
