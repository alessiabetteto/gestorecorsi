import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()
        self._ddCodinsValue = None

    """ handle - qualcosa: metodi che gestiscono dei bottoni. evento dovuto alla pressione del pulsante"""

    def handlePrintCorsiPD(self, e):
        self._view.txt_result.controls.clear()


        """deve recuperare dall'interfaccia grafica il PD, fare la query al db tramite il model e poi stamparli"""
        pd = self._view.ddPD.value # mi restituisce I o II, o None se l'utente non passa nulla
        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico")
            self._view.update_page()
            return

        if pd == "I":
            pdInt = 1
        else: pdInt = 2

        corsiPD = self._model.getCorsiPD(pdInt)   #getCorsiPD è una lista

        # la lista potrebbe essere vuota
        if not len(corsiPD):
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pd} periodo didattico:"))
            self._view.update_page()
            return

        # se la lista contiene elementi
        self._view.txt_result.controls.append(ft.Text(f"Di seguito i corsi dei {pd} periodo didattico:"))
        for c in corsiPD:
            self._view.txt_result.controls.append(ft.Text(c))
        self._view.update_page()



    def handlePrintIscrittiCorsiPD(self, e):
        self._view.txt_result.controls.clear()

        pd = self._view.ddPD.value  # mi restituisce I o II, o None se l'utente non passa nulla
        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico")
            self._view.update_page()
            return
        if pd == "I":
            pdInt = 1
        else: pdInt = 2

        corsi = self._model.getCorsiPDwIscritti(pdInt)
        if not len(corsi):
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pd} periodo didattico:"))
            self._view.update_page()
            return
        self._view.txt_result.controls.append(ft.Text(f"Di seguito i corsi dei {pd} periodo didattico con dettaglio iscritti:"))
        for c in corsi:  # c è una tupla
            self._view.txt_result.controls.append(ft.Text(f"{c[0]} -- N Iscritti: {c[1]}"))
        self._view.update_page()

    def handlePrintIscrittiCodins(self, e):
        # se non hai scelto nulla nel drop downn, scegli
        self._view.txt_result.controls.clear()

        if self._ddCodinsValue is None:
            self._view.create_alert("Per favore selezionare un insegnamento")
            self._view.update_page()
            return

        # se arriviamo qui, posso recuperare gli studenti
        studenti = self._model.getStudentiCorso(self._ddCodinsValue.codins)  # _ddCodinsValue è un oggetto di tipo Corso che ha tra gli attributi codins

        # se la lista studenti è vuota
        if not len(studenti):
            self._view.txt_result.controls.append(ft.Text("Nessuno studente iscritto a questo corso"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(ft.Text(f"Di seguito gli studenti iscritti al corso {self._ddCodinsValue} "))
        for s in studenti:
            self._view.txt_result.controls.append(ft.Text(s))
        self._view.update_page()


    def handlePrintCDSCodins(self, e):
        self._view.txt_result.controls.clear()

        if self._ddCodinsValue is None:
            self._view.create_alert("Per favore selezionare un insegnamento")
            self._view.update_page()
            return

        cds = self._model.getCDSofCorso(self._ddCodinsValue.codins)   # cds è una lista di tuple
        if not len(cds):
            self._view.text_result.controls.append(ft.Text(f"Nessun CDS afferente al corso {self._ddCodinsValue} "))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(ft.Text(f"Di seguito i CDS che frequentano il corso {self._ddCodinsValue} "))
        for c in cds:
            self._view.txt_result.controls.append(ft.Text(f"{c[0]} - N iscritti:{c[1]}"))
        self._view.update_page()



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