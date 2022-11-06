from PyQt5.QtWidgets import QApplication
from smart import *
import json

notes = {
    "Ласкаво просимо!": {
         "текст": "Це програма для створення заміток ...",
         "тегі": ["інструкція", "про програму"]
    }
}

with open("notes.json", "w", encoding="utf-8") as file:
    json.dump(notes, file)

app = QApplication([])

wind = Ui_Form()
wind.setupUi(wind)
wind.show()

app.exec_()
