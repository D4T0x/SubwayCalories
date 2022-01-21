from tkinter import *
from Subway import *

def run1():
    txt.delete(1.0, END)
    kcal = int(e1.get())
    tPoblacion = int(e2.get())
    numGeneraciones = int(e3.get())
    a = '%i\n' % (kcal)
    txt.insert(END, a)
    e1.delete(0, END)
    prueba = Subway('SubwayMenu.txt', kcal, tPoblacion, numGeneraciones)
    prueba.evolucionar()
    mejor = prueba.getMejor()
    for c in mejor.getCromosoma():
        a = c.getNombre()
        a += '\n'
        txt.insert(END, a)
    txt.insert(END, 'Kilocalorias del bocadillo: ')
    a = '%i\n' % (mejor.getKilocalorias())
    txt.insert(END, a)

# Definimos la ventana
ventana = Tk()
ventana.title("Subway")
ventana.geometry('400x600')

lb1 = Label(ventana, text="Ingrese Kilocalorias: ")
lb2 = Label(ventana, text="Ingrese tamaño población: ")
lb3 = Label(ventana, text="Ingrese número generaciones: ")

lb1.place(relx=0.015, rely=0.03)
lb2.place(relx=0.015, rely=0.09)
lb3.place(relx=0.015, rely=0.16)

e1 = Entry(ventana)
e2 = Entry(ventana)
e3 = Entry(ventana)

e1.place(relx=0.5, rely=0.03)
e2.place(relx=0.5, rely=0.09)
e3.place(relx=0.5, rely=0.16)

btn = Button(ventana, text='Run!', command=run1)
btn.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.05)

txt = Text(ventana)
txt.place(rely=0.4, relheight=1)

ventana.mainloop()



