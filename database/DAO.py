from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class DAO():

    @staticmethod
    def getCodins():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select codins
                    FROM corso"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["codins"])


        cursor.close()
        cnx.close()
        return res

    """ Meglio appendere l'oggetto Corso dal momento che ci servirà in seguito, piuttosto che la stringa codins"""
    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT * FROM corso"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(
                codins = row["codins"],
                crediti = row["crediti"],
                nome = row["nome"],
                pd = row["pd"]
            ))


        cursor.close()
        cnx.close()
        return res


    @staticmethod
    def getCorsiPD(pd):
           cnx = DBConnect.get_connection()
           cursor = cnx.cursor(dictionary=True)

           query = """SELECT *
                    FROM corso c
                    WHERE c.pd = %s """

           cursor.execute(query, (pd,))  # periodo didattico è un parametro che ci arriva dall'esterno

           res = []
           for row in cursor:
               res.append(Corso(**row
                   # codins = row["codins"],
                   # crediti = row["crediti"],
                   # nome = row["nome"],
                   # pd = row["pd"]
                   # poiché i nomi delle chiavi sono uguali ai nomi delle proprietà possiamo fare l'unpack del dizionario
               ))


           cursor.close()
           cnx.close()
           return res

    @staticmethod
    def getCorsiPDwIscritti(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select c.codins, c.crediti , c.nome , c.pd, count(*) as n
                    from corso c, iscrizione i
                    where c.codins = i.codins 
                    and c.pd = %s
                    group by c.codins, c.crediti , c.nome , c.pd  """

        cursor.execute(query, (pd,))  # periodo didattico è un parametro che ci arriva dall'esterno

        res = []
        for row in cursor:
            res.append((Corso(codins = row["codins"],    # append(Corso, int)
                             crediti = row["crediti"],
                             nome = row["nome"],
                             pd = row["pd"]),
                       row ["n"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select s.*
                    from studente s, iscrizione i
                    where s.matricola = i.matricola
                    and i.codins = %s  """

        cursor.execute(query, (codins,))  # periodo didattico è un parametro che ci arriva dall'esterno

        res = []
        for row in cursor:  # ci serve una nuova DTO -> bisogna creare "studente.py"
            # ora possiamo creare oggetti di tipo Studente
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCDSofCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select s.CDS, count(*) as n
                from studente s, iscrizione i
                where s.matricola  = i.matricola 
                and i.codins = %s  
                and s.CDS != ""
                group by s.CDS 
                  """

        cursor.execute(query, (codins,))  # periodo didattico è un parametro che ci arriva dall'esterno

        res = []
        for row in cursor:
            res.append((row["CDS"], row["n"]))  # tupla: corso di studi - n iscritti

        cursor.close()
        cnx.close()
        return res


