string_1 = "Ugani"
string_2 = "skrito stevilo"

skrito_stevilo = 9
poskus = 0

while poskus != skrito_stevilo:
    poskus = int(raw_input("Zdravo, %s %s(0 < skrito ? < 12): " %(string_1, string_2)))

    if poskus == skrito_stevilo:
        print "Bravo, Uganil si! Nase skrito stevilo je 9!"
        break

    else:
        print "Izbrano stevilo " + str(poskus) + " ni nase skrito stevilo. Poskusi znova!:)"
