def main():

    filename = input("Enter the name of the file with the molar masses:\n")
    try:
        file = open(filename, "r")
        sanakirja = {}
        rivi = 0
        for line in file:
            rivi += 1
            line = line.rstrip()
            try:
                osat = line.split(":")
                if len(osat) != 2:
                    print("Invalid line: '{}'".format(line))
                    rivi -= 1
                else:
                    aine = osat[0]
                    try:
                        moolimassa = float(osat[1])
                        if aine not in sanakirja:
                            sanakirja[aine] = moolimassa
                        else:
                            print("A molar mass for {} has already been saved in the dictionary ({:.3f} g/mol)."
                                  .format(aine, sanakirja[aine]))
                            vastaus = input("Should it be replaced by the value {:.3F} g/mol (y/n)?\n".format(moolimassa))
                            if vastaus == "y":
                                sanakirja[aine] = moolimassa
                                rivi -= 1
                            else:
                                rivi -= 1
                    except ValueError:
                        print("Invalid molar mass on line: '{}'".format(line))
                        rivi -= 1
            except ValueError:
                print("Invalid line: '{}'".format(line))
                rivi -= 1
        file.close()
        print("Molar masses of", rivi, "substances were successfully read from the file.")
        print()
        aine = input("Enter the chemical formula of the substance. Stop by entering an empty line.\n")
        while aine != "":
            if aine not in sanakirja:
                print("A molar mass for '{}' could not be found in the file.".format(aine))
                print()
                aine = input("Enter the chemical formula of the substance. Stop by entering an empty line.\n")
            else:
                muuttuja = True
                massa = input("Enter the mass of the substance (in grams):\n")
                while muuttuja:
                    try:
                        m = float(massa)
                        if m < 0:
                            print("The mass needs to be positive or zero!")
                            massa = input("Enter the mass of the substance (in grams):\n")
                        else:
                            n = m / sanakirja[aine]
                            print("{:.3f} grams of {} is equal to {:.3f} moles.".format(m, aine, n))
                            print()
                            aine = input("Enter the chemical formula of the substance. Stop by entering an empty line.\n")
                            muuttuja = False
                    except ValueError:
                            print("The mass needs to be a number!")
                            massa = input("Enter the mass of the substance (in grams):\n")
    except OSError:
        print("File could not be read.")
    print("Program terminating.")
main()