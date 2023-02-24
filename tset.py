"""def square(x):
    return x*x


kare=[square(i) for i in range(1,11)]
tek_kare=[a for a in kare if a%2!=0]
print(kare)
print(tek_kare)"""
giriss= [[1, 2], [3, 4], [5, 6, 7]]

def terse(liste):
    liste=liste[::-1]
    liste=[i[::-1] for i in liste]
    return liste
print(terse(giriss))