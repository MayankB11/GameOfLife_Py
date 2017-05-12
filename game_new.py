from tkinter import *
import random

class Game:
	def __init__(self):
		self.buttons = 2500
		self.createButtons()

	def createButtons(self):
		self.buttons = {}
		for i in range(0,400):
			status = random.choice([1,0])
			self.buttons[i] = [Button(root,bg='yellow' if status == 1 else 'black'),status]
			self.buttons[i][0].grid(row = i//20,column = i%20)

	def run(self):
		self.buttons_new = {}
		for k in range(0,400):
			status = self.buttons[k][1]
			row = k//20
			column = k%20
			c = 0
			for i in [row-1,row,row+1]:
				for j in [column-1,column,column+1]:
					if self.validButton(i,j):
						c = c + self.buttons[i*j][1]
			if c <=1 or c>=4 :
				self.buttons_new[k] = [self.buttons[k][0],0]
				self.buttons[k][0].configure(bg='black')
			else:
				self.buttons_new[k] = [self.buttons[k][0],1]
				self.buttons[k][0].configure(bg='yellow')
		self.buttons = self.buttons_new
		root.after(500,self.run)

	def validButton(self,i,j):
		if i<0 or j<0 or j>19 or i> 19:
			return False
		else:
			return True

def main():
    global root
    root = Tk()
    root.title('Game Of Life')
    game = Game()
    root.after(500,game.run)
    root.mainloop()

if __name__ == '__main__':
    main()