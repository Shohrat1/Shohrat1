program = {"hello":'salam',
        "appel":'alma',
        "dog": "kopek",
        "lemon":"limon",
        "cat":"pisik",
        "flag":"baydak",
        "student":"baydak",
        "family":"masgala",
        "pen":"rucka",
        'water':"suw",
        "bread":"corek"}

while True:
    print(''' *****My dictionary program*****
    1.Show
    2.add
    3.edit
    4.delete
    5.exit
    ''')

    a = int(input("birini sayla: "))
    if 1 == a:
        for i, j in program.items():
            print(i, '=' ,j)
    elif 2 == a:
        eng = input("english word: ")
        tkm = input("turkmnen word: ")
        program[eng] = tkm
        print("added")

    elif 3 == a:
        word = input("enter the word in english: ")
        wrod1 = input("enter the word in turkmen: ")
        program[word] = wrod1
        print("edited")

    elif 4 == a:
        soz =input("enter the word in english: ")
        del program [soz]
        print("deleted")
    
    elif 5 == a:
        print("thank you using program: ")
        break

    else:
        print("wrong command...")