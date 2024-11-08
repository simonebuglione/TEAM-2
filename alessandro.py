class Utente:
    def __init__(self,nome_utente,password,punteggio):
        self.__nome_utente = nome_utente
        self.__password = password
        self.__punteggio = punteggio

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
    

    