# Y1 AUTUMN 2020
# Basic Course in Programming Y1
# Author: Anni Niskanen
# Template for Exercise 9.5


import random


class PlayerCharacter:

    ABILITIES = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

    SKILLS_TO_ABILITIES = {"Acrobatics" : "Dexterity", "Animal Handling" : "Wisdom", "Arcana" : "Intelligence",
                           "Athletics" : "Strength", "Deception" : "Charisma", "History" : "Intelligence",
                           "Insight" : "Wisdom", "Intimidation" : "Charisma", "Investigation" : "Intelligence",
                           "Medicine" : "Wisdom", "Nature" : "Intelligence", "Perception" : "Wisdom",
                           "Performance" : "Charisma", "Persuasion" : "Charisma", "Religion" : "Intelligence",
                           "Sleight of Hand" : "Dexterity", "Stealth" : "Dexterity", "Survival" : "Wisdom"}

    ABILITY_SCORES_TO_MODIFIERS = {1 : -5, 2 : -4, 3 : -4, 4 : -3, 5 : -3, 6 : -2, 7 : -2, 8 : -1, 9 : -1, 10 : 0,
                                   11 : 0, 12 : 1, 13 : 1, 14 : 2, 15 : 2, 16 : 3, 17 : 3, 18 : 4, 19 : 4, 20 : 5}

    def __init__(self, character_name, race, character_class, hit_die, armor_class):
        self.__name = character_name
        self.__race = race
        self.__class = character_class
        self.__hit_die = hit_die
        self.__armor_class = armor_class
        self.__level = 1
        self.__ability_scores = {}
        for abiliti in PlayerCharacter.ABILITIES:
            self.__ability_scores[abiliti] = self.roll_ability_score()
        self.__max_hp = self.__hit_die + self.get_ability_modifier("Constitution")
        self.__hp = self.__max_hp

    def get_name(self):
        return self.__name
        # Palauttaa hahmon nimen (__name-kentän arvon).

    def get_race(self):
        return self.__race
        # Palauttaa hahmon lajin (__race-kentän arvon).

    def get_class(self):
        return self.__class
        # Palauttaa hahmon luokan (__class-kentän arvon).

    def get_level(self):
        return self.__level
        # Palauttaa hahmon tason (__level-kentän arvon).

    def is_downed(self):
        if self.__hp == 0:
            return True
        else:
            return False
        #Hahmon elämäpisteet ovat nollassa eli hahmo on kykenemätön hyökkäämään tai liikkumaan ("downed").

    def get_ability_modifier(self, ability):
        if ability in self.__ability_scores:
            level = self.__ability_scores[ability]
            modifier = PlayerCharacter.ABILITY_SCORES_TO_MODIFIERS[level]
            return modifier
        else:
            return None

    def get_skill_level(self, skill):
        if skill in PlayerCharacter.SKILLS_TO_ABILITIES:
            skill_level = self.get_ability_modifier(PlayerCharacter.SKILLS_TO_ABILITIES[skill])
            return skill_level
        else:
            return None

    def skill_check(self, skill, result_to_pass):
        if skill in PlayerCharacter.SKILLS_TO_ABILITIES:
            skill_check = self.get_skill_level(skill) + self.roll_die(20)
            if skill_check >= result_to_pass:
                return True
            else:
                return False
        else:
            return None

    # Tämän metodin avulla hahmo tekee taitotestin taidossa skill (merkkijono). Taitotesti toimii seuraavasti:
    # pelaaja heittää 20-sivuista noppaa ja lisää tulokseen taidon taitotason (käytä hyväksi aiemmin toteutettua
    # get_skill_level-metodia). Tämän summan tulee olla vähintään yhtä suuri kuin parametri
    # result_to_pass (kokonaisluku), jotta hahmo läpäisisi taitotestin. Metodi palauttaa tiedon siitä,
    # onnistuiko taitotesti, eli True, mikäli taitotesti onnistui ja False, mikäli se epäonnistui.
    # Jos parametri skill ei ole oikea taito, metodi palauttaa None.

    def level_up(self):
        self.__level += 1
        nopanheiton_tulos = self.roll_die(self.__hit_die)
        self.__hp += nopanheiton_tulos
        self.__max_hp += nopanheiton_tulos
        return nopanheiton_tulos

    # Tämän metodin avulla hahmo kasvattaa tasoaan ("level up"). Hahmon __level-kenttää kasvatetaan
    # yhdellä ja hahmon elämäpisteet kasvavat siten, että heitetään noppaa, jossa on __hit_die-kentän verran sivuja.
    # Esimerkiksi hahmolle, jonka osumanoppa on 6, heitetään 6-sivuista noppaa. Elämäpisteitä kasvatetaan
    # nopanheiton tuloksen verran (siis sekä __max_hp- että __hp-kenttiä). Metodi palauttaa nopanheiton tuloksen
    # eli sen luvun, jolla elämäpisteitä kasvatettiin.

    def attack(self, other_character):
        die_roll_result = self.roll_die(20)
        if die_roll_result >= other_character.__armor_class:
            if self.__class == "Fighter":
                vahinko = PlayerCharacter.roll_die(6)
                if vahinko <= other_character.__hp:
                    other_character.__hp -= vahinko
                else:
                    other_character.__hp = 0.0
                return vahinko
            elif self.__class == "Ranger":
                vahinko = PlayerCharacter.roll_die(8)
                if vahinko <= other_character.__hp:
                    other_character.__hp -= vahinko
                else:
                    other_character.__hp = 0.0
                return vahinko
            elif self.__class == "Wizard":
                vahinko = PlayerCharacter.roll_die(10)
                if vahinko <= other_character.__hp:
                    other_character.__hp -= vahinko
                else:
                    other_character.__hp = 0.0
                return vahinko
            elif self.__class == "Rogue":
                vahinko = PlayerCharacter.roll_die(4)
                if vahinko <= other_character.__hp:
                    other_character.__hp -= vahinko
                else:
                    other_character.__hp = 0.0
                return vahinko
        else:
            return 0

    def heal(self):
        life_points = random.randint(1, 5)
        limit = self.__max_hp - self.__hp
        if life_points <= limit:
            self.__hp += life_points
        else:
            self.__hp = self.__max_hp
        return life_points

    def __str__(self):
        mjono ="{}, a level {} {} {}\n".format(self.__name, self.__level, self.__race, self.__class)
        mjono += "HP: {}/{}\n".format(self.__hp, self.__max_hp)
        mjono += "STR: {:2d}   DEX: {:2d}   CON: {:2d}   INT: {:2d}   WIS: {:2d}   CHA: {:2d}   "\
            .format(self.__ability_scores["Strength"], self.__ability_scores["Dexterity"],
                    self.__ability_scores["Constitution"], self.__ability_scores["Intelligence"],
                    self.__ability_scores["Wisdom"], self.__ability_scores["Charisma"])
        return mjono


    @staticmethod
    def roll_die(die_sides):
        return random.randint(1, die_sides)

    @staticmethod
    def roll_ability_score():
        roll_results = [PlayerCharacter.roll_die(6) for i in range(4)]  # throwing 4 6-sided dies
        smallest = 1000  # just some very large value
        for result in roll_results:  # choosing 3 largest results
            if result < smallest:
                smallest = result
        roll_results.remove(smallest)  # removing smallest result
        roll_sum = sum(roll_results)  # adding 3 largest results
        return roll_sum
