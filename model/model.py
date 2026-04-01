from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodins(self): # il modello a sua volta non lo sa, lo chiede al DAO
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()