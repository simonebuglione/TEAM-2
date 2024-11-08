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

