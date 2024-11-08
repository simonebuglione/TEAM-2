"""RICHIESTE CLIENTE

Registrazione e Login
Il gestionale deve permettere agli utenti di registrarsi e fare il login.
Ogni utente ha un punteggio iniziale di 0.
I dati degli utenti (nome, punteggio, ecc.) vengono salvati in un file per la persistenza.

Menu Principale
Dopo il login, viene mostrato un menu con le opzioni: "Ciao [Nome utente]", "Login", "Esci".
Il menu permette di interagire con il sistema e accedere alla funzionalità evolutiva (Gamification).

Funzionalità Evolutiva (Gamification)
Ogni volta che l'utente compie un'azione con un risultato corretto (ad esempio, una risposta giusta a una domanda), il punteggio dell'utente (X) aumenta.
Più il punteggio X aumenta, più la difficoltà delle azioni proposte cresce.
La difficoltà aumenta tramite:
Più addendi nelle somme (es. 2 addendi, poi 3 addendi, ecc.).
Maggiore tempo a disposizione per rispondere.

Sistema di Punteggio
L'utente inizia con 0 punti.
Ogni volta che l'utente risponde correttamente a una domanda, guadagna 1 punto. Se la risposta è errata, perde 1 punto.
La difficoltà aumenta con il punteggio accumulato:
A 5 punti, la somma diventa con 3 addendi.
A 10 punti, con 4 addendi, e così via, fino a 10 livelli di difficoltà.

Classifica degli Utenti
Il sistema tiene traccia dei punteggi di tutti gli utenti e genera una classifica.
La classifica deve essere stampata a schermo, mostrando gli utenti con i punteggi più alti.
Quando il programma viene chiuso, la classifica deve essere salvata in un file di testo o altro formato di salvataggio, in modo che i punteggi siano mantenuti tra le sessioni (es. "Pippo: 15 punti" salvato nel file).
Salvataggio della Classifica
La classifica viene aggiornata e salvata nel file ogni volta che il programma si chiude.
Il salvataggio avviene in modo semplice, senza l'uso di librerie esterne come pandas, scikit-learn ecc."""


class Utente:
    def __init__(self,nome_utente,password):
        self.__nome_utente = nome_utente
        self.__password = password
        self.__punteggio = 0

    def get_utente(self):
        return self.__nome_utente
    
    def set_utente(self,nome_utente):
        self.__nome_utente = nome_utente

    def get_password(self):
        return self.__password
    
    def set_password(self,password):
        self.__password = password

    def get_punteggio(self):
        return self.__punteggio
    
    def set_punteggio(self,punteggio):
        self.__punteggio = punteggio
    

class ArchivioUtenti:
    def __init__(self):
        self.__utenti = {}


    def get_utenti(self):
        return self.__utenti
    
    def set_utenti(self,utenti):
        self.__utenti = utenti

    def registrazione(self,nome_utente,password):
        if nome_utente in self.__utenti:
            return False
        else:
            utente = Utente(nome_utente,password)
            self.__utenti[nome_utente] = utente
            return True
        

    def login(self,nome_utente,password):
        if nome_utente in self.__utenti:
            utente = self.__utenti[nome_utente]
            if utente.get_password() == password:
                return 0  #Login effettuato
            else:
                return 1 #Password errata
        else:
            return 2 #Nome utente errato
        



#utenti = ArchivioUtenti()

#utenti.registrazione("alep_03","1234")


import random

class Gioco:
    # aggiugnere classifica come parametro
    def __init__(self, nome_utente, classifica):
        self.nome_utente=nome_utente
        self.classifica=classifica
        self.punteggio = classifica.get_punteggio(nome_utente)
        self.vite=10
       
    def livello_difficoltà(self):
        risposta=input(f "Ciao {self.nome_utente} . Da che livello vuoi partire? ")
        for livello in ["facile", "medio","difficile"]:
            if risposta.lower() in livello:
                if self.livello_consentito(livello):
                    return livello
                else:
                    print("Il tuo punteggio è troppo basso per accedere a questo livello. ")
            else :
                print("Riprova")

    def livello_consentito(self, livello):
        if livello == "facile":
            return True
        if livello == "medio":
            if self.punteggio > 10:
                return True
        if livello == "difficile":
            if self.punteggio > 55:
                return True
        return False

        
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

        self.classifica.aggiungi_punteggio_in_classifica(self, self.nome_utente, self.punteggio)

