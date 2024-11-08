class Gioco:
    def __init__(self, nome_utente):
        self.nome_utente=nome_utente
        self.vite=10
        self.livello=0
       
    def livello_difficoltà(self):
        print(f"\n Ciao {self.utente}! Iniziamo con il livello di difficoltà {self.livello}.")
        print("Hai 10 vite iniziali, ogni errore ti costa una vita.")

    def gioco1(self):
        while self.vite > 0:
            risposta = input("Quanto fa 2+2? Rispondi con il numero: ")
            
            if risposta == "4":
                self.punteggio += 5
                print(f"Bravo! Hai guadagnato 5 punti, il tuo punteggio totale è {self.punteggio}. Puoi passare al gioco 2!")
                self.livello += 1
                break
            else:
                self.punteggio -= 5
                self.vite -= 1
                print(f"Risposta errata! Ti rimangono {self.vite} vite e il tuo punteggio è ora {self.punteggio}. Riprova!")
        
        if self.vite == 0:
            print("Hai esaurito le vite! Riprova dall'inizio.")
