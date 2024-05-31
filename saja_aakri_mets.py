def juurdekasv(pindala, juurdekasv):
    pindala = float(pindala)
    hektar = pindala * 0.4047
    juures = hektar * juurdekasv
    juures = round(juures, 1)
    return juures

failinimi = input("Sisesta failinimi: ")
juurde = float(input("Sisestage aastane juurdekasv hektari kohta tihumeetrites: "))
piir = float(input("Sisesta piir millest suuremad arvesse võtta: "))

with open(failinimi, encoding = "UTF-8") as fail:
    arvutati = 0
    for rida in fail:
        if float(rida) < piir:
            print("Metsatükki ei võeta arvesse.")
        elif float(rida) > piir:
            print(juurdekasv(rida, juurde))
            arvutati += 1
print(f"Arvutati {arvutati} metsatüki juurdekasv")
