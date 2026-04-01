import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()

    """ handle - qualcosa: metodi che gestiscono dei bottoni """

    def handlePrintCorsiPD(self, e):
        pass

    def handlePrintIscrittiCorsiPD(self, e):
        pass

    def handlePrintIscrittiCodins(self, e):
        pass

    def handlePrintCDSCodins(self, e):
        pass

    """ metodo per riempire il drop down dei corsi: il controller lo prende dal modello"""
    def fillddCodins(self):
        # for cod in self._model.getCodins():
        #     self._view.ddCodins.options.append(
        #         ft.dropdown.Option(cod)
        #     )

        """ è più utile usare l'oggetto corsi piuttosto che la stringa codins"""
        for c in self._model.getAllCorsi():   # lo chiede al model
            self._view.ddCodins.options.append(ft.dropdown.Option(
                key = c.codins,   # stringa che viene visualizzata nel menu
                data = c,   # l'oggeto vero e proprio inserito del dd
                on_click = self._choiceDDCodins    # come x i bottoni: ci vogliamo salvare da qualche parte l'opzione che è stata selezionata per esempio
            ))
            pass

    def _choiceDDCodins(self, e):
        """ Metodo che legge la selezione dell'utente e la salva in una variabile locale"""
        self._ddCodinsValue = e.control.data
        print(self._ddCodinsValue)   # se selezioni una voce dal menu a tendina, troverai ancora il codice del corso ma quando LO CLICCHI nella console qui sotto ti dovrebbe stampare il corso vero e proprio (grazie al metodo __str__)