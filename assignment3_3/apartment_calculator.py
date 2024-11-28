def main():
    asunnon_hinta = int(input("How much does the apartment cost?\n"))
    palkka = int(input("How much is your initial monthly salary?\n"))
    palkka_prosentti = int(input("How many percent does your salary increase per year?\n"))
    saasto_prosentti = int(input("And how many percent of your salary will you save?\n"))
    saasto_nyt = int(input("How much savings do you have?\n"))
    while asunnon_hinta <= 0 or palkka <= 0 or 100 < palkka_prosentti < 0 or 100 < saasto_prosentti < 0 or not saasto_nyt >= 0:
        print("Enter only positive values and percentages between 0 - 100!")
        asunnon_hinta = int(input("How much does the apartment cost?\n"))
        palkka = int(input("How much is your initial monthly salary?\n"))
        palkka_prosentti = int(input("How many percent does your salary increase per year?\n"))
        saasto_prosentti = int(input("And how many percent of your salary will you save?\n"))
        saasto_nyt = int(input("How much savings do you have?\n"))
    asunnon_hinta_miinus_saasto = asunnon_hinta - saasto_nyt
    saasto = 0
    kuukaudet = 0
    vuodet = 0
    while saasto < asunnon_hinta_miinus_saasto:
        saasto = saasto + palkka*(saasto_prosentti/100)
        kuukaudet = kuukaudet + 1
        if kuukaudet % 12 == 0:
            vuodet = vuodet + 1
            palkka = palkka*((palkka_prosentti/100)+1)
        kk = kuukaudet%12
    print("You need", asunnon_hinta_miinus_saasto, "euros for the apartment.")
    if kuukaudet%12 == 0:
        print("It will take you exactly",vuodet, "years to save the money for the apartment.")
    else:
        print("It will take you",vuodet,"years and",kk,"months to save the money for the apartment.")
main()