from tkinter import *


# Methods
def dispScr(var):
    if var is None:
        txt = ""
    else:
        txt = str(var)
    text.set(txt)


def setVarA(number=None):
    global varA
    if number is None:
        varA = None
    else:
        varA = int(number)
    dispScr(varA)


def setVarB(number=None):
    global varB
    if number is None:
        varB = None
    else:
        varB = int(number)
    dispScr(varB)


def addVarA(number):
    #  change int-varA to str-varA -> add str-number -> change new-str-var to int-varA
    global varA
    _varA = str(varA)
    _varA += str(number)
    setVarA(int(_varA))


def addVarB(number):
    global varB
    #  adding digit to end of varB
    _varB = str(varB)
    _varB += str(number)
    setVarB(int(_varB))


def setOperation(operation=None):
    global ope
    if operation is None:
        ope = None
    else:
        ope = operation


def setMemory(memory=None):
    global mem
    if memory is None:
        mem = None
    else:
        mem = memory
        setVarA()
        setOperation()
        setVarB()


def DEV_show_vars():
    global varA, varB, ope, mem
    print(f"varA: {varA}\nvarB: {varB}\nope: {ope}\nmem: {mem}\n\n\n")


#  To create No. buttons.
def doBtnNo(number, row, column, width=6, height=3):
    """Creates No. button 0-9"""
    btn = Button(text=number, width=width, height=height, command=lambda: clickBtnNo(number))
    if number == 0:
        btn.grid(row=row, column=column, columnspan=2, sticky=W + E, padx=5, pady=5)
    else:
        btn.grid(row=row, column=column, padx=5, pady=5)
    return btn


def clickBtnNo(number):
    global varA, varB, ope, mem
    #  jeżeli to pierwsze  kliknięcie guzika -> ustaw varA
    if varA is None:
        setVarA(number)
    #  jeżeli varA jest już ustalona a operation wybrana -> ustaw varB
    elif varA is not None and ope is not None and varB is None:
        setVarB(number)
    #  jeżeli chcemy zmienić varA z cyfry na liczbę, czyli nie ma wybranej operacji -> dodaj cyfre na koniec varA
    elif varA is not None and ope is None:
        addVarA(number)
    #  jeżeli varA i operation są wybrane -> ustaw varB
    elif varA is not None and ope is not None and varB is None:
        setVarB(number)
    #  jeżeli  chcemy dodać cyfre na koniec varB
    elif varA is not None and ope is not None and varB is not None:
        addVarB(number)


# To create operation buttons.
def doBtnOpe(operation, row, column, width=6, height=3):
    if operation == "+/-":
        btn = Button(text=operation, width=width, height=height, command=lambda: clickBtnPM())
    elif operation == "=":
        btn = Button(text=operation, width=width, height=height, command=lambda: clickBtnEqual())
    elif operation == "AC":
        btn = Button(text=operation, width=width, height=height, command=lambda: clickBtnAC())
    elif operation == ",":
        btn = Button(text=operation, width=width, height=height, command=lambda: clickBtnDot())
    else:
        btn = Button(text=operation, width=width, height=height, command=lambda: clickBtnOpe(operation))
    btn.grid(row=row, column=column, padx=5, pady=5)
    return btn


#  Operation buttons methods
def clickBtnOpe(operation):
    if varA is None and mem is None:
        pass
    elif varA is None and mem is not None:
        setVarA(mem)
        setOperation(operation)
    elif varA is not None and varB is None:
        setOperation(operation)
    elif varA is not None and ope is not None and varB is not None:
        clickBtnEqual()
        setVarA(mem)
        setOperation(operation)


def clickBtnEqual():
    """Do the math"""
    global varA, varB, ope
    equation = None
    if varA is not None and ope is not None and varB is not None:
        #  adding
        if ope == "+":
            equation = varA + varB
            setMemory(equation)
            dispScr(equation)
        #  subrtaction
        elif ope == "-":
            equation = varA - varB
            setMemory(equation)
            dispScr(equation)
        #  multiplication
        elif ope == "*":
            equation = varA * varB
            setMemory(equation)
            dispScr(equation)
        #  division
        elif ope == "/":
            equation = varA / varB
            setMemory(equation)
            dispScr(equation)


def clickBtnAC():
    global varA, varB, ope, mem
    #  jeżeli to mem
    if varA is None:
        setMemory()
    #  jeżeli to varA
    if varA is not None and ope is None:
        setVarA()
    #  jeżeli to operacja
    if varA is not None and ope is not None and varB is None:
        setOperation()
    #  jeżeli to varB
    if varA is not None and ope is not None and varB is not None:
        setVarB()


def clickBtnPM():
    """Changes variable's sign."""
    global varA, varB, ope
    if varA is not None and ope is None:
        varA *= -1
        dispScr(varA)
    elif varA is not None and ope is not None and varB is not None:
        varB *= -1
        dispScr(varB)


def clickBtnDot():
    pass


app = Tk()
app.title("Kalkulator")
# app.geometry("260x380")
app.resizable(False,False)


#  Global variables
varA = None  # variable A
varB = None  # variable B
ope = None  # math operation
mem = None  # last result

#  Display
text = StringVar()
text.set("")
display = Entry(app, width=6, font=("Arial", 36), textvariable=text, justify=RIGHT)
display.grid(row=1, column=0, columnspan=4, sticky=N + S + W + E)
display.config(state="disabled")

frame1 = Frame(app, highlightbackground="blue", highlightthickness=2)
frame1.grid(padx=20, pady=20)

#  Buttons
# button_ac = doBtnOpe("AC", 2, 0)
button_ac = Button(text="AC", width=6, height=3, command=lambda: clickBtnAC())
button_ac.grid(row=2, column=0)
button_7 = doBtnNo(7, 3, 0)
button_4 = doBtnNo(4, 4, 0)
button_1 = doBtnNo(1, 5, 0)
button_0 = doBtnNo(0, 6, 0)
# button_0 = Button(text="0", width=6, height=3, command=lambda: clickBtnNo(0))
# button_0.grid(row=6, column=0, columnspan=2, sticky=W + E)

button_pm = doBtnOpe("+/-", 2, 1)
button_8 = doBtnNo(8, 3, 1)
button_5 = doBtnNo(5, 4, 1)
button_2 = doBtnNo(2, 5, 1)

button_per = doBtnOpe("%", 2, 2)
button_9 = doBtnNo(9, 3, 2)
button_6 = doBtnNo(6, 4, 2)
button_3 = doBtnNo(3, 5, 2)
# button_dot = doBtnOpe(",", 6, 2)
button_dot = Button(text=",", width=6, height=3, command=lambda: DEV_show_vars())
button_dot.grid(row=6, column=2)

button_d = doBtnOpe("/", 2, 3)
button_t = doBtnOpe("*", 3, 3)
button_m = doBtnOpe("-", 4, 3)
button_p = doBtnOpe("+", 5, 3)
button_e = doBtnOpe("=", 6, 3)
# button_e = Button(text="=", width=6, height=3, command=lambda: clickBtnEqual())
# button_e.grid(row=6, column=3)

#  Start program
app.mainloop()
