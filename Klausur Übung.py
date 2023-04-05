class Bank:
    def __init__(self):
        self.__konto = []
    
    def kontoerstellen(self, inhaber):
        for element in self.__konto:
            if element["inhaber"] == inhaber:
                element["konto"] += 1
            
            else:
                dictionaryKonto = {}
                dictionaryKonto["inhaber"] = inhaber
                dictionaryKonto["kontos"] = 1
                self.__konto.append(dictionaryKonto)



class Konto:

    def __init__(self, inhaber, zugriffberechtigte={"bank"}, kontostand=0):
        self.__inhaber = inhaber
        self.__zugriffberechtigte = zugriffberechtigte
        self.__kontostand = kontostand
        self.__buchungen = []

    def einzahlen(self, betrag):
        if str(betrag).isnumeric() == True and betrag > 0:
            self.__kontostand += betrag
            return f"Der neue Kontostand beträgt: {self.__kontostand}€"
        
        else:
            return f"Der Betrag ist kleiner als null oder keine Zahl!"

    def auszahlen(self, betrag, person):
        if person in self.__zugriffberechtigte or self.__inhaber:
            if str(betrag).isnumeric() == True and betrag > 0:
                if betrag <= self.__kontostand:
                    self.__kontostand -= betrag

                return f"Der neue Kontostand beträgt: {self.__kontostand}€"
        
        else:
            return f"Der Betrag ist kleiner als null oder keine Zahl!"

    def kontostand(self):
        f"Der aktuelle Kontostand beträgt: {self.__kontostand}€"

class Buchungen:

    def __init__(self, buchungsdatum, betrag, buchungstext, empfänger):
        self.__buchungsdatum = buchungsdatum
        self.__betrag = betrag
        self.__buchungstext = buchungstext
        self.__empfänger = empfänger

    def buchungAlsText(self):
        return f"Am {self.__buchungsdatum} wurden {self.__betrag}€ mit folgendem Text {self.__buchungstext} an {self.__empfänger} überwiesen"

buchung1 = Buchungen("11.09.2022", "11", "Hallo", "HUHU")
print(buchung1.buchungAlsText())

konto1 = Konto("Sina")
print(konto1.einzahlen(10))
print(konto1.auszahlen(1, "Sina"))