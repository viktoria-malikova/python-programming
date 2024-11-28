def main():
    lasten_lkm = int(input("How many heights will be entered?\n"))
    while lasten_lkm <= 0:
        print("Enter a positive value!")
        lasten_lkm = int(input("How many heights will be entered?\n"))
    print("Enter the heights of the children on separate lines.")
    yli_140_lkm = 0
    alle_140_lkm = 0
    for i in range(lasten_lkm):
        lasten_pituus = int(input())
        if lasten_pituus >= 140:
            yli_140_lkm += 1
        if lasten_pituus < 140:
            alle_140_lkm += 1
    print("There are", lasten_lkm, "children.")
    print(yli_140_lkm, "of the children are allowed and", alle_140_lkm, "are not allowed on the roller coaster.")
main()

