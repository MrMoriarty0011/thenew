from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("TIC TAC TOE")

click = True

def checker(buttons):
    global click
    if buttons['text'] == " " and click == True:
        buttons["text"] == "x"
        click = False

    elif buttons["text"] == " " and click == False:
        buttons["text"] == "o"
        click = True

    elif (button1["text"] == "x" and button2["text"] == "x" and button3["text"] == "x" or
          button4["text"] == 'x' and button5["text"] == 'x' and button6['text'] == 'x' or
          button7["text"] == 'x' and button8["text"] == 'x' and button8['text'] == 'x' or
          button1["text"] == 'x' and button4["text"] == 'x' and button7['text'] == 'x' or
          button2["text"] == 'x' and button5["text"] == 'x' and button8['text'] == 'x' or
          button3["text"] == 'x' and button6["text"] == 'x' and button9['text'] == 'x' or
          button1["text"] == 'x' and button5["text"] == 'x' and button9['text'] == 'x' or
          button3["text"] == 'x' and button5["text"] == 'x' and button7['text'] == 'x'):
        tkinter.messagebox.showinfo('Winner X','You have won the game bitch')


    elif(button1['text']=='o' and button2['text']=='o' and button3['text']=='o' or
          button4['text'] == 'o' and button5['text'] == 'o' and button6['text'] == 'o' or
          button7['text'] == 'o' and button8['text'] == 'o' and button8['text'] == 'o' or
          button1['text'] == 'o' and button4['text'] == 'o' and button7['text'] == 'o' or
          button2['text'] == 'o' and button5['text'] == 'o' and button8['text'] == 'o' or
          button3['text'] == 'o' and button6['text'] == 'o' and button9['text'] == 'o' or
          button1['text'] == 'o' and button5['text'] == 'o' and button9['text'] == 'o' or
          button3['text'] == 'o' and button5['text'] == 'o' and button7['text'] == 'o'):
        tkinter.messagebox.showinfo('Winner O','You have won the game bitch')

buttons=StringVar()


button1 = Button(text=' ', font='Arial 26 bold', height=4, width=8, command=lambda: checker(button1))
button1.grid(row=1, column=0, sticky=S+N+E+W)
button2 = Button(text=' ', font='Arial 26 bold', height=4, width=8, command=lambda: checker(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)
button3 = Button(text=' ', font='Arial 26 bold', height=4, width=8, command=lambda: checker(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)
button4 = Button(text=' ', font='Arial 26 bold', height=4, width=8, command=lambda: checker(button4))
button4.grid(row=2, column=0, sticky=S+N+E+W)
button5 = Button(text=' ', font='Arial 26 bold', height=4, width=8, command=lambda: checker(button5))
button5.grid(row=2, column=1, sticky=S+N+E+W)
button6 = Button(text=' ', font='Arial 26 bold', height=4, width=8, command=lambda: checker(button6))
button6.grid(row=2, column=2, sticky=S+N+E+W)
button7 = Button(text=' ', font='Arial 26 bold', height=4, width=8, command=lambda: checker(button7))
button7.grid(row=3, column=0, sticky=S+N+E+W)
button8 = Button(text=' ', font='Arial 26 bold', height=4, width=8, command=lambda: checker(button8))
button8.grid(row=3, column=1, sticky=S+N+E+W)
button9 = Button(text=' ', font='Arial 26 bold', height=4, width=8, command=lambda: checker(button9))
button9.grid(row=3, column=2, sticky=S+N+E+W)

tk.mainloop()

