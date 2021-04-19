import os
import pygubu
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import serial

'''
GUI napisane przy pomocy biblioteki tkinter oraz pygubu designer
'''

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "simpleGUI.ui")

# Domyślne ustawienia:
ser = serial.Serial(
    port='COM2',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)


class SimpleguiApp:
    def __init__(self, parent):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('background', parent)
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    # Wybór COMa
    def choiceCOM1(self):
        ser.port = 'COM1'

    def choiceCOM2(self):
        ser.port = 'COM2'

    def choiceCOM3(self):
        ser.port = 'COM3'

    # Wybór bitu stopu
    def one(self):
        ser.stopbits = serial.STOPBITS_ONE

    def onePointFive(self):
        ser.stopbits = serial.STOPBITS_ONE_POINT_FIVE

    def two(self):
        ser.stopbits = serial.STOPBITS_TWO

    def loadFile(self):
        # Wybor pliku do otwarcia poprzez menu
        root.filename = filedialog.askopenfilename(initialdir="/", title="Wybierz plik", filetypes='')
        pass

    def saveFile(self):
        # Wybor pliku do zapisu poprzez menu
        root.filename = filedialog.asksaveasfilename(initialdir="/", title="Wybierz plik")

    # Wybór trybu
    def choiceCRC(self):
        root.quit()

    def choiceCRC(self):
        root.quit()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tytul')
    app = SimpleguiApp(root)
    app.run()
