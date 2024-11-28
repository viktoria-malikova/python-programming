def main():

    filename = input("Enter the name of the file containing the recipe:\n")
    try:
        file = open(filename, "r")

        for line in file:
            line = line.rstrip()
            rivilista = line.split()
            print("This recipe of", rivilista[0], "makes", rivilista[1])

        annokset = 0
        annos = False
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

        for line in rivilista:
            try:
                massa = float(rivilista[0])
                uusi_massa = massa * annokset
                teksti = " ".join(rivilista[1:len(rivilista)])
                print(round(uusi_massa, 1), teksti)
            except ValueError:
                print(line)
        file.close()

    except OSError:
        print("File could not be read. Terminating program.".format(filename))
main()