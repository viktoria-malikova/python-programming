SPECIFIC_HEAT_CAPACITY_ICE = 2.09 # ominaislämpökapasiteetti c jäälle, yksikkö kJ / (kg * °C)
SPECIFIC_HEAT_CAPACITY_WATER = 4.1819 # ominaislämpökapasiteetti c vedelle, yksikkö kJ / (kg * °C)
SPECIFIC_HEAT_OF_FUSION_WATER = 333 # ominaissulamislämpö s, yksikkö kJ / kg
SPECIFIC_HEAT_OF_VAPORIZATION_WATER = 2260 # ominaishöyrystymislämpö r, yksikkö kJ / kg

#Lämpöenergiaa, joka vaaditaan samassa olomuodossa pysyvän aineen, esim. kiinteän jääpalan tai nestemäisen veden,
# lämmittämiseen, kuvaa kaava Q = c * m * ΔT, missä Q on lämpöenergia, c on aineen ominaislämpökapasiteetti
# (vakio, annettu alempana sekä jäälle että vedelle), m on aineen massa ja ΔT lämpötilan muutos.

#Sulamislämpöä, joka vastaa aineen sulamiseen vaadittavaa energiaa, kuvaa kaava Q = s * m, missä Q on sulamislämpö,
# s on aineen ominaissulamislämpö (vakio, annettu alempana vedelle) ja m on aineen massa.

#Höyrystymislämpöä, joka vastaa aineen höyrystymiseen vaadittavaa energiaa, kuvaa samantapainen kaava Q = r * m, missä
# Q on hyörystymislämpö, r on aineen ominaishöyrystymislämpö (vakio, annettu alempana vedelle) ja m on aineen massa.


# Implement the function ice_cube_heating here
def ice_cube_heating(energy, mass, start_temp, end_temp):
    if start_temp >= 0:
        energia_tarvitaan = mass * SPECIFIC_HEAT_CAPACITY_WATER * (end_temp - start_temp)
    else:
        energia_tarvitaan = mass * SPECIFIC_HEAT_CAPACITY_ICE * (end_temp - start_temp)
        #energia, joka tarvitaan, että jää sulaa
    if energia_tarvitaan <= energy:
        jaa_energia = energy - energia_tarvitaan
        lampotila_lopussa = end_temp
    else:
        jaa_energia = 0.0
        if start_temp >= 0:
            lampotila_lopussa = start_temp + energy / (mass * SPECIFIC_HEAT_CAPACITY_WATER)
        else:
            lampotila_lopussa = start_temp + energy / (mass * SPECIFIC_HEAT_CAPACITY_ICE)
    return jaa_energia, lampotila_lopussa

# Implement the function ice_cube_melting here
def ice_cube_melting(energy, mass):
    energia_tarvitaan = mass * SPECIFIC_HEAT_OF_FUSION_WATER
    if energia_tarvitaan <= energy:
        energia_jaa = energy - energia_tarvitaan
        return energia_jaa, True
    else:
        return 0.0, False


# Implement the function ice_cube_vaporization here
def ice_cube_vaporization(energy, mass):
    energia_tarvitaan = mass * SPECIFIC_HEAT_OF_VAPORIZATION_WATER
    if energia_tarvitaan <= energy:
        energia_jaa = energy - energia_tarvitaan
        return energia_jaa, True
    else:
        return 0.0, False


def print_heating_result(energy_total, mass, temp_init, temp_end, melted, vaporized):
    print("With {:.2f} kJ, an ice cube weighing {:.2f} kg heats from {:.2f} °C to {:.2f} °C."
          .format(energy_total, mass, temp_init, temp_end))
    if not melted and not vaporized:
        print("The ice cube stays solid.")
    elif melted and not vaporized:
        print("The ice cube has melted into fluid water.")
    else:
        print("The ice cube has vaporized and is now water vapor.")

def main():
    print("Welcome to the ice cube simulator! I will tell you stats about heating your ice cube.")
    mass = float(input("What is the mass of the ice cube (in kg)?\n"))
    while mass <= 0.0:
        print("Mass cannot be zero or negative!")
        mass = float(input("What is the mass of the ice cube?\n"))
    temp_init = float(input("What is the initial temperature of the ice cube (in °C)?\n"))
    while temp_init < -273.15 or temp_init > 0.0:
        print("The ice cube's temperature can't be under the absolute zero or above 0 degrees!")
        temp_init = float(input("What is the initial temperature of the ice cube (in °C)?\n"))
    energy_total = float(input("What is the total energy used for heating the ice cube (in kJ)?\n"))
    while energy_total < 0.0:
        print("Energy cannot be negative!")
        energy_total = float(input("What is the total energy used for heating the ice cube (in kJ)?\n"))

    melted = False
    vaporized = False
    energy_remaining, end_temp = ice_cube_heating(energy_total, mass, temp_init, 0.0)
    if energy_remaining != 0.0:
        energy_remaining, melted = ice_cube_melting(energy_remaining, mass)
        if energy_remaining != 0.0:
            energy_remaining, end_temp = ice_cube_heating(energy_remaining, mass, 0.0, 100.0)
            if energy_remaining != 0.0:
                energy_remaining, vaporized = ice_cube_vaporization(energy_remaining, mass)

    print_heating_result(energy_total, mass, temp_init, end_temp, melted, vaporized)

main()