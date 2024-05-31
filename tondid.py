class Tont:
    def __init__(self, nimi, vanus, elukoht):
        self.nimi = nimi
        self.vanus = vanus
        self.elukoht = elukoht
        
    def kummita(self):
        print(f"{self.nimi} kummitab elukohas {self.elukoht}.")
        
    def __str__(self):
        return f"Nimi: {self.nimi}, vanus: {self.vanus}, elukoht: {self.elukoht}."
    
    
class Võlur(Tont):
    def nõiu(self, isend):
        print(f"{self.nimi} pani nõiduse, millega sai pihta {isend.nimi}.")
        
tont = Tont("Norbert", 31, "Tartu")
võlur1 = Võlur("Harry", 17, "Tartu")
võlur2 = Võlur("Snape", 35, "Tartu")

print(tont)
print(võlur1)
print(võlur2)
tont.kummita()
võlur1.nõiu(võlur2)