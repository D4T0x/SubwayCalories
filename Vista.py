from tkinter import *

def run1():
    kcal = int(e1.get())
    a = '%i\n' % (kcal)
    txt.insert(END, a)
    e1.delete(0, END)


# Definimos la ventana
ventana = Tk()
ventana.title("Subway")
ventana.geometry('460x240')


# Definimos la entrada
lb = Label(ventana, text='Ingrese las kilocalorias a pedir y presione el boton')
lb.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
e1 = Entry(ventana, show=None)
e1.place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.1)

btn = Button(ventana, text='Run!', command=run1)
btn.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.1)

txt = Text(ventana)
txt.place(rely=0.6, relheight=0.4)

ventana.mainloop()



