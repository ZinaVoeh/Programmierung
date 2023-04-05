from unicodedata import name


class Mensch:
    def __init__(self, name, geburtsdatum):
        self.__name = name
        self.__geburtsdatum = geburtsdatum

    def stell_dich_vor(self):
        return "Ich heiße" + self.__name
    
    def geburtsdatumAnzeigen(self):
        return self.__geburtsdatum

class Amt:
    def __init__(self, name):
        self.__antraege = {}
        self._name = name 

    
    def nehme_antrag_an(self, person, antrag):
        if person not in self.__antraege:
            self.__antraege[person] = []
        
        self.__antraege[person].append(antrag)

    def gib_auskunft_zu(self, person, antrag):
        pass

    def sende_bescheid(self, beamter, person, bescheid):
        pass

    def nenne_name(self):
        return self.__name

    def helloWorld(self):
        return "Hallo von dem DVM 2021!"

class Standesamt(Amt):
    def __init__(self, name, adresse):
        super().__init__("Standesamt " + adresse)
        self.__name = name
        self.__adresse = adresse
        self.__geburtenregister = {}
        self.__sterberegister = {}
        self.__eheregister = {}

    def geburt_eintragen(self, neugeborenes, mutter, vater):
        self.__geburtenregister[neugeborenes] = (mutter, vater)

    def ehe_eintragen(self, partner1, partner2, datum):

        neueEhe = Ehe(partner1, partner2, datum)

        if partner1 not in self.__eheregister:
            self.__eheregister[partner1] = []
        
        if partner2 not in self.__eheregister:
            self.__eheregister[partner2] = []

        self.__eheregister[partner1].append(neueEhe)
        self.__eheregister[partner2].append(neueEhe)

    def todestag_eintrage(self, person, todestag):
        
        if person not in self.__sterberegister:
            self.__sterberegister[person] = todestag
        
        if person in self.__eheregister:
            for ehe in self.__eheregister[person]:
                if ehe.istEheAufrecht():
                    ehe.enddatumÄndern(todestag)


class Bauamt:
    def __init__(self, ort):
        super().__init__("Bauamt")
        self.__ort = ort

    def nenne_name(self):
        return super().nenne_name() + " " + self.__ort     


class Ehe:
    def __init__(self, partner1, partner2, datum, enddatum):
        self.__partner1 = partner1
        self.__partner2 = partner2
        self.__datum = datum
        self.__enddatum = enddatum

    def istEheAufrecht(self):
        if bool(self.__enddatum):
            return False
        
        else:
            return True

    def enddatumÄndern(self, neuesEnddatum):
        self.__enddatum == neuesEnddatum


class Antrag:
    def __init__(self, antragssteller, antragstext):
        self.__antragssteller = antragssteller
        self.__antrgstext = antragstext
        
    


standesamtBlaubeuren = Standesamt("Standesamt Blaubeuren", "Karlstraße 2 89134 Blaubeuren")
standesamtLudwigsburg = Standesamt("Standesamt Lubu", "Ludwigsburg")
standesamtKehl = Standesamt("Standesamt Kehl", "Kehl")

bauamtStuttgart = Bauamt("Stuttgart")

print(standesamtBlaubeuren.nenne_name())
print(standesamtLudwigsburg.nenne_name())
print(standesamtKehl.nenne_name())

print(bauamtStuttgart.nenne_name())

#print(standesamt.helloWorld())