import math

def calculate_cost(consumption, distance, gas_price, rent, time):
    vuokra = rent * math.ceil(time)
    bensa = distance/100 * gas_price * consumption
    kustannukset = vuokra + bensa
    return kustannukset

def main():

    bensan_hinta = float(input("How much does gas cost (per litre)?\n")) #euroa/l
    ison_vuokrahinta = float(input("Enter the hourly rent for the big van:\n")) #euro
    ison_vuokra_aika = float(input("Enter the estimated rental time (hours) for the big van:\n")) #h
    ison_etaisyys = float(input("Enter estimated driving distance (km) for the big van:\n")) #km
    ison_kulutus = float(input("Enter fuel consumption (litres / 100 km) for the big van:\n")) #l/100 km
    ison_kustannukset = calculate_cost(ison_kulutus, ison_etaisyys, bensan_hinta, ison_vuokrahinta, ison_vuokra_aika)

    pienin_vuokrahinta = float(input("Enter the hourly rent for the small van:\n")) #euro
    pienin_vuokra_aika = float(input("Enter the estimated rental time (hours) for the small van:\n")) #h
    pienin_etaisyys = float(input("Enter estimated driving distance (km) for the small van:\n")) #km
    pienin_kulutus = float(input("Enter fuel consumption (litres / 100 km) for the small van:\n")) #l/100 km
    pienin_kustannukset = calculate_cost(pienin_kulutus, pienin_etaisyys, bensan_hinta, \
                                         pienin_vuokrahinta, pienin_vuokra_aika)

    print("Renting the bigger van would cost {:.2f} euros and renting the smaller van would cost {:.2f} euros." \
          .format(ison_kustannukset, pienin_kustannukset))

    if ison_kustannukset < pienin_kustannukset:
        print("You should rent the big van.")
    elif ison_kustannukset == pienin_kustannukset:
        print("You should rent the big van.")
    else:
        print("You should rent the small van")

main()