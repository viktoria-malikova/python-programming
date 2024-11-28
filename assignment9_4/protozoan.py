NUMBER_OF_GENES = 10
GENE_MIN_VALUE = 0
GENE_MAX_VALUE = 5

class Protozoan:
    NUMBER_OF_GENES = 10
    GENE_MIN_VALUE = 0
    GENE_MAX_VALUE = 5

    def __init__(self, given_name, genelist):
        self.__name = given_name
        for alkio in genelist:
            if (alkio < GENE_MIN_VALUE or alkio > GENE_MAX_VALUE) or len(genelist) != NUMBER_OF_GENES:
                self.__genes = [0] * NUMBER_OF_GENES
                break
            else:
                self.__genes = genelist.copy()
    #Metodi luo uuden Protozoan-olion.
    #Se saa parametrina luotavan alkueläimen nimen ja kokonaislukulistan, joka sisältää luotavan alkueläimen geenit.

    def get_name(self):
        return self.__name
    #Palauttaa alkueläimen nimen (merkkijono).

    def get_genes(self):
        return self.__genes
    #Palauttaa alkueläimen geenit sisältävän kokonaislukulistan.

    def mutation(self, gene_no, new_gene):
        if 0 <= gene_no <= 9 and GENE_MIN_VALUE <= new_gene <= GENE_MAX_VALUE:
            self.__genes[gene_no] = new_gene
            return True
        else:
            return False
    #Vaihtaa alkueläimen geenit sisältävässä listassa parametrina annetun geenin
    #(listassa indeksillä gene_no olevan alkion) uudeksi arvoksi viimeisen parametrin arvon.

    def clone(self, clone_name):
        clone = Protozoan(clone_name, self.__genes)
        return clone
    #Luo ja palauttaa uuden Protozoan-olion.

    def mate(self, another_protozoan, descendant_name):
        uudet_geenit = another_protozoan.get_genes()
        another_protozoan_list = list(self.__genes)
        for i in range(0, len(self.__genes), 2):
            another_protozoan_list[i] = uudet_geenit[i]
        new_protozoan = Protozoan(descendant_name, another_protozoan_list)
        return new_protozoan
    #Luo uuden Protozoan-olion, joka saa geenien 1, 3, 5, 7 ja 9 arvot nykyiseltä alkueläimeltä
    #ja loppujen geenien arvot parametrina saadulta alkueläimeltä.

    def __str__(self):
        mjono = "Name: " + str(self.__name) + ", genes: " + str(self.__genes)
        return mjono
    #Metodi palauttaa merkkijonon.