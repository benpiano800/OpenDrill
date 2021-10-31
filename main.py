# Main Source Code File For OpenDrill
# Version 0.1.0
from tkinter import *
from PyQt5 import QtWidgets, uic
import time
import sys
class project():
    def __init__(self, name):
        pass
    def export_dotsheet(self, filetype):
        if filetype == "pdf":
            pass
        elif filetype == "docx":
            pass
        elif filetype == "odt":
            pass
        elif filetype == "xlsx":
            pass
        elif filetype =="ods":
            pass
    def export_drillchart(self, filetype):
        if filetype == "pdf":
            pass
        elif filetype == "pptx":
            pass
        elif filetype == "odp":
            pass
    def export_video(self, filetype):
        if filetype == "mp4":
            pass
        elif filetype == "webm":
            pass
        elif filetype == "mkv":
            pass
class show():
    def __init__(self, movements):
        pass
class movement():
    def __init__(self, tempo, sets, music):
        pass
    def playmusic(self):
        pass
class drillset():
    def __init__(self, counts):
        pass
class marcher():
    def __init__(self, role, drillnum):
        if self.role == "SnareDrum":
            pass
        elif self.role == "TenorDrum":
            pass
        elif self.role == "BassDrum":
            pass
        elif self.role =="FlubDrum":
            pass
        elif self.role == "Cymbals":
            pass
        elif self.role == "Flute":
            pass
        elif self.role == "Clarinet":
            pass
        elif self.role == "BassClarinet":
            pass
        elif self.role == "SopranoSax":
            pass
        elif self.role == "AltoSax":
            pass
        elif self.role == "TenorSax":
            pass
        elif self.role == "BariSax":
            pass
        elif self.role == "Trumpet":
            pass
        elif self.role == "Mellophone":
            pass
        elif self.role == "Baritone":
            pass
        elif self.role == "Euphonium":
            pass
        elif self.role == "Trombone":
            pass
        elif self.role == "Tuba":
            pass
        elif self.role == "GuardFlag":
            pass
        elif self.role == "GuardRifle":
            pass
        elif self.role == "GuardSword":
            pass
        elif self.role == "GuardNoEquip":
            pass
        elif self.role == "Extra":
            pass
        else:
            raise Exception("INVALID")
    def draw(self):
        pass
    def move(self):
        pass
class prop():
    def __init__(self, dimensions):
        pass
    def draw(self):
        pass
class field():
    def __init__(self, nums, hashes):
        if self.nums == "HS":
            pass
        elif self.nums == "Col":
            pass
        elif self.nums == "Pro":
            pass
        else:
            raise Exception("INVALID")
        if self.hashes == "HS":
            pass
        elif self.hashes == "Col":
            pass
        elif self.hashes == "Pro":
            pass
        else:
            raise Exception("INVALID")
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("MainWindow.ui")
window.show()
app.exec()
