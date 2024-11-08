import random

class Gioco:
    def __init__(self, nome_utente):
        self.nome_utente=nome_utente
        self.vite=10
       
    def livello_difficoltà(self):
        risposta=input(f "Ciao {self.nome_utente} . Da che livello vuoi partire? ")
        for livello in ["facile", "medio","difficile"]:
            if risposta.lower() in livello:
                return livello
            else :
                print("Riprova")

        
    def gioco1(self):
        print("Hai scelto il gioco più facile ! Let's go !")


        while self.vite > 0:
            domande = [("Quanto fa 5 + 7?", "12"), ("Quanto fa 9 + 2?", "11")]
            domanda, risposta_corretta = random.choice(domande)

            risposta = input(f"{domanda} ")

            
            if risposta == risposta_corretta:
                self.punteggio += 10
                print(f"Bravo! Hai guadagnato 10 punti, il tuo punteggio totale è {self.punteggio}")
                break
            else:
                self.punteggio -= 10
                self.vite -= 1
                print(f"Risposta errata!  Riprova!")

    def gioco2(self):
        print("Hai scelto il livello medio ! Cominciamo !!")

        while self.vite>0:
            risposta = input("Dimmi la capitale della Francia ")
            risposta2=input("Come si chiama il nuovo presidente americano ? ")
            
            if risposta.lower() == "Parigi ":
                self.punteggio += 65
                print(f"Bravo! Hai guadagnato 15 punti, il tuo punteggio totale è {self.punteggio}")
                break
            else:
                self.punteggio -= 35
                self.vite -= 1
                print(f"Risposta errata! Riprova!")
                continue
    
    def gioco3(self):
        print("Acciderbolina! Sei un temerario, mi hai sfidato! Ora finirai tutte le vite my friend !")

        while self.vite >0:
            risposta= int(input("Scrivi l'anno della caduta del'impero romano d'Oriente "))
            risposta1= int(input ("Dimmi in quale anno l'uomo ha messo piede sulla Luna?"))
            risposta2= input("Dimmi come si chiama il ct della nazionale italiana di calcio")

            if risposta.lower() == 1453 and risposta1 = 1969 and (risposta2.lower = "spalletti" or risposta2.lower()="luciano spalletti")
                self.punteggio += 365
                print(f"Bravo! Hai guadagnato 15 punti, il tuo punteggio totale è {self.punteggio}")
                break
            else:
                self.punteggio -= 135
                self.vite -= 1
                print(f"Risposta errata! Riprova!")
                continue

    def avvia_gioco(self):
        livello = self.livello_difficoltà()
        
        # Apertura del gioco in base alla difficoltà scelta
        if livello == "facile":
            self.gioco1()
        elif livello == "medio":
            self.gioco2()
        elif livello == "difficile":
            self.gioco3()