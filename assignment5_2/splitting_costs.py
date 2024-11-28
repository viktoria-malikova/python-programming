def main():

    lkm = int(input("Enter the number of the participants.\n")) #osallistuja
    while lkm < 2:
        print("The number must be at least 2!")
        lkm = int(input("Enter the number of the participants.\n"))

    kustannukset = []
    i = 0
    while i < lkm:
        osuus = float(input("Enter the sum (eur) paid by participant no {:d}.\n".format(i+1)))
        kustannukset.append(osuus)
        i += 1

    #kustannukset = []
    #for i in range(lkm):
        #osuus = float(input("Enter the sum (eur) paid by participant no {:d}.\n".format(i+1)))
        #kustannukset.append(osuus)

    summa = 0.0
    for arvo in kustannukset:
        summa += arvo
    print("Total costs are {:.2f} eur.".format(summa))

    keskiarvo = summa / lkm
    i = 0

    #for muuttuja in kustannukset:
    while i < lkm:
        if kustannukset[i] >= keskiarvo:
            erotus = kustannukset[i] - keskiarvo
            print("Participant no {:d} should receive {:.2f} eur.".format(i+1, erotus))
        else:
            erotus = keskiarvo - kustannukset[i]
            print("Participant no {:d} should pay {:.2f} eur.".format(i+1, erotus))
        i += 1
main()



