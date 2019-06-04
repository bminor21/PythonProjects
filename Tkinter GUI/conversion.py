from tkinter import *

# Button functions
def convert():
    clear()
    try:
        kg = float(entryField.get())
        gramsText.insert(END, kg*1000)
        poundsText.insert(END, kg*2.20462)
        ouncesText.insert(END, kg*35.274)
    except ValueError:
        pass

def clear():
    gramsText.delete('1.0', END)
    poundsText.delete('1.0', END)
    ouncesText.delete('1.0', END)

# Define the window
window=Tk(className='Kg Conversion Tool')

#Variables
kgInput=StringVar()

#Components
kgLabel=Label(window, text='Kg')
entryField=Entry(window, textvariable=kgInput)
convertBtn=Button(window, text='Convert', command=convert)
gramsText=Text(window, height=1, width=20)
poundsText=Text(window, height=1, width=20)
ouncesText=Text(window, height=1, width=20)

#Component Placement
kgLabel.grid(row=0, column=0)
entryField.grid(row=0, column=1)
convertBtn.grid(row=0, column=2)
gramsText.grid(row=1, column=0)
poundsText.grid(row=1, column=1)
ouncesText.grid(row=1, column=2)

# Start the main loop
window.mainloop()
