def loe_seis(failinimi):
    sonastik = {}
    with open(failinimi, encoding = "UTF-8") as fail:
        read = fail.readlines()
        for rida in read[1:]:
            osad = rida.strip().split()
            numbrid = []
            for nr in osad[1:]:
                if nr.isdigit():
                    nr = int(nr)
                    numbrid.append(nr)
                else:
                    numbrid.append(nr)
            sonastik[osad[0]] = numbrid
        return sonastik
    
def lisa_tulemus(osaleja, vooru_nr, tulemus, sonastik):
    
    if osaleja in sonastik:
        if sonastik[osaleja][vooru_nr - 1] == "-":
            sonastik[osaleja][vooru_nr - 1] = tulemus
            print("Tulemus lisatud!")
        else:
            print("Tulemus on juba lisatud")
    else:
        print("Sellist osalejat ei ole")
    return sonastik
            
def leia_skoor(osaleja, sonastik):
    kokku = sum(int(x) for x in sonastik[osaleja] if x != "-")
    return kokku

def leia_parim(sonastik):
    tulemus = 0
    for nimi, väärtus in sonastik.items():
        if leia_skoor(nimi, sonastik) > tulemus:
            tulemus = leia_skoor(nimi, sonastik)
            parim = nimi
    print(f"Suurima skooriga on {parim} ({tulemus} punkti).")
    
def faili(sonastik, failinimi):
    with open(failinimi, "w") as fail:
        for nimi, väärtus in sonastik.items():
            punktid = ' '.join(str(e) for e in väärtus)
            fail.write(f"{nimi} {punktid}\n")
    
def main():
    sonastik = loe_seis("lk.py")
    while True:
        tegevus = input("""Vali tegevus:
1 - Vaata punktitabelit
2 - Lisa tulemus
3 - Vaata skoori
4 - Leia võitja
5 - Lõpeta programmi töö
""")
        if tegevus == "1":
            for nimi, tulemused in sonastik.items():
                print(nimi + ":", ' '.join(map(str, tulemused)))
        
        elif tegevus == "2":
            osaleja = input("Sisesta osaleja nimi: ")
            vooru_nr = int(input("Sisesta vooru number: "))
            tulemus = int(input("Sisesta tulemus: "))
            sonastik = lisa_tulemus(osaleja, vooru_nr, tulemus, sonastik)
        
        elif tegevus == "3":
            nimi = input("Sisestage osaleja nimi: ")
            skoor = leia_skoor(nimi, sonastik)
            print(f"{nimi} skoor on {skoor}")
            
        elif tegevus == "4":
            leia_parim(sonastik)
            
        elif tegevus == "5":
            faili(sonastik, "turniir_uus.txt")
            print("Programm lõpetas töö")
            break
        
        else:
            print("Sellist valikut ei ole")
main()

    