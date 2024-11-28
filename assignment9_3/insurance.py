class Insurance:

    def __init__(self, owner_name, original_premium, given_deductible, cap):
        self.__name = owner_name
        self.__bonus = 0.0
        if original_premium < 0:
            self.__premium = 0.0
        else:
            self.__premium = original_premium
        if given_deductible < 0:
            self.__deductible = 150.0
        else:
            self.__deductible = given_deductible
        self.__total_compensations = 0.0
        if cap <= 0:
            self.__total_compensation_cap = 15000.0
        else:
            self.__total_compensation_cap = cap
        self.__valid = True

    def get_name(self):
        return self.__name
    #Palauttaa vakuutuksen omistajan nimen.

    def get_bonus(self):
        return self.__bonus
    #Palauttaa vakuutuksen bonusprosentin.

    def get_premium(self):
        return self.__premium
    #Palauttaa vakuutuksen perusmaksun.

    def get_deductible(self):
        return self.__deductible
    #Palauttaa vakuutuksen omavastuun.

    def get_total_compensations(self):
        return self.__total_compensations
    #Palauttaa vakuutuksen perusteella maksettujen korvausten summan.

    def get_total_compensation_cap(self):
        return self.__total_compensation_cap
    #Palauttaa maksimikorvaussumman eli vakuutuksen perusteella maksettavien kaikkein korvausten summan ylärajan.

    def is_valid(self):
        return self.__valid
    #Palauttaa True, jos vakuutus on voimassa, ja muuten False.

    def set_premium(self, new_premium):
        if new_premium < 0:
             self.__premium = self.__premium
        else:
            self.__premium = new_premium
    #Muuttaa vakuutuksen perusmaksuksi parametrina (desimaaliluku) annetun arvon.

    def set_deductible(self, new_deductible):
        if new_deductible < 0:
            self.__deductible = self.__deductible
        else:
            self.__deductible = new_deductible
    #Muuttaa vakuutuksen omavastuuksia parametrina annetun arvon.

    def increase_bonus(self, increase):
        if increase < 0:
            self.__bonus = self.__bonus
        else:
            lisays = self.__bonus + increase
            if lisays > 70:
                self.__bonus = 70.0
            else:
                self.__bonus += increase
    #Kasvattaa bonusta parametrina (desimaaliluku) annetulla määrällä prosenttiyksiköitä.

    def decrease_bonus(self, decrease):
        if decrease <= 0:
            self.__bonus = self.__bonus
        else:
            self.__bonus -= decrease
            if self.__bonus < 0:
                self.__bonus = 0.0
    #Pienentää bonusta parametrina (desimaaliluku) annetulla määrällä prosenttiyksiköitä.

    def set_invalid(self):
        self.__valid = False
    #Asettaa vakuutuksen olevan pois voimasta.

    def set_valid(self):
        self.__valid = True
    #Asettaa vakuutuksen olevan voimassa.

    def calculate_real_premium(self):
        tot_vuosimaksu = self.__premium - self.__premium * (self.__bonus / 100)
        return tot_vuosimaksu
    #Laskee ja palauttaa todellisen vuosimaksun, kun bonus on otettu huomioon
    #eli perusmaksusta on vähennetty bonuksen mukainen alennus.

    def calculate_compensation(self, damage):
        if self.__valid == True:
            korvaus = damage - self.__deductible #vahinko - omavastuu
            if korvaus > 0:
                compensation = self.__total_compensation_cap - self.__total_compensations 
                if korvaus <= compensation:
                    compensation = korvaus
                    self.__total_compensations += compensation
                    self.decrease_bonus(10)
                else:
                    if compensation > 0:
                        self.__total_compensations += compensation
                        self.decrease_bonus(10) 
                    else:
                        compensation = 0.0
            else:
                compensation = 0.0
        else:
            compensation = 0.0
        return compensation
    #Laskee ja palauttaa vakuutuksen omistajalle kuuluvan korvauksen.

    def __str__(self):
        info = "Owner: {}, premium {} eur / year, bonus {} %.\n".format(self.__name, self.__premium, self.__bonus)
        info += "Deductible {} eur, total compensation cap {} eur.\n".format(self.__deductible, self.__total_compensation_cap)
        info += "Total compensations currently {} eur.\n".format(self.__total_compensations)
        if self.__valid == True:
            info += "Insurance policy is valid."
        else:
            info += "Insurance policy is not valid."
        return info
    #Palauttaa merkkijonon.