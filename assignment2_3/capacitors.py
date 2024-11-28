def main():
    rivi = input("How many capacitors are there? \n")
    capacitors = int(rivi)
    while capacitors < 1:
        print("Enter a positive value!")
        rivi = input("How many capacitors are there? \n")
        capacitors = int(rivi)
    rivi = input("Are the capacitors connected: \n1. in series \n2. in parallel? \n")
    connected = int(rivi)
    while connected !=1 and connected !=2:
        print("Invalid choice!")
        connected = int(input("Are the capacitors connected: \n1. in series \n2. in parallel? \n"))
    i = 0
    result = 0.0
    while i < capacitors:
        c = float(input("Enter the capacitance for the next capacitor: "))
        if connected == 1:
            result = result + 1/c
        if connected == 2:
            result = result + c
        i = i + 1
    if connected == 1:
        result = 1/result
    print("The total capacitance of the capacitors is", result ,"F.")
main()
