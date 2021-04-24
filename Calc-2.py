from tkinter import *
from tkinter.messagebox import *

#some useful variables
font = ('Verdana', 15, 'bold')

#some useful function
def all_clear():
    textField.delete(0, END)


def clear():
    ex = textField.get()
    ex = ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)


def click_btn_function(event):
    print("btn clicked")
    b = event.widget #fetch clicked button
    text = b['text']
    print(text)

    if text == 'x':
        textField.insert(END, '*')
        return  

    if text == '=':
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)
        except Exception as e:
            print("Error..", e)
            showerror("Error", e)
        
        return

    textField.insert(END, text)


#creating a window
window = Tk()
window.title('General Calculator')
window.geometry('500x400')
#picture label
pic = PhotoImage(file = 'calculatorPic.PNG')
headingLabel = Label(window, image = pic)
headingLabel.pack(side = TOP, pady = 5)

'''
#heading label
heading = Label(window,  text = 'My Calculator', font = ('Verdana', 10, 'bold'))
heading.pack(side = TOP)
'''

#text field
textField = Entry(window, font = ('Verdana', 20, 'bold'))
textField.pack(side = TOP, padx = 5, pady = 5, fill = X)

#button
buttonFrame = Frame(window)
buttonFrame.pack(side = TOP)

#adding button
temp = 1
for i in range(0,3):
    for j in range(0,3):
        btn = Button(buttonFrame, text = str(temp), font = ('Verdana', 15, 'bold'), relief = 'ridge', activebackground = 'yellow', activeforeground = 'black')
        btn.grid(row = i, column = j, padx = 5, pady = 5)
        temp = temp+1
        btn.bind('<Button-1>', click_btn_function) #event object creating each click

dotBtn = Button(buttonFrame, text = '.', font = ('Verdana', 15, 'bold'), relief = 'ridge',activebackground = 'yellow', activeforeground = 'black')
dotBtn.grid(row = 3, column = 0, padx = 5, pady = 5)
dotBtn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text = '0', font = ('Verdana', 15, 'bold'), relief = 'ridge',activebackground = 'yellow', activeforeground = 'black')
zeroBtn.grid(row = 3, column = 1, padx = 5, pady = 5)
zeroBtn.bind('<Button-1>', click_btn_function)

equalBtn = Button(buttonFrame, text = '=', font = ('Verdana', 15, 'bold'), relief = 'ridge',activebackground = 'yellow', activeforeground = 'black')
equalBtn.grid(row = 3, column = 2, padx = 5, pady = 5)
equalBtn.bind('<Button-1>', click_btn_function)

plusBtn = Button(buttonFrame, text = '+', font = ('Verdana', 15, 'bold'), relief = 'ridge', activebackground = 'yellow', activeforeground = 'black')
plusBtn.grid(row = 0, column = 3, padx = 5, pady = 5)
plusBtn.bind('<Button-1>', click_btn_function)

minusBtn = Button(buttonFrame, text = '-', font = ('Verdana', 15, 'bold'), relief = 'ridge', activebackground = 'yellow', activeforeground = 'black')
minusBtn.grid(row = 1, column = 3, padx = 5, pady = 5)
minusBtn.bind('<Button-1>', click_btn_function)

multBtn = Button(buttonFrame, text = 'x', font = ('Verdana', 15, 'bold'), relief = 'ridge', activebackground = 'yellow', activeforeground = 'black')
multBtn.grid(row = 2, column = 3, padx = 5, pady = 5)
multBtn.bind('<Button-1>', click_btn_function)

divBtn = Button(buttonFrame, text = '/', font = ('Verdana', 15, 'bold'), relief = 'ridge', activebackground = 'yellow', activeforeground = 'black')
divBtn.grid(row = 3, column = 3, padx = 5, pady = 5)
divBtn.bind('<Button-1>', click_btn_function)

clearBtn = Button(buttonFrame, text = 'AC', font = ('Verdana', 15, 'bold'), relief = 'ridge', activebackground = 'yellow', activeforeground = 'black', command = all_clear)
clearBtn.grid(row = 0, column = 4, padx = 5, pady = 5)


bkspsBtn = Button(buttonFrame, text = 'CE', font = ('Verdana', 15, 'bold'), relief = 'ridge', activebackground = 'yellow', activeforeground = 'black', command = clear)
bkspsBtn.grid(row = 1, column = 4, padx = 5, pady = 5)




window.mainloop()