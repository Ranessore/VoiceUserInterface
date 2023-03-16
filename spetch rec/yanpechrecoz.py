import speech_recognition as sr
import os
import sys
import webbrowser
import time
import subprocess
import shlex
from tkinter import *
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
		print(f"Text Corrector: {textCorrected}") 
		print("Вы сказали: " + zadanie)
		f = open( 'text.txt', 'w' )
		f.write(f"{time.ctime()} - {zadanie}\n")
		f.close()
	except sr.UnknownValueError:
		status = 'unknwn'
		talk("Я вас не поняла")
#		ahk.key_press('Space')
		zadanie = command()
		
	return zadanie
	
def comanding(zadanie):
	print()

while True:
	comanding(command())