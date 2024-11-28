def main():
    filename = input("Enter the name of the file containing the recipe:\n")
    try:
        file = open(filename, "r")
        line1 = file.readline().rstrip()
        line2 = file.readline().rstrip()
        print("This recipe of", line1, end=" ")
        print("makes", line2, end=".\n")
        osa = line2.split()
        kerroin = float(osa[0])
        annos = False
        annokset = 0
        while annos == False:
            try:
                servings = int(input("How many servings do you want to make with this recipe?\n"))
                if servings > 0:
                    annokset += servings
                    annos = True
                else:
                    print("The amount needs to be positive!")
            except ValueError:
                print("The amount needs to be an integer!")
        print()
        print("For", annokset, "servings of", line1, "you will need:")
        file.readline()
        for line in file:
            line = line.rstrip()
            osat = line.split()
            try:
                massa = float(osat[0])
                uusi_massa = massa/kerroin * annokset
                teksti = " ".join(osat[1:len(osat)])
                print(round(uusi_massa, 1), teksti)
            except ValueError:
                print(line)
        file.close()
    except OSError:
        print("File could not be read. Terminating program.".format(filename))
main()