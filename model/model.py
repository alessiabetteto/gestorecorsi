from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodins(self): # il modello a sua volta non lo sa, lo chiede al DAO
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPDwIscritti(self, pd):
        result= DAO.getCorsiPDwIscritti(pd)
        # se volessimo ordinare la lista: si fa nel model perché lui si occupa di manipolare i dati
        result.sort(key=lambda s:s[1], reverse=True)  # s è una tupla della lista result, s[0] è il Corso, s[1] N iscritti
        return result

    def getStudentiCorso(self, codins):
        studenti = DAO.getStudentiCorso(codins)
        # ordiniamo per cognome
        studenti.sort(key=lambda s:s.cognome)
        return studenti

    def getCDSofCorso(self, codins):
        cds = DAO.getCDSofCorso(codins)
        cds.sort(key=lambda c:c[1], reverse=True)
        return cds