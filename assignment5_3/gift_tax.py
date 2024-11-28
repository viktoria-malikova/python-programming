LOWER_LIMITS = [5000, 25000, 55000, 200000, 1000000]
TAX_PERCENTS_RELATIVES = [0.08, 0.10, 0.12, 0.15, 0.17]
TAX_AT_LOWER_LIMIT_RELATIVES = [100, 1700, 4700, 22100, 142100]
TAX_PERCENTS_OTHERS = [0.19, 0.25, 0.29, 0.31, 0.33]
TAX_AT_LOWER_LIMIT_OTHERS = [100, 3900, 11400, 53450, 301450]

def calculate_gift_tax(gift_value, relative):
    gift_value = int(gift_value/100)*100
    for i in range(len(LOWER_LIMITS)):
        if gift_value < LOWER_LIMITS[0] and relative == True:
            return 0.0
        elif gift_value < LOWER_LIMITS[0] and relative == False:
            return 0.0
        elif gift_value < LOWER_LIMITS[i] and relative == True:
            tax = TAX_AT_LOWER_LIMIT_RELATIVES[i-1] + (gift_value - LOWER_LIMITS[i-1]) * TAX_PERCENTS_RELATIVES[i-1]
            return tax
        elif gift_value < LOWER_LIMITS[i] and relative == False:
            tax = TAX_AT_LOWER_LIMIT_OTHERS[i-1] + (gift_value - LOWER_LIMITS[i-1]) * TAX_PERCENTS_OTHERS[i-1]
            return tax
        elif gift_value > LOWER_LIMITS[4] and relative== True:
            tax = TAX_AT_LOWER_LIMIT_RELATIVES[4] + (gift_value - LOWER_LIMITS[4]) * TAX_PERCENTS_RELATIVES[4]
            return tax
        elif gift_value > LOWER_LIMITS[4] and relative == False:
            tax = TAX_AT_LOWER_LIMIT_OTHERS[4] + (gift_value - LOWER_LIMITS[4]) * TAX_PERCENTS_OTHERS[4]
            return tax


def main():
    lahja = int(input("Enter the value of the gift:\n"))  # euroina
    sukulainen = input("Is the receiver a close relative (yes/no)?\n")
    if sukulainen == "yes":
        sukulainen = True
    elif sukulainen == "no":
        sukulainen = False
    vero = calculate_gift_tax(lahja, sukulainen)
    print("Gift tax is {:.2f} euros.".format(vero))
    if vero > 0:
        most_tax = int(input("How much gift tax are you willing to pay at most?\n"))
        if vero < most_tax:
            print("You can give the whole gift in one installment.")
        else:
            i = 1
            uusi_vero = vero
            while uusi_vero * i > most_tax:
                i += 1
                uusi_lahja = lahja // i
                uusi_vero = calculate_gift_tax(uusi_lahja, sukulainen)
            print("You would have to part the gift in {:d} parts ({:.2f} euros per part).".format(i, uusi_lahja))
            print("Tax would be {:.2f} euros per part and {:.2f} euros in total.".format(uusi_vero, uusi_vero*i))
            print("It would take you {:d} years to give away the whole gift.".format((i-1)*3))

main()