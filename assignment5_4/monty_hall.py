import random

def initialize_doors(number_of_doors):
    ovien_lista = [False] * number_of_doors
    ovien_lista[random.randint(0, (number_of_doors - 1)] = True
    return ovien_lista

def remove_wrong_doors(chosen_door, doors):
    for i in doors == False:
        if doors.index("False") == chosen_door:
            return i+1
        else:
            return random.randint(0, len(doors)-2)
    return i

def print_doors(doors, dont_open):
    print(" _  " * len(list_of_doors))
    print("| | " * len(list_of_doors))
    print("|_| " * len(list_of_doors))
    for i in range(len(list_of_doors)):
        print("{:^3d} ".format(i), end="")


def main():
    seed = int(input("Set seed:\n"))
    random.seed(seed)

    ovien_lkm = int(input("How many doors?\n"))
    while ovien_lkm < 3 or ovien_lkm > 999:
        print("The number of doors must be between 3-999!")
        ovien_lkm = int(input("How many doors?\n"))
    list_of_doors = initialize_doors(ovien_lkm)
    print(" _  " * len(list_of_doors))
    print("| | " * len(list_of_doors))
    print("|_| " * len(list_of_doors))
    for i in range(len(list_of_doors)):
        print("{:^3d} ".format(i), end="")
    choose = int(input("Choose a door 1-{:d}.".format(ovien_lkm)))
    while choose < 1 or choose > ovien_lkm:
        choose = int(input("Choose a door 1-{:d}.".format(ovien_lkm)))
    print("You chose the door number {:d}".format(choose))
    print("...")
    x = remove_wrong_doors(choose, list_of_doors)
    y = print_doors(list_of_doors, )

main()