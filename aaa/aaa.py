print("*** NUMBRIDEGA MANGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage taisarv => ")))) #добавил 2 скобки
        break
    except ValueError:
         print("See ei ole taisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole motlet midagi peale hakata")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Maarake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a #убрал=
    paaris=0 #убрал=
    paaritu=0
    while b > 0:#:
            if b % 2 == 0:#2 =
                    paaris += 1 #+=
            else:
                    paaritu += 1 #+=
            b = b // 10 #убрал пробел
    print("Paarisarvud:", paaris) #,
    print("Paaritud nubmrid:", paaritu) #,
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Tagurda* sisestatud nubmer") #,
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #убрал пробел
    print("*Umberpooratud nubmer", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hupoteesi testmine") #лишняя скобка
    print()
    if c % 2 == 0:
        print("с - Paaris arv. Jagame 2. ")
    else:
        print("с - Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")
    while c != 1:
            if c % 2 == 0: #=
                c == c / 2
            else:
                c == (3*c + 1) / 2
            print(c, end=" ") #"
    print()
    print("Hupotees on oige")
