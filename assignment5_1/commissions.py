def main():

    days = int(input("How many sales will you input?\n"))
    sales = [0.0] * days #lista = sales
    for i in range(days):
        sales_day = float(input("Enter the next amount.\n"))
        sales[i] = sales_day

    print("Commissions")

    LIMIT = 300             # euros
    NORMAL_COMMISSION = 7.5 # %
    BONUS_COMMISSION = 14   # %

    commissions = []
    for x in sales:
        if x >= LIMIT:
            commission = x * BONUS_COMMISSION / 100
            commissions.append(commission)
        elif 0 < x < LIMIT:
            commission = x * NORMAL_COMMISSION / 100
            commissions.append(commission)
        else:
            commission = 0
            commissions.append(commission)

    summa = 0.0
    for arvo in commissions:
        print("{:.2f} eur".format(arvo))
        summa += arvo

    print("Total commissions {:.2f} eur.".format(summa))

main()