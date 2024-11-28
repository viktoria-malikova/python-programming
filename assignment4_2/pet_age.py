# Implement the function dog_age_in_human_years here
def dog_age_in_human_years(dog_age):
    if 0 <= dog_age <= 1:
        ika = dog_age * 15
    elif 1 < dog_age <= 2:
        ika = 15 + (dog_age - 1) * 9
    elif dog_age > 2:
        ika = 15 + 9 + (dog_age - 2) * 5
    print("Your dog is {:.1f} years old in human years!".format(ika))

# Implement the function cat_age_in_human_years here
def cat_age_in_human_years(cat_age):
    if 0 <= cat_age <= 1:
        ika = cat_age * 15
    elif 1 < cat_age <= 2:
        ika = 15 + (cat_age - 1) * 10
    elif cat_age > 2:
        ika = 15 + 10 + (cat_age - 2) * 4
    print("Your cat is {:.1f} years old in human years!".format(ika))

# Implement the function bunny_age_in_human_years here
def bunny_age_in_human_years(bunny_age):
    if 0 <= bunny_age <= 0.5:
        ika = bunny_age * 32
    elif 0.5 < bunny_age <= 1:
        ika = 16 + (bunny_age - 0.5) * 10
    elif bunny_age > 1:
        ika = 16 + 5 + (bunny_age - 1) * 6
    print("Your bunny is {:.1f} years old in human years!".format(ika))

def main():
    print("Welcome to the pet age calculator! I will tell your pet's age in human years.")
    choice = 0
    while not 1 <= choice <= 3:
        print("Choose a pet:\n"
              "1: dog\n"
              "2: cat\n"
              "3: bunny")
        choice = int(input())
    age = float(input("How old is your pet?\n"))
    if choice == 1:
        dog_age_in_human_years(age)
    elif choice == 2:
        cat_age_in_human_years(age)
    else:
        bunny_age_in_human_years(age)

main()