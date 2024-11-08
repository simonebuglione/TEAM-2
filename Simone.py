#Parte Simone: creazione menu
#creo classe menu
class Menu:
    def __init__(self, ArchivioUtente):
        self.__ArchivioUtente = ArchivioUtente
        self.__UtenteCorrente = None  #utente attualmente loggato

    def carica_utenti(self):
        #carica utenti da archivio
        self.__ArchivioUtente.carica_utenti()

    def start(self):
        #gestisce ciclo del menu
        while True:
            if self.__utente_corrente:
                print(f"\nCiao {self.__utente_corrente['nome']}! Punteggio attuale: {self.__utente_corrente['punteggio']}")
                print("1. Inizia gioco")
                print("2. Visualizza classifica")
                print("3. Esci")
                scelta = input("Scegli un'opzione(1, 2, 3): ")

                if scelta == '1':
                    self.__inizia_gioco()
                elif scelta == '2':
                    self.__classifica()
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
        utente = self.__ArchivioUtente.login(nome_utente, password)
        if utente:
            self.__utente_corrente =utente
            print(f"Login effettuato con successo, benvenuto {utente['nome']}!")
        else:
            print("Credenziali non valide, riprova")

    def registrazione(self):
        #permette all'utente di registrarsi
        nome_utente = input("Scegli nome utente: ")
        password = input("Scegli password: ")
        conferma_password = input("Conferma password: ")

        if password != conferma_password:
            print("password errrata, riprova")
            return

        #crea nuovo utente e lo aggiunge all'archivio
        nuovo_utente = self.__ArchivioUtente.registra(nome_utente, password)
        if nuovo_utente:
            print(f"Registrazione completata, benvenuto {nuovo_utente['nome']}!")
        else:
            print("Nome utente già esistente, riprova")

    def classifica(self):
        #mostra classifica con punteggi più alti
        print("\nClassifica:")
        classifica = self.__ArchivioUtente.get_classifica()
        for utente in classifica:
            print(f"{utente['nome']}: {utente['punteggio']} punti")

    def inizia_gioco(self):
        #avvia il gioco (dobbiamo sostituirlo con il gioco)
        print("il gioco è iniziato (inseriamo il gioco)")
        #implementiamo la logica del gioco qui. aggiorna il punteggio dell'utente
        if self.__utente_corrente:
            self.__utente_corrente['punteggio'] +=1  #incrementa il punteggio come esempio

    def salva_classifica(self):
        #funzione che salva la classifica su file quando si chiude il programma
        self.__ArchivioUtente.salva_classifica()
