from tkinter import *

window = Tk()

txt = Entry(window)
txt.grid(row = 0, column = 0, columnspan = 4, ipadx = 30)

b1 = Button(window, text = "1", height = 3, width = 5)
b1.grid(row = 2, column = 0)

b2 = Button(window, text = "2", height = 3, width = 5)
b2.grid(row = 2, column = 1)

b3 = Button(window, text = "3", height = 3, width = 5)
b3.grid(row = 2, column = 2)

b4 = Button(window, text = "4", height = 3, width = 5)
b4.grid(row = 3, column = 0)

b5 = Button(window, text = "5", height = 3, width = 5)
b5.grid(row = 3, column = 1)

b6 = Button(window, text = "6", height = 3, width = 5)
b6.grid(row = 3, column = 2)

b7 = Button(window, text = "7", height = 3, width = 5)
b7.grid(row = 4, column = 0)

b8 = Button(window, text = "8", height = 3, width = 5)
b8.grid(row = 4, column = 1)

b9 = Button(window, text = "9", height = 3, width = 5)
b9.grid(row = 4, column = 2)

b0 = Button(window, text = "0", height = 3, width = 5)
b0.grid(row = 5, column = 0)

plusButton = Button(window, text = "+", height = 3, width = 5)
plusButton.grid(row = 2, column = 3)

minusButton = Button(window, text = "-", height = 3, width = 5)
minusButton.grid(row = 3, column = 3)

multiButton = Button(window, text = "*", height = 3, width = 5)
multiButton.grid(row = 4, column = 3)

divButton = Button(window, text = "/", height = 3, width = 5)
divButton.grid(row = 5, column = 3)

clearButton = Button(window, text = "CLEAR", height = 3, width = 5)
clearButton.grid(row = 5, column = 1)

equalButton = Button(window, text = "=", height = 3, width = 5)
equalButton.grid(row = 5, column = 2)

window.mainloop()
