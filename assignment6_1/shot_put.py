def main():

    print("Enter the lengths of the throws (m) separated by commas.")
    results = input()
    if results == "":
        print("No accepted results.")
    else:
        luvut = results.split(",")
        lukulista = []
        for luku in luvut:
            lukuja = float(luku)
            lukulista.append(lukuja)
        best_result = 0.0
        for arvo in lukulista:
            if arvo > best_result:
                best_result = arvo
        print("The best result is {:.2f} m.".format(best_result))

main()