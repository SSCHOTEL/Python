from tkinter import *
import tkinter.messagebox
import requests
import pycountry
import datetime
import numbers
from currency_converter import CurrencyConverter

c = CurrencyConverter()
root = Tk()
root.geometry("400x210")#Specifying how I want my window displayed.
root.resizable(False, False) #Prevents resizing.
root.title("Currency Converter")
title = Label(root, text = "Currency Converter", font = ('Helvetica', 30), fg = '#778899' , bg = '#A2B5CD', height = 2) #A title displayed at the top.
title.pack(fill = X)

frame = Frame(root)
frame.pack()

display = PanedWindow(frame)
display.grid(row = 0)

button = PanedWindow(frame)
button.grid(row =8)

buttonDec = Button(button, text = " Convert ", font = ('Helvetica', 20, 'italic'), fg = '#BAB2B2', bg = 'gray44', width = 10, command = lambda : Click('convert')) #Lambda implemented to give buttons functionality.
buttonDec.grid(row = 8, column = 1, padx = 10, pady = 40)

def letsconvert():
    root2 = Tk()
    root2.geometry("350x430")#Specifying how I want my window displayed.
    root2.resizable(False, False) #Prevents resizing.
    root2.title("Currency Converter")
    title = Label(root2, text = "Currency Converter", font = ('Helvetica', 30), fg = '#778899' , bg = '#A2B5CD', height = 2) #A title displayed at the top.
    title.pack(fill = X)
    frame = Frame(root2)
    frame.pack()
    display = PanedWindow(frame)
    display.grid(row = 0)
    button = PanedWindow(frame)
    button.grid(row =8)

    currencies = ['USD', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'NOK', 'HRK', 'RUB', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB','ZAR', 'ISK']

    l1 = Label(display, text='Enter Value of Money: ', font=('Arial', 15))
    l1.grid(row=2,column=5, pady =5)
    entry = Entry(display, width = 20, font = ('Arial', 15), bd = 1)
    entry.grid(row = 3, column = 5, pady = 10)

    Lb1 = Listbox(root2)
    Lb1.insert(1, "Select")
    Lb1.insert(2, currencies[0])
    Lb1.insert(3, currencies[1])
    Lb1.insert(4, currencies[2])
    Lb1.insert(5, currencies[3])
    Lb1.insert(6, currencies[4])
    Lb1.insert(7, currencies[5])
    Lb1.insert(8, currencies[6])
    Lb1.insert(9, currencies[7])
    Lb1.insert(10, currencies[8])
    Lb1.pack()

    def submitFunction():
        value = entry.get()
        if value == "":
            tkinter.messagebox.showerror("Invalid Entry", "Enter Required Fields.")
        else:
            if Lb1.get(ANCHOR) == "Select":
                tkinter.messagebox.showerror("Invalid Entry", "Select Choice.")
            else:
                lstbox=Lb1.get(ANCHOR)
                if value.isdigit()==False:
                    tkinter.messagebox.showerror("Invalid Entry", "Enter Integer Only.")
                else:
                    root2.destroy()
                    root3 = Tk()
                    root3.geometry("380x500")#Specifying how I want my window displayed.
                    root3.resizable(False, False) #Prevents resizing.
                    root3.title("Currency Converter")
                    title = Label(root3, text = "Currency Converter", font = ('Helvetica', 30), fg = '#778899' , bg = '#A2B5CD', height = 2) #A title displayed at the top.
                    title.pack(fill = X)
                    frame = Frame(root3)
                    frame.pack()
                    display = PanedWindow(frame)
                    display.grid(row = 0)
                    button = PanedWindow(frame)
                    button.grid(row =8)

                    l1 = Label(root3, text='', font=('Arial', 15))
                    l1.pack()
                    l1 = Label(root3, text='Select Currency to Exchange', font=('Arial', 15))
                    l1.pack()
                    l1 = Label(root3, text='', font=('Arial', 15))
                    l1.pack()
                    l1 = Label(root3, text='', font=('Arial', 15))
                    l1.pack()
                    Lb3 = Listbox(root3)
                    Lb3.insert(1, "Select")
                    Lb3.insert(2, currencies[0])
                    Lb3.insert(3, currencies[1])
                    Lb3.insert(4, currencies[2])
                    Lb3.insert(5, currencies[3])
                    Lb3.insert(6, currencies[4])
                    Lb3.insert(7, currencies[5])
                    Lb3.insert(8, currencies[6])
                    Lb3.insert(9, currencies[7])
                    Lb3.insert(10, currencies[8])
                    Lb3.pack()

                    def exchange():
                        output_cur=Lb3.get(ANCHOR)
                        input_cur=lstbox
                        data = c.convert(value, input_cur, output_cur)
                        root3.destroy()
                        root4 = Tk()
                        root4.geometry("400x430")#Specifying how I want my window displayed.
                        root4.resizable(False, False) #Prevents resizing.
                        root4.title("Currency Converter")
                        title = Label(root4, text = "Currency Converter", font = ('Helvetica', 30), fg = '#778899' , bg = '#A2B5CD', height = 2) #A title displayed at the top.
                        title.pack(fill = X)
                        frame = Frame(root4)
                        frame.pack()
                        display = PanedWindow(frame)
                        display.grid(row = 0)
                        button = PanedWindow(frame)
                        button.grid(row =8)

                        text44 = Label(root4, text = "Amount: "+value+""+input_cur, font = ('Helvetica', 30), fg = '#778899' , bg = '#A2B5CD', height = 2) #A title displayed at the top.
                        text44.pack()
                        text44 = Label(root4, text = "Exchanged: "+str(format(data, '.2f'))+""+output_cur, font = ('Helvetica', 30), fg = '#778899' , bg = '#A2B5CD', height = 2) #A title displayed at the top.
                        text44.pack()

                        root4.mainloop()


                    submit = Button(root3, text='Exchange', command=exchange)#on execution, Student name is grabbed and then a panel of information is displayed.
                    submit.place(x=200,y=386,height=30,width=120)

        





                        
                    root3.mainloop()

    l1 = Label(display, text='Original Currency: ', font=('Arial', 15))
    l1.grid(row=80,column=5, pady =5)
    submit = Button(root2, text='Continue', command=submitFunction)#on execution, Student name is grabbed and then a panel of information is displayed.
    submit.place(x=200,y=386,height=30,width=120)


    root2.mainloop()



def Click(val):
        if(val == 'convert'):
            root.destroy()
            letsconvert()



root.mainloop()