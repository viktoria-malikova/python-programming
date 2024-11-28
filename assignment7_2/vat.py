def main():
    filename = input("Enter the name of the file containing selling prices.\n")
    try:
        file = open(filename, "r")
        print("    Price       VAT    Price (incl. VAT)")
        summa_ALV = 0.0
        luku = None
        for line in file:
            line = line.rstrip()
            luku = False
            try:
                alk_hinta = float(line) #alkuperäisen hinta ilman arvonlisäveroa
                ALV = alk_hinta * 0.24 #arvonlisävero
                summa_ALV += ALV
                kok_hinta = alk_hinta + ALV #kokonaishinta ALV:n kanssa
                print("{:9.2f} {:9.2f} {:9.2f}".format(alk_hinta, ALV, kok_hinta))
                luku = True
            except ValueError:
                print("Incorrect line in file {:s}. Closing program.".format(filename))
                break
        if luku == True or luku == None:
            print("------------------------------------------")
            print("Total VAT {:.2f} eur.".format(summa_ALV))
        file.close()
    except OSError:
        print("Error in reading file {:s}. Closing program.".format(filename))
main()

#^