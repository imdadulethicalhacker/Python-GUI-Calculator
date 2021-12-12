from tkinter import *

def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    scvalue.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    scvalue.set("")

def split(word):
    return [char for char in word]


def btnEqualsInput():
    global operator
    # opt1 = operator
    try:
        if "%" in split(operator):
            operator = operator.replace("%", "/100")
            sumup = str(eval(operator))
            scvalue.set(sumup)
            operator = ""
        else:    
            sumup = str(eval(operator))
            scvalue.set(sumup)
            operator = ""
    except:
        operator = "_ERROR_"
        scvalue.set(operator)


def clear_button():                                               # 'clear_button' function clears the last input item
    global operator
    operator = ""
    scvalue.set(scvalue.get()[0:-1])
    # operator = ""

# def percent_calc(operator):
#     operator1= "%"
#     operator = "/100"




root = Tk()
root.title("Imdadul - Title of My GUI")
img = PhotoImage(file='D:\\Coding\\My_Practis\\python\\calculator\\c.png')
root.iconphoto(False,img)
operator = ""
scvalue = StringVar()

screen = Entry(root,font=('arial',20,'bold'), textvariable=scvalue, bd=30,insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)

#========================================================================================
btnc = Button(root, text="C",pady=16, padx=14, bd=8, fg="white", font="arial 20 bold",bg="green",command=btnClearDisplay).grid(row=1,column=0)
btnp =  Button(root, text="%",pady=16, padx=12, bd=8, fg="white", font="arial 20 bold",bg="green",command=lambda:btnclick("%")).grid(row=1,column=1)
btnb =  Button(root, text="⌫",pady=16, padx=5, bd=8, fg="white", font="arial 20 bold",bg="green",command=lambda:clear_button()).grid(row=1,column=2)
btnd =  Button(root, text="÷",pady=16, padx=13, bd=8, fg="white", font="arial 20 bold",bg="green",command=lambda:btnclick("÷")).grid(row=1,column=3)

#========================================================================================
btn7 =  Button(root, text="7",pady=16, padx=16, bd=8, fg="black", font="arial 20 bold",bg="powder blue",command=lambda:btnclick(7)).grid(row=2,column=0)
btn8 =  Button(root, text="8",pady=16, padx=16, bd=8, fg="black", font="arial 20 bold",bg="powder blue",command=lambda:btnclick(8)).grid(row=2,column=1)
btn9 =  Button(root, text="9",pady=16, padx=16, bd=8, fg="black", font="arial 20 bold",bg="powder blue",command=lambda:btnclick(9)).grid(row=2,column=2)
btnm =  Button(root, text="*",pady=16, padx=16, bd=8, fg="white", font="arial 20 bold",bg="green",command=lambda:btnclick("*")).grid(row=2,column=3)


#========================================================================================
btn4 =  Button(root, text="4",pady=16, padx=16, bd=8, fg="black", font="arial 20 bold",bg="powder blue",command=lambda:btnclick(4)).grid(row=3,column=0)
btn5 =  Button(root, text="5",pady=16, padx=16, bd=8, fg="black", font="arial 20 bold",bg="powder blue",command=lambda:btnclick(5)).grid(row=3,column=1)
btn6 =  Button(root, text="6",pady=16, padx=16, bd=8, fg="black", font="arial 20 bold",bg="powder blue",command=lambda:btnclick(6)).grid(row=3,column=2)
btndv = Button(root, text="-",pady=16, padx=16, bd=8, fg="white", font="arial 20 bold",bg="green",command=lambda:btnclick("-")).grid(row=3,column=3)

#========================================================================================
btn1 =  Button(root, text="1",pady=16, padx=16, bd=8, fg="black", font="arial 20 bold",bg="powder blue",command=lambda:btnclick(1)).grid(row=4,column=0)
btn2 =  Button(root, text="2",pady=16, padx=16, bd=8, fg="black", font="arial 20 bold",bg="powder blue",command=lambda:btnclick(2)).grid(row=4,column=1)
btn3 =  Button(root, text="3",pady=16, padx=16, bd=8, fg="black", font="arial 20 bold",bg="powder blue",command=lambda:btnclick(3)).grid(row=4,column=2)
btnp =  Button(root, text="+",pady=16, padx=13, bd=8, fg="white", font="arial 20 bold",bg="green",command=lambda:btnclick("+")).grid(row=4,column=3)


#========================================================================================
btn00 =  Button(root, text="00",pady=16, padx=10, bd=8, fg="white", font="arial 20 bold",bg="green",command=lambda:btnclick("00")).grid(row=5,column=0)
btn0 =   Button(root, text="0",pady=16, padx=16, bd=8, fg="white", font="arial 20 bold",bg="green",command=lambda:btnclick("0")).grid(row=5,column=1)
btndo =  Button(root, text=".",pady=16, padx=20, bd=8, fg="white", font="arial 20 bold",bg="green",command=lambda:btnclick(".")).grid(row=5,column=2)
btnme =  Button(root, text="=",pady=16, padx=13, bd=8, fg="white", font="arial 20 bold",bg="green",command=lambda:btnEqualsInput()).grid(row=5,column=3)
root.resizable(0,0)
root.mainloop()