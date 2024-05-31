class Sportlane:
    def __init__(self, nimi, kaal):
        self.nimi = nimi
        self.kaal = kaal
        
    def __str__(self):
        return f"Nimi: {self.nimi}, kaal: {self.kaal}"
        
class Maadleja(Sportlane):
    def __init__(self, nimi, kaal):
        super().__init__(nimi, kaal)
        if kaal <= 55:
            self.kaalukategooria = "kärbeskaal"
        elif kaal <= 66:
            self.kaalukategooria = "kergekaal"
        elif kaal <= 84:
            self.kaalukategooria = "keskkaal"
        elif kaal <= 96:
            self.kaalukategooria = "poolraskekaal"
        elif kaal > 96:
             self.kaalukategooria = "raskekaal"
                
    def muuda_kaalu(self, kaal):
        self.kaal = kaal
        if kaal <= 55:
            self.kaalukategooria = "kärbeskaal"
        elif kaal <= 66:
            self.kaalukategooria = "kergekaal"
        elif kaal <= 84:
            self.kaalukategooria = "keskkaal"
        elif kaal <= 96:
            self.kaalukategooria = "poolraskekaal"
        else:
            self.kaalukategooria = "raskekaal"
                
    def __str__(self):
        return f"Nimi: {self.nimi}, kaal: {self.kaal}, kaalukategooria: {self.kaalukategooria}"
    
sportlane = Sportlane("Indrek", 105)
maadleja1 = Maadleja("Georg", 83)
maadleja2 = Maadleja("Kristjan", 115)

print(sportlane)
print(maadleja1)
print(maadleja2)
maadleja2.muuda_kaalu(95)
print(maadleja2)