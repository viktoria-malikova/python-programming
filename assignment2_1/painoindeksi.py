def main():
    rivi = input("Anna painosi kiloina: ")
    paino = float(rivi)
    rivi = input("Anna pituutesi metreina: ")
    pituus = float(rivi)
    if pituus > 0.0 and pituus < 3.0:
        painoindeksi = paino / (pituus * pituus)
        print("Painoindeksisi on", painoindeksi)
        if painoindeksi < 19.0:
            print("Olet alipainoinen")
        elif painoindeksi < 25.0:
            print("Painosi on normaali")
        elif painoindeksi < 30.0:
            print("Olet lievasti ylipainoinen")
        elif painoindeksi < 35.0:
            print("Olet merkittavasti ylipainoinen")
        elif painoindeksi < 40.0:
            print("Olet vaikeasti ylipainoinen")
        else:
            print("Olet sairaalloisesti ylipainoinen")
    else:
        print("Virheellinen pituus - painoindeksia ei voi laskea")

main()