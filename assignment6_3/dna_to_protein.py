dna_to_rna_bases = {"G" : "C", "C" : "G", "A" : "U", "T" : "A"}
amino_acids = {"UUU" : "Phe", "UUC" : "Phe", "UUA" : "Leu", "UUG" : "Leu",
            "CUU" : "Leu", "CUC" : "Leu", "CUA" : "Leu", "CUG" : "Leu",
            "AUU" : "Ile", "AUC" : "Ile", "AUA" : "Ile", "AUG" : "Met",
            "GUU" : "Val", "GUC" : "Val", "GUA" : "Val", "GUG" : "Val",
            "UCU" : "Ser", "UCC" : "Ser", "UCA" : "Ser", "UCG" : "Ser",
            "CCU" : "Pro", "CCC" : "Pro", "CCA" : "Pro", "CCG" : "Pro",
            "ACU" : "Thr", "ACC" : "Thr", "ACA" : "Thr", "ACG" : "Thr",
            "GCU" : "Ala", "GCC" : "Ala", "GCA" : "Ala", "GCG" : "Ala",
            "UAU" : "Tyr", "UAC" : "Tyr", "UAA" : "STOP", "UAG" : "STOP",
            "CAU" : "His", "CAC" : "His", "CAA" : "Gln", "CAG" : "Gln",
            "AAU" : "Asn", "AAC" : "Asn", "AAA" : "Lys", "AAG" : "Lys",
            "GAU" : "Asp", "GAC" : "Asp", "GAA" : "Glu", "GAG" : "Glu",
            "UGU" : "Cys", "UGC" : "Cys", "UGA" : "STOP", "UGG" : "Trp",
            "CGU" : "Arg", "CGC" : "Arg", "CGA" : "Arg", "CGG" : "Arg",
            "AGU" : "Ser", "AGC" : "Ser", "AGA" : "Arg", "AGG" : "Arg",
            "GGU" : "Gly", "GGC" : "Gly", "GGA" : "Gly", "GGG" : "Gly"
              }

# Your code here
def check_dna(dna):
    if len(dna) % 3 != 0:
        return False
    else:
        for i in dna:
            if i not in dna_to_rna_bases:
                return False
        return True

# Funktio saa parametrina merkkijonon, joka kuvaa DNA-ketjua. Funktio tarkistaa,
# voiko DNA-ketjun perusteella luoda proteiinin, eli onko ketjussa vain sallittuja kirjaimia
# ja onko se oikean pituinen eli onko pituus kolmella jaollinen. Funktio palauttaa False,
# jos DNA-ketjussa on jotain vikaa, ja muutoin True.

def dna_to_rna(dna):
        rna = ""
        for i in dna:
            rna += dna_to_rna_bases[i]
        return rna

#Funktio saa parametrina DNA - ketjua kuvaavan merkkijonon.Funktio muuntaa DNA - ketjun
# RNA - ketjuksi ja palauttaa RNA - ketjua kuvaavan merkkijonon.

def rna_to_protein(rna):
    aminohappoketju = []
    for i in range(0, len(rna), 3):
        code = rna[i:i+3]
        if amino_acids[code] == "STOP":
            aminohappo = "*"
        else:
            aminohappo = amino_acids[code]
        aminohappoketju.append(aminohappo)
    return "-".join(aminohappoketju)

# Funktio saa parametrina RNA-ketjua kuvaavan merkkijonon. Funktio käy läpi ketjun emäskolmikot ja
# lisää aminohappoketjuun oikeat aminohapot. Funktio palauttaa aminohappoketjua kuvaavan merkkijonon muotoiltuna siten,
# että aminohappojen kolmikirjaimisten lyhenteiden välissä on viiva, ja STOP-kodoneita vastaavat kohdat on merkitty
# tähdellä *. Katso mallia esimerkkiajoista. VINKKI: join-metodista voi olla tässä funktiossa hyötyä.

def main():
    print("Enter the DNA sequence:")
    dna_code = input()
    dna_code = dna_code.upper()
    dna_oikeellisuus = check_dna(dna_code)
    if dna_oikeellisuus == False:
        print("Sorry,", dna_code ,"is not a valid DNA sequence for protein synthesis.")
    else:
        rna_code = dna_to_rna(dna_code)
        print("DNA:", dna_code)
        print("RNA:", rna_code)
        protein_code = rna_to_protein(rna_code)
        print("Protein:", protein_code)

        luvut = protein_code.split("-")
        lukulista = []
        for luku in luvut:
            lukulista.append(luku)

        print("The protein has", len(lukulista) ,"amino acids in total.")

main()