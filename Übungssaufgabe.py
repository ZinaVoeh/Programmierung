class Konto:
    def __init__(self, inhaber, zugriffsberechtigte={"bank"}, kontostand=7):
        self.__inhaber = inhaber
        self.__zugriffsberechtigte = zugriffsberechtigte
        self.__kontostand = kontostand
        self.__buchungen = []
    
    def kontostand(self):

        return "Ihr Kontostand beträgt: " + str(self.__kontostand) + "€."
    
    def abbuchungen(self, betrag, person):

        if person in self.__zugriffsberechtigte or self.__inhaber == person:

            if betrag >= 0 and self.__kontostand >= betrag:
                self.__kontostand -= betrag
                neueBuchung = Buchung("12.10.2022", betrag, "Hallo", person)
                self.__buchungen.append(neueBuchung)
                return "Die Abbuchung war erfolgreich. Ihr neuer Kontostand beträgt " + str(self.__kontostand) + "€!"
                
                
            
            else:
                return "Diese Abbuchung ist nicht möglich!"

        else:
                return "Diese Abbuchung ist nicht möglich!"


    
    def zubuchung(self, betrag, person):

        if betrag > 0:

            self.__kontostand += betrag
            return "Der Betrag wurde erfolgreich eingezahlt. Ihr neuer Kontostand beträgt " + str(self.__kontostand) + "€!"

        else:

            return "Der Betrag ist kleiner als null und kann daher nicht eingezahlt werden!"



class Buchung:
    def __init__(self, buchungsdatum, betrag, buchungstext, empfänger):
        self.__buchungsdatum = buchungsdatum
        self.__betrag = betrag
        self.__buchungstext = buchungstext
        self.__empfänger = empfänger

    def buchungAlsText(self):

        return "Am " + self.__buchungsdatum + ", wurden " + str(self.__betrag) + "€ mit folgendem Text: " + self.__buchungstext + " an " + self.__empfänger + "überwiesen."


        
#class bank: 


konto1 = Konto("Sina Vöhringer")
print(konto1.kontostand())


print(konto1.abbuchungen(3, "bank"))
#Konto1 = buchungen("12.10.2022", 10, "HAllo", "Herr Mensch")

#print(Konto1.buchungAlsText())
    
