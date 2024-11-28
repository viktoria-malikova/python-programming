GAS_CONSTANT = 8.31446261815324 # moolinen kaasuvakio R (J/mol*K --> Pa*m^3/mol*K)

def main():
    n = int(input("What is the amount of substance of the gas (in moles)?\n")) #ainemäärä (mol)
    T_low = int(input("Enter a lower limit for the temperature (in Kelvins)?\n")) #lämpötilan alaraja (K)
    T_high = int(input("Enter a higher limit for the temperature (in Kelvins)?\n")) #lämpötilan yläraja (K)
    V_low = int(input("Enter a lower limit for the volume (in cubic metres)?\n")) #tilavuuden alaraja (m^3)
    V_high = int(input("Enter a higher limit for the volume (in cubic metres)?\n")) #tilavuuden yläraja (m^3)
    filename = input("Enter the name of the file where the table will be written:\n")
    try:
        file = open(filename, "w")
        #p * V = n * R * T
        #p = nRT / V (Pa)
        #p = (nRT / V) / 1000 (kPa)
        file.write("The pressure of {} moles of gas between {} - {} Kelvins and {} - {} cubic metres, "
                   "measured in kilopascals\n".format(n, T_low, T_high, V_low, V_high))
        file.write("{:>9s} |".format("p(T, V)"))
        for T in range(T_low, T_high+1, 10):
            file.write("{:>9d}".format(T))
        file.write("\n")
        kpl = int(((T_high - T_low) / 10) + 2)
        file.write("---------" * kpl + "--\n")
        for volume in range(V_low, V_high+1, 1):
            file.write("{:>9d} |".format(volume))
            for temperature in range(T_low, T_high+1, 10):
                p = (n * GAS_CONSTANT * temperature / volume) / 1000
                file.write("{:>9.2f}".format(p))
            file.write("\n")
        file.close()
        print("The table was written successfully.")
        print()
        print("The file", filename, "looks like this:")
        print()
        open_file = open(filename, "r")
        for line in open_file:
            line = line.rstrip()
            print(line)
    except OSError:
        print("Could not write to file.")
main()