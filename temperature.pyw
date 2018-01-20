from tkinter import *

window = Tk()
window.title('Temperature conversion')

label = Label(window, text = 'Temperature conversion')

Label(window, text ='temperature in celcius').grid(row=2)

e1 = Entry(window)

def convert():
    C = e1.get()
    Cint = float(C)
    temperature = 1.8*Cint + 32
    temperature = round(temperature, 2)
    output1.configure(text = temperature)

output1 = Label(window, relief = 'groove', width = 10)
getBtn = Button(window)
resBtn = Button(window)

label.grid(row = 1, column = 1, padx = 50)
e1.grid(row = 2, column = 1, padx = 5, pady = 5)
output1.grid(row = 3, column = 1, padx = 50)
getBtn.grid(row = 2, column = 2, padx = 5)

getBtn.configure( text = 'convert', command = convert)

window.mainloop()
