def main():
    x = float(input("Enter the wavelength of the electromagnetic radiation in metres:\n"))
    if x <= 0 or x > 1*10**8:
        print("The wavelength doesn't correspond to any type of radiation.")
    elif x <= 10*10**(-12):
        print("The radiation is gamma radiation.")
        print("The radiation is highly dangerous!")
    elif 0.01*10**(-9) < x <= 10*10**(-9):
        print("The radiation is X-radiation.")
    elif 10*10**(-9) < x <= 400*10**(-9):
        print("The radiation is ultraviolet radiation.")
    elif 400*10**(-9) < x <= 700*10**(-9):
        print("The radiation is visible light.")
        if 400*10**(-9) < x <= 450*10**(-9):
            print("The light is violet.")
        elif 450*10**(-9) < x <= 490*10**(-9):
            print("The light is blue.")
        elif 490*10**(-9) < x <= 560*10**(-9):
            print("The light is green.")
        elif 560*10**(-9) < x <= 590*10**(-9):
            print("The light is yellow.")
        elif 590*10**(-9) < x <= 630*10**(-9):
            print("The light is orange.")
        elif 630*10**(-9) < x <= 700*10**(-9):
            print("The light is red.")
    elif 700*10**(-9) < x <= 1*10**(-3):
        print("The radiation is infrared light.")
    elif 1*10**(-3) < x <= 1:
        print("The radiation is microwaves.")
    else:
        print("The radiation is radio waves.")
main()