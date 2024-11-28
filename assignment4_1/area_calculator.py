def calculate_and_print(muoto, pohja, korkeus):
    if muoto == "r":
        pinta_ala = pohja * korkeus
    if muoto == "t":
        pinta_ala = (pohja * korkeus) / 2
    print("The area is", pinta_ala, "square meters.")


def main():
    print("Choose a shape:")
    print("r - rectangle")
    print("t - triangle")
    shape = input()
    base = float(input("Enter the length of the base (m):\n"))
    height = float(input("Enter the height (m):\n"))
    calculate_and_print(shape, base, height)

main()