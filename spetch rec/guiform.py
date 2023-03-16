import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import speech_recognition as sr
import os
import sys
import webbrowser
import time
import subprocess
import shlex
from textblob import TextBlob

status = ''

def talk(words):
	print(words)

def command():
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		print("Говорите")
		status = 'say'
		r.pause_threshold = 0.5
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
		
	try:
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		text = zadanie # Reading the file 
		textBlb = TextBlob(text) # Making our first textblob 
		textCorrected = textBlb.correct() # Correcting the text 
#		print(f"Text Corrector: {textCorrected}") 
		print("Вы сказали: " + zadanie)
		f = open( 'text.txt', 'w' )
		f.write(f"{time.ctime()} - {zadanie}\n")
		f.close()
	except sr.UnknownValueError:
		status = 'unknwn'
		talk("Я вас не поняла")
		zadanie = command()
	except sir.RequestError:
		print("Код Ошибки: 502")
		
	return zadanie
	
def comanding(zadanie):
	print()
	
#####


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		state = "Включить запись"
		self.setWindowTitle("Voice Recognizer")
		self.setFixedSize(QSize(400, 300))
		widget = QPushButton(state)
		widget.setCheckable(True)
		widget.clicked.connect(self.the_button_was_clicked)
		widget.clicked.connect(self.the_button_was_toggled)

		self.setCentralWidget(widget)

	def the_button_was_clicked(self):
		print("Clicked!")

	def the_button_was_toggled(self, checked):
#		if checked==1:
		while checked==1:
			comanding(command())
			checked=False
		else:
			print("", checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()