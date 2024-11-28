def main():
    first_number = int(input("Enter the first number to be printed.\n"))
    while first_number <= 0:
        print("Enter a positive number!")
        first_number = int(input("Enter the first number to be printed.\n"))
    last_number = int(input("Enter the last number to be printed.\n"))
    while last_number == first_number or last_number < first_number:
        print("Enter a number that is larger than the first number!")
        last_number = int(input("Enter the last number to be printed.\n"))

##Jos luku on jaollinen vain kolmosella, ohjelman pitää tulostaa luvun sijasta merkkijono "hocus".
#Jos luku on jaollinen vain viitosella, ohjelman pitää tulostaa luvun sijasta merkkijono "pocus".
#Jos luku on jaollinen sekä kolmosella että viitosella, ohjelman pitää tulostaa luvun sijasta merkkijono "HOCUS POCUS!".
    print("Hocus pocus between {:d} - {:d}:".format(first_number, last_number))
    for i in range(first_number, last_number+1):
        if i % 3 == 0 and i % 5 == 0:
            print("HOCUS POCUS!")
        elif i % 3 == 0:
            print("hocus")
        elif i % 5 == 0:
            print("pocus")
        else:
            print(i)
main()

