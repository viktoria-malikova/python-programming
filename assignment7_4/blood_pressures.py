SYSTOLIC_LIMITS = [0, 100, 120, 130, 140, 160, 180]
DIASTOLIC_LIMITS = [0, 60, 80, 85, 90, 100, 110]
BLOOD_PRESSURE_DESCRIPTIONS = ['low', 'optimal', 'normal', 'high normal',
                               'grade 1 hypertension', 'grade 2 hypertension', 'grade 3 hypertension']

def blood_pressure(list):
    if list[0] < SYSTOLIC_LIMITS[1] and list[1] < DIASTOLIC_LIMITS[1]:
        return BLOOD_PRESSURE_DESCRIPTIONS[0]
    elif list[0] >= SYSTOLIC_LIMITS[6] or list[1] >= DIASTOLIC_LIMITS[6]:
        return BLOOD_PRESSURE_DESCRIPTIONS[6]
    else:
        i = 0
        while list[0] >= SYSTOLIC_LIMITS[i] or list[1] >= DIASTOLIC_LIMITS[i]:
            i += 1
        return BLOOD_PRESSURE_DESCRIPTIONS[i-1]

def prosentti_osuus(x, y): #potilaiden määrä, kelvollisia datapisteitä
    prosentti = x / y * 100
    jakauma = round(prosentti / 5)
    return prosentti, jakauma


def main():
    filename = input("Enter the name of the data file:\n")
    try:
        file = open(filename, "r")
        low = 0
        optimal = 0
        normal = 0
        high_normal = 0
        grade_1_hypertension = 0
        grade_2_hypertension = 0
        grade_3_hypertension = 0
        rivi = 0
        luku = 0
        kpl = 0
        for line in file:
            rivi += 1
            luku += 1
            line = line.rstrip()
            osat = line.split("/")
            if len(osat) != 2:
                print("Invalid line # {}: {}".format(luku, line))
                rivi -= 1
            else:
                try:
                    ylapaine = int(osat[0])
                    alapaine = int(osat[1])
                    if 250 < ylapaine or alapaine <= 0:
                        kpl += 1
                        rivi -= 1
                    elif ylapaine <= alapaine:
                        print("Invalid line # {}: {}".format(luku, line))
                        rivi -= 1
                    else:
                        lista = [ylapaine, alapaine] #yhden potilaan ylä-/alapaine
                        pressure = blood_pressure(lista)
                        if pressure == 'low':
                            low += 1
                        elif pressure == 'optimal':
                            optimal += 1
                        elif pressure == 'normal':
                            normal += 1
                        elif pressure == 'high normal':
                            high_normal += 1
                        elif pressure == 'grade 1 hypertension':
                            grade_1_hypertension += 1
                        elif pressure == 'grade 2 hypertension':
                            grade_2_hypertension += 1
                        else:
                            grade_3_hypertension += 1
                except ValueError:
                    print("Invalid line # {}: {}".format(luku, line))
                    rivi -= 1
        if kpl > 0:
            print("Removed", kpl, "measurements from data.")
        if rivi <= 0:
            print()
            print("Not enough valid data.")
        else:
            print()
            print(rivi, "valid data points read.")
            print("Blood pressure distribution among the patients:")
            p, a = prosentti_osuus(low, rivi) #prosentuaalinen osuus, jakauma
            print("{:25s} | {:20s} ({:.0f}%)".format(BLOOD_PRESSURE_DESCRIPTIONS[0], "#" * a, p))
            r, b = prosentti_osuus(optimal, rivi) #prosentuaalinen osuus, jakauma
            print("{:25s} | {:20s} ({:.0f}%)".format(BLOOD_PRESSURE_DESCRIPTIONS[1], "#" * b, r))
            o, c = prosentti_osuus(normal, rivi) #prosentuaalinen osuus, jakauma
            print("{:25s} | {:20s} ({:.0f}%)".format(BLOOD_PRESSURE_DESCRIPTIONS[2], "#" * c, o))
            s, x = prosentti_osuus( high_normal, rivi) #prosentuaalinen osuus, jakauma
            print("{:25s} | {:20s} ({:.0f}%)".format(BLOOD_PRESSURE_DESCRIPTIONS[3], "#" * x, s))
            e, y = prosentti_osuus(grade_1_hypertension, rivi) #prosentuaalinen osuus, jakauma
            print("{:25s} | {:20s} ({:.0f}%)".format(BLOOD_PRESSURE_DESCRIPTIONS[4], "#" * y, e))
            n, z = prosentti_osuus(grade_2_hypertension, rivi) #prosentuaalinen osuus, jakauma
            print("{:25s} | {:20s} ({:.0f}%)".format(BLOOD_PRESSURE_DESCRIPTIONS[5], "#" * z, n))
            t, w = prosentti_osuus(grade_3_hypertension, rivi) #prosentuaalinen osuus, jakauma
            print("{:25s} | {:20s} ({:.0f}%)".format(BLOOD_PRESSURE_DESCRIPTIONS[6], "#" * w, t))
            high_blood = grade_1_hypertension + grade_2_hypertension + grade_3_hypertension
            high_blood_prosentti = high_blood / rivi * 100
            if high_blood != 0:
                print("{:d} ({:.0f}%) of the patients have high blood pressure!"
                      .format(high_blood, high_blood_prosentti))
            if low != 0:
                print("{:d} ({:.0f}%) of the patients have low blood pressure!".format(low, p))
            file.close()
    except OSError:
        print("Error in reading the file.")
main()