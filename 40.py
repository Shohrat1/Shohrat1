print()
dictionary = {
    "alma"  :  "8",
    "uzum" : "12" ,
    "hurma" : "18",
    "banan" : "25",
    "nar" : "15"
}
summa = []
harytlar = []
for i, j in dictionary.items():
   print(i, '-' ,j)  
while True:
    print()
    haryt = input("name almak isleyarsiniz: ").lower()
    if haryt in dictionary:
        massa = int(input("nace kg almak isleyarsiniz: "))
        x = int(dictionary[haryt]) * massa
        summa.append(x)
        harytlar
    elif haryt.lower() == "quit":
        break
    elif haryt not in dictionary:
        print(f"{haryt.capitalize()} bizde yok ")
print('siz',sum(summa),"manat tolemeli")