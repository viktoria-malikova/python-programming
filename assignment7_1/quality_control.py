def main():
    filename = input("Enter the name of the file to be read:\n")
    try:
        product_file = open(filename,'r')
        total = 0
        optimal = 0
        allowed = 0
        faulty = 0
        for line in product_file:
            line = line.rstrip()
            measure = float(line)
            if 4.52 <= measure <= 4.58:
                optimal += 1
                total += 1
            elif 4.50 <= measure <= 4.60:
                allowed += 1
                total += 1
            else:
                faulty += 1
                total += 1
        product_file.close()
        print("File read successfully.")
        optimal_pros = optimal/total * 100
        allowed_pros = allowed/total * 100
        fail = faulty/total * 100
        print("The batch contained:")
        print("{:d} optimal ({:.1f}%) \n"
              "{:d} allowed ({:.1f}%) \n"
              "{:d} faulty ({:.1f}%).".format(optimal, optimal_pros, allowed, allowed_pros, faulty, fail))
        if fail >= 3:
            print("The batch didn't pass the quality inspection.")
        else:
            print("The batch passed the quality inspection.")
    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))
    except ValueError:
        print("Incorrect number in the file '{:s}'. Program ends.".format(filename))
main()