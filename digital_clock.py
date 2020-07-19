
try:

	import sys
	# importing whole module
	from tkinter import *
	from tkinter.ttk import *
	from time import strftime
	import time


	root = Tk()
	root.title("A Digital Clock")

	def clock():
	    Strr = strftime("%a/%H:%M:%S:%p ")
	    design.config(text = Strr)
	    design.after(100,clock)


	design = Label(root, font = ('Arial',70, 'bold'),
				background = 'Yellow',
				foreground = 'Black'
	                )
	design.grid(row = 0,column = 2)
	design.pack(anchor = 'center')
	clock()
	root.mainloop()

except ModuleNotFoundError as e:
	#print("\nModule Not Found: Run 'bash requerments.ssh'\n")
	print(e)
except KeyboardInterrupt:
	print("\n\nManually Killed The Task. GoodBye\n")