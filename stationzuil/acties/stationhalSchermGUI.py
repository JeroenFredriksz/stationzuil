import tkinter
from tkinter import  ttk

from stationzuil.util import StationsManager
from stationzuil.data import PostgresDataBaseEditor
class MyGUI:
    def __init__(self):
        self.root = tkinter.Tk()

        self.stations = StationsManager.getAllStations()
        self.clickedStation = None

        self.root.geometry("600x400")
        self.root.title("halscherm")

        self.startScherm = tkinter.ttk.Frame(self.root)
        self.startScherm.place(y=800, width=200, height=200)
        self.startScherm.pack()

        self.kiesStationLabel = ttk.Label(self.startScherm, text="Kies een van de 3 stations hieronder", font=("arial", 20))
        self.kiesStationLabel.pack(pady=50)

        self.buttonGridFrame = ttk.Frame(self.startScherm)
        self.buttonGridFrame.columnconfigure(0, weight=1)
        self.buttonGridFrame.columnconfigure(1, weight=1)
        self.buttonGridFrame.columnconfigure(2, weight=1)

        self.buttonStation1 = tkinter.Button(self.buttonGridFrame, text=self.stations[0], font=('arial', 18), command=self.buttonStation1Click)
        self.buttonStation1.grid(row=0, column=0, sticky=tkinter.W + tkinter.E)

        self.buttonStation2 = tkinter.Button(self.buttonGridFrame, text=self.stations[1], font=('arial', 18), command=self.buttonStation2Click)
        self.buttonStation2.grid(row=0, column=1, sticky=tkinter.W + tkinter.E)

        self.buttonStation3 = tkinter.Button(self.buttonGridFrame, text=self.stations[2], font=('arial', 18), command=self.buttonStation3Click)
        self.buttonStation3.grid(row=0, column=2, sticky=tkinter.W + tkinter.E)

        self.buttonGridFrame.pack(pady=100, fill=tkinter.X)

        self.messageFrame = tkinter.Frame(self.root)
        self.berichten = PostgresDataBaseEditor.getLaatste5Berichten()


        self.labelBericht1 = tkinter.Label(self.messageFrame, text="dit is een groot bericht om te tonen")
        self.labelBericht1.pack()

        self.root.mainloop()



    def buttonStation1Click(self):
        self.clickedStation = self.stations[0]
        self.switchToMessageFrame(self.clickedStation)
        return

    def buttonStation2Click(self):
        self.clickedStation = self.stations[1]
        self.switchToMessageFrame(self.clickedStation)
        return

    def buttonStation3Click(self):
        self.clickedStation = self.stations[2]
        self.switchToMessageFrame(self.clickedStation)
        return
    def switchToMessageFrame(self, station):
        self.startScherm.destroy()
        self.messageFrame.pack()
        print(station)

MyGUI()