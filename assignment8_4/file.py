def mine_grid(matrix):
    print("-" * (len(matrix[0]) * 2) + "---")
    for rivi in matrix:
        print("| ", end="")
        for alkio in rivi:
            print("{} ".format(alkio), end="")
        print("|")
    print("-" * (len(matrix[0]) * 2) + "---")


def star_area(matriisi):
    tahti_matriisi = list(matriisi)
    for rivi in tahti_matriisi:
        for i in range(
                len(rivi)):  # i => alkio rivissa
            if rivi[i] == 1:
                rivi[i] = "*"
    return tahti_matriisi


def mine_area(star_matrix):
    miina_matriisi = list(star_matrix)
    for i in range(len(miina_matriisi)):
        for j in range(len(miina_matriisi[0])):
            if miina_matriisi[i][j] == 0:
                numero = 0
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if (ii > -1 and jj > -1) and (ii <= len(miina_matriisi) - 1 and jj <= len(miina_matriisi) - 1) \
                                and miina_matriisi[ii][jj] == "*":
                            numero += 1
                miina_matriisi[i][j] = numero

    return miina_matriisi


def complete_grid(mine_matrix):
    print("-" * (len(mine_matrix[0]) * 2) + "---")
    for rivi in mine_matrix:
        print("| ", end="")
        for luku in rivi:
            print("{} ".format(luku), end="")
        print("|")
    print("-" * (len(mine_matrix[0]) * 2) + "---")


def main():
    filename = input("Enter the name of the file with the locations of the mines:\n")
    try:
        file = open(filename, "r")
        rivi = 0
        mines = 0
        matriisi = []
        try:
            line = file.readlines()
            line = line.rstrip()
            osat = line.split()
            lukulista = []
            for osa in osat:
                try:
                    luku = int(osa)
                    if luku != 1 and luku != 0:
                        print("Invalid integer '{}' on line: {}".format(luku, line))
                        print("Program terminating.")
                        return False
                    else:
                        lukulista.append(luku)
                        if luku == 1:
                            mines += 1
                except ValueError:
                    print("Invalid value '{}' on line: {}".format(osa, line))
                    print("Program terminating.")
                    return False
            matriisi.append(lukulista)

            print("This {:d}x{:d} grid has {:d} mines.".format(len(matriisi[0]), rivi, mines))
            print("Mine grid:")
            mine_grid(matriisi)
            print()
            tahtikenta = star_area(matriisi)
            miinakenta = mine_area(tahtikenta)
            print("Complete grid:")
            complete_grid(miinakenta)
        except OSError:
            print("Program terminating.")
        file.close()
    except OSError:
        print("File could not be read.")
        print("Program terminating.")


main()