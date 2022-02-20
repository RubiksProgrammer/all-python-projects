from random import randint
from time import time
from time import sleep
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class TheGame(BoxLayout):

	def __init__(self,**kwargs):

		super(TheGame, self).__init__(**kwargs)

		self.label1 = self.ids.numlabel
		self.label2 = self.ids.timelabel
		self.txtinput = self.ids.my_input
		self.directions = self.ids.directions
		self.button = self.ids.mybutton

	def myfunc(self):
		number = randint(10,100)
		self.label1.text = f"What is {number} squared?"
		return number

	def answer(self, number):
		while True:
			while True:
				try:
					myanswer = int(self.txtinput.text)
				except:
					self.directions.text = "That is not an integer. Please enter a different number."
					self.txtinput.text = ""
				else:
					break
			if myanswer == number**2:
				self.directions.text = 'You got the answer right!'
				break
			else:
				self.directions.text = "Wrong answer! Try again."
				self.txtinput.text = ""

	def replay(self):
		return True

class SquaringGameApp(App):
	def build(self):
		game = TheGame()
		t = time()
		game.myfunc()
		game.answer(game.myfunc())
		game.label2.text = f'It took you {time() - t:2.2f} seconds.'

		return game
			
if __name__ == "__main__":
		SquaringGameApp().run()



