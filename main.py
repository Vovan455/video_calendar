from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer

from ui import Ui_MainWindow

import os
from datetime import date

app = QApplication([])
win = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(win)

media =QMediaPlayer ()
media.setVideoOutput(ui.videoWidget)

today = date.today().day
filepath = os.path.join("Video", str(today)+".avi")

media.setSource(QUrl.fromLocalFile(filepath))
media.play()

ui.start_btn.clicked.connect(media.play)
ui.stop_btn.clicked.connect(media.stop)

def get_date():

    day = str(ui.calendarWidget.selectedDate().day())

    filepath = os.path.join("Video", day+".avi" )
    media.setSource(QUrl.fromLocalFile(filepath))

    if ui.autoplay_check.isChecked():
        media.play()

ui.calendarWidget.selectionChanged.connect(get_date)    



win.show()
app.exec()