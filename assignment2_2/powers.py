def main():
    
    rivi = input("Base number: ")
    a = int(rivi)
    rivi = input("Upper limit for the powers: ")
    limit = int(rivi)
    n = 1
    print("Powers: ")
    while a**n <= limit:
        print(a**n)
        n = n + 1
main()
