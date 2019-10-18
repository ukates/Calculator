from tkinter import *

window = Tk()
window.configure(background = 'black')
window.wm_title("Calculator")

txt = Entry(window, background = 'black', fg = 'white', font = ("Open Sans", "10"))
txt.grid(row = 0, column = 0, columnspan = 4, ipadx = 40, ipady = 6)

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['+', '-', '*', '/', 'CLEAR', '=']
numberButtons = []
symbolButtons = []
buttonNumber = 0
symbolNumber = 0

for num in numbers:
    numberButtons.append(Button(window, text = num, height = 3, width = 6, highlightthickness = 0, background = '#3F3F3F', fg = 'white', font = ("Open Sans", "10")))
    buttonNumber += 1
for sym in symbols:
    symbolButtons.append(Button(window, text = sym, height = 3, width = 6, highlightthickness = 0, background = '#468500', fg = 'white', font = ("Open Sans", "10")))
    symbolNumber += 1
numberButtons[0].grid(row = 2, column = 0)
numberButtons[1].grid(row = 2, column = 1)
numberButtons[2].grid(row = 2, column = 2)
numberButtons[3].grid(row = 3, column = 0)
numberButtons[4].grid(row = 3, column = 1)
numberButtons[5].grid(row = 3, column = 2)
numberButtons[6].grid(row = 4, column = 0)
numberButtons[7].grid(row = 4, column = 1)
numberButtons[8].grid(row = 4, column = 2)
numberButtons[9].grid(row = 5, column = 0)

symbolButtons[0].grid(row = 2, column = 3)
symbolButtons[1].grid(row = 3, column = 3)
symbolButtons[2].grid(row = 4, column = 3)
symbolButtons[3].grid(row = 5, column = 3)
symbolButtons[4].grid(row = 5, column = 1)
symbolButtons[5].grid(row = 5, column = 2)
# b1 = Button(window, text = "1", height = 3, width = 6, highlightthickness = 0, background = '#3F3F3F', fg = 'white', font = ("Open Sans", "10"))
# b1.grid(row = 2, column = 0)
#
# b2 = Button(window, text = "2", height = 3, width = 6, highlightthickness = 0, background = '#3F3F3F', fg = 'white', font = ("Open Sans", "10"))
# b2.grid(row = 2, column = 1)
#
# b3 = Button(window, text = "3", height = 3, width = 6, highlightthickness = 0, background = '#3F3F3F', fg = 'white', font = ("Open Sans", "10"))
# b3.grid(row = 2, column = 2)
#
# b4 = Button(window, text = "4", height = 3, width = 6, highlightthickness = 0, background = '#3F3F3F', fg = 'white', font = ("Open Sans", "10"))
# b4.grid(row = 3, column = 0)
#
# b5 = Button(window, text = "5", height = 3, width = 6, highlightthickness = 0, background = '#3F3F3F', fg = 'white', font = ("Open Sans", "10"))
# b5.grid(row = 3, column = 1)
#
# b6 = Button(window, text = "6", height = 3, width = 6, highlightthickness = 0, background = '#3F3F3F', fg = 'white', font = ("Open Sans", "10"))
# b6.grid(row = 3, column = 2)
#
# b7 = Button(window, text = "7", height = 3, width = 6, highlightthickness = 0, background = '#3F3F3F', fg = 'white', font = ("Open Sans", "10"))
# b7.grid(row = 4, column = 0)
#
# b8 = Button(window, text = "8", height = 3, width = 6, highlightthickness = 0, background = '#3F3F3F', fg = 'white', font = ("Open Sans", "10"))
# b8.grid(row = 4, column = 1)
#
# b9 = Button(window, text = "9", height = 3, width = 6, highlightthickness = 0, background = '#3F3F3F', fg = 'white', font = ("Open Sans", "10"))
# b9.grid(row = 4, column = 2)
#
# b0 = Button(window, text = "0", height = 3, width = 6, highlightthickness = 0, background = '#3F3F3F', fg = 'white', font = ("Open Sans", "10"))
# b0.grid(row = 5, column = 0)

# plusButton = Button(window, text = "+", height = 3, width = 6, highlightthickness = 0, background = '#468500', fg = 'white', font = ("Open Sans", "10"))
# plusButton.grid(row = 2, column = 3)
#
# minusButton = Button(window, text = "-", height = 3, width = 6, highlightthickness = 0, background = '#468500', fg = 'white', font = ("Open Sans", "10"))
# minusButton.grid(row = 3, column = 3)
#
# multiButton = Button(window, text = "*", height = 3, width = 6, highlightthickness = 0, background = '#468500', fg = 'white', font = ("Open Sans", "10"))
# multiButton.grid(row = 4, column = 3)
#
# divButton = Button(window, text = "/", height = 3, width = 6, highlightthickness = 0, background = '#468500', fg = 'white', font = ("Open Sans", "10"))
# divButton.grid(row = 5, column = 3)
#
# clearButton = Button(window, text = "CLEAR", height = 3, width = 6, highlightthickness = 0, background = '#468500', fg = 'white', font = ("Open Sans", "10"))
# clearButton.grid(row = 5, column = 1)
#
# equalButton = Button(window, text = "=", height = 3, width = 6, highlightthickness = 0, background = '#468500', fg = 'white', font = ("Open Sans", "10"))
# equalButton.grid(row = 5, column = 2)

window.mainloop()
