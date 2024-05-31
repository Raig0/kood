def loe_kollektsioon(failinimi):
    sonastik = {}
    with open(failinimi, encoding = "UTF-8") as fail:
        read = fail.readlines() #loeb read
        pealkiri = read[0].strip().split() # votab 1 2 3 4
        for rida in read[1:]: # votab iga rea eraldi
            osad = rida.strip().split() #teeb iga rea eraldi osadeks
            abc = osad[0] # votab A B C
            for i in range(1, len(osad)): # votab osad
                if osad[i] != "-": #kui i ei vordu -
                    voti = abc + pealkiri[i-1]
                    sonastik[voti] = osad[i]
    return sonastik

def vaata_puslesid(sonastik):
    for voti, vaartus in sonastik.items():
        
        return f"{voti} {vaartus}"
        
        
def mitu_puslet(sonastik, kategooria):
    mitu = 0
    for voti in sonastik.keys():
        if kategooria in voti:
            mitu += 1
    return mitu

def laena_pusle(sonastik):
    kood = input("Sisesta pusle kood: ")
    nimi = input("Sisesta laenaja nimi: ")
    
    if kood in sonastik.keys():
        if sonastik[kood] == "*":
            sonastik[kood] = nimi
    else:
        print("Vastava koodiga pusle ei ole Juku käes.")
    return sonastik

def tagasta_pusle(sonastik):
    kood = input("Sisesta pusle kood: ")
    if sonastik[kood] != "*":
        sonastik[kood] == "*"
        
    elif sonastik[kood] == "*":
        print("Vastava koodiga pusle on juba Juku käes.")
    return sonastik

def kirjuta_faili(sonastik, fail):
    pass


def main():
    sonastik = loe_kollektsioon("andmedk.py")
    while True:
        vali = input("""
1 - Vaata pusle kataloogi
2 - Leia puslede arv
3 - Laena pusle
4 - Tagasta pusle
5 - Lõpeta programmi töö
Vali tegevus: """)
    
        if vali == "1":
            print(vaata_puslesid(sonastik))
    
    
main()
        