class Classifica:
    
    def __init__(self):
        self.__classifica = {}
    
    def aggiungi_punteggio_in_classifica(self, username, punteggio):
            self.get_classifica()[username] = punteggio

    def get_classifica(self):
        return self.__classifica

    def visualizza_classifica(self):  
        print("CLASSIFICA")
        classifica_ordinata = self.ordina_classifica()
        print(classifica_ordinata)

    def ordina_classifica(self):
        classifica_ordinata = 
        return classifica_ordinata

    def salva_su_file(self, nome_file="classifica.txt"):
        with open(nome_file, "w") as file:
            for key, value in self.get_classifica().items():
                file.write(f"{key}: {value}\n")

    def carica_da_file(self, nome_file="classifica.txt"):
        with open(nome_file, "r") as file:
            for riga in file:
                key, value = riga.strip().split(": ")
                self.get_classifica()[key] = value

    def get_value(item):
        return item[1]
    
     # Function to sort a dictionary by values
    def sort_dict_by_value(dictionary):
        # Convert dictionary items to a list and use the helper function to sort by values
        dictionary.items()
        sorted_items = sorted(dictionary.items(), key=get_value)
        # Convert back to dictionary
        sorted_dict = dict(sorted_items)
        return sorted_dict
    
    def get_punteggio(nome_utente)
    
#Parte Simone: creazione menu
#creo classe menu


class Menu:
    def __init__(self):
        self.__archivio_utente = ArchivioUtente()
        self.__utente_corrente = None  #utente attualmente loggato
        self.__classifica = Classifica()

    def carica_utenti(self):
        #carica utenti da archivio
        self.__archivio_utente.carica_utenti()

    def start(self):
        #creare classifica (oggetto Classifica)
        #gestisce ciclo del menu
        while True:
            if self.__utente_corrente:
                nome_utente = self.__utente_corrente['nome']
                punteggio = self.__utente_corrente['punteggio']
                print(f"\nCiao {nome_utente}! Punteggio attuale: {punteggio}")
                print("1. Inizia gioco")
                print("2. Visualizza classifica")
                print("3. Esci")
                scelta = input("Scegli un'opzione(1, 2, 3): ")

                if scelta == '1':
                    self.__inizia_gioco(nome_utente, classifica)
                elif scelta == '2':
                    self.__visualizza_classifica()
                elif scelta == '3':
                    self.__salva_classifica()
                    print("a presto!!")
                    break
                else:
                    print("Opzione non valida, riprova.")
            else:
                print("Benvenuto")
                print("1. Login")
                print("2. Registrazione")
                print("3. Esci")
                scelta = input("Scegli un'opzione (1, 2, 3): ")

                if scelta == '1':
                    self.__login()
                elif scelta == '2':
                    self.__registrazione()
                elif scelta == '3':
                    print("a presto!")
                    break
                else:
                    print("Opzione non valida, riprova")

    def login(self):
        #fa fare il login all'utente
        nome_utente = input("Inserisci nome utente: ")
        password = input("Inserisci password: ")

        #verifica login tramite ArchivioUtente
        utente = self.__archivio_utente.login(nome_utente, password)
        if utente == 0:
            self.__utente_corrente =utente
            print(f"Login effettuato con successo, benvenuto {utente['nome']}!")
        elif utente == 1:
            print("PASSWORD ERRATA")
        elif utente == 2:
            print("USERNAME NON ESISTE")

    def __registrazione(self):
        #permette all'utente di registrarsi
        nome_utente = input("Scegli nome utente: ")
        password = input("Scegli password: ")
        conferma_password = input("Conferma password: ")

        if password != conferma_password:
            print("password errrata, riprova")
            return

        #crea nuovo utente e lo aggiunge all'archivio
        nuovo_utente = self.__archivio_utente.registrazione(nome_utente, password)
        if nuovo_utente:
            print(f"Registrazione completata, benvenuto {nuovo_utente['nome']}!")
        else:
            print("Nome utente già esistente, riprova")

    def __visualizza_classifica(self):
        #mostra classifica con punteggi più alti
        print("\nClassifica:")
        # classifica = self.__archivio_utente.get_classifica()
        chiama la funzione stampa_classifica di Classifica

    def __inizia_gioco(self, nome_utente, classifica):
        #avvia il gioco (dobbiamo sostituirlo con il gioco)
        print("il gioco è iniziato (inseriamo il gioco)")
        gioco = Gioco(nome_utente, classifica)
        gioco.avvia_gioco()
        #implementiamo la logica del gioco qui. aggiorna il punteggio dell'utente
        if self.__utente_corrente:
            self.__utente_corrente['punteggio'] +=1  #incrementa il punteggio come esempio

    def __salva_classifica(self):
        #funzione che salva la classifica su file quando si chiude il programma
        self.classifica.salva_classifica()



il_menu = Menu()
il_menu.start()