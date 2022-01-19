from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser

WIDTH = 800
HEIGHT = 520

GEOMETRY = str(WIDTH) + "x" + str(HEIGHT)

FONT = "Segoe UI"

penColor = "black"
backgroundColor = "white"

def eraser():
	global backgroundColor
	global penColor

	penColor = backgroundColor

def clearAll():
	canvas.delete("all")

def selectBackgroundColor():
	global backgroundColor

	color = colorchooser.askcolor()

	backgroundColor = color[1]
	canvas.configure(background=backgroundColor)

def selectColor(color):
	global penColor

	penColor = color

def drawCircle(event):
	x1, y1 = (event.x - 2.5), (event.y - 2.5)
	x2, y2 = (event.x + 2.5), (event.y + 2.5)

	canvas.create_oval(x1, y1, x2, y2, fill=penColor, outline=penColor, width=penSize.get())

def drawCube(event):
	x1, y1 = (event.x - 2.5), (event.y - 2.5)
	x2, y2 = (event.x + 2.5), (event.y + 2.5)

	canvas.create_rectangle(x1, y1, x2, y2, fill=penColor, outline=penColor, width=penSize.get())

app = Tk()
app.title("SerrrPaint")
app.geometry(GEOMETRY)
app.resizable(width=False, height=False)
app.configure(background="white")

canvas = Canvas(app, bd=5, bg="white", relief=GROOVE, width=500, height=500)
canvas.place(x=100, y=0)

colorsFrame = LabelFrame(app, text="Color", font=(FONT, 15), bd=5, bg="white", relief=RIDGE)
colorsFrame.place(x=10, y=0, width=70, height=185)

COLORS = ["#ff0000", "#ff8000", "#ffff00", "#00ff00", "#00ffff", "#0000ff", "#000000", "#757575", "#ffffff"]

i=j=0

for color in COLORS:
	Button(colorsFrame, bd=2, bg=color, relief=RIDGE, width=3, command=lambda col = color:selectColor(col)).grid(row=i, column=j)

	i += 1

	if(i == 6):
		i = 0
		j = 1

eraserButton = Button(app, text="Eraser", font=(FONT, 12), bd=2, bg="white", relief=RIDGE, command=eraser)
eraserButton.place(x=WIDTH - 175, y=0)

clearAllButton = Button(app, text="Clear all", font=(FONT, 12), bd=2, bg="white", relief=RIDGE, command=clearAll)
clearAllButton.place(x=WIDTH - 175, y=50)

penSizeFrame = LabelFrame(app, text="Size", font=(FONT, 15), bd=5, bg="white", relief=RIDGE)
penSizeFrame.place(x=10, y=200, width=70, height=300)

penSize = Scale(penSizeFrame, orient=VERTICAL, from_=30, to=1, length=265)
penSize.grid(row=0, column=1, padx=15)

penSize.set(10)

backgroundColorButton = Button(app, text="BG color", font=(FONT, 12), bd=2, bg="white", relief=RIDGE, command=selectBackgroundColor)
backgroundColorButton.place(x=WIDTH - 175, y=100)

canvas.bind("<Button-1>", drawCircle)
canvas.bind("<Button-3>", drawCube)
canvas.bind("<B1-Motion>", drawCircle)
canvas.bind("<B3-Motion>", drawCube)

app.mainloop()