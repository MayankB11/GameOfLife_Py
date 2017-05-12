from tkinter import *
import random

class Game:
	def __init__(self):
		self.buttons = 2500
		self.createButtons()

	def createButtons(self):
		self.buttons = {}
		row = 0
		col = 0
		for i in range(0,400):
			status = random.choice([1,0])
			self.buttons[i] = [Button(root,bg='yellow' if status == 1 else 'black'),status]
			self.buttons[i][0].grid(row = i//20,column = i%20)
def main():
    global root
    root = Tk()
    root.title('Game Of Life')
    game = Game()
    root.mainloop()

if __name__ == '__main__':
    main()