from tkinter import *

window = Tk()

l1 = Label(window, text="Input Number of terms to Find its Fibbonacci Sequence:")
l1.grid(row=0, column=2)

t1 = Text(window, height=10, width=20)
t1.grid(row=1, column=3)

ei_value = StringVar()
e1 = Entry(window, textvariable=ei_value)
e1.grid(row=1, column=2)


def fibbonacci():

    nterms=float(ei_value.get())
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        output="Please enter a positive integer"
        t1.insert(END, output)
    elif nterms == 1:
        t1.insert(END, n1)
    else:
        while count < nterms:
            t1.insert(END, n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

b1 = Button(window, text="Okay", height=4, width=10, command=fibbonacci)
b1.grid(row=2, column=2)

window.mainloop()