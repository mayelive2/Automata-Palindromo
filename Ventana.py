from tkinter import *
from tkinter import messagebox
import re
import time
import threading
from Automata import *


class mostrar():
    def __init__(self):
        self.lista = list()
        self.ventana()

    def ventana(self):
        self.root = Tk()
        self.listpila = list()
        self.root.title(" Palindromo Impar")
        self.root.geometry('600x400')
        self.root.configure (background = "light blue" )
        self.texto = Label(self.root, text="Ingrese el Palindromo (ab) impar:", bg = "light blue", font=("Times New Roman", 16))
        self.texto.pack(padx=0, pady=0)
        self.texto.place(x=9, y=9)
        self.dato = Entry(self.root, text="validar")
        self.dato.place(x=10, y=40)
        self.boton = Button(self.root, text="Validar", fg="red", command=self.iniciarAutomata)
        self.boton.place(x=150, y=40)
        self.root.mainloop()

    def validar(self):
        lenguaje = self.dato.get()
        self.__palabraEntry = lenguaje
        j = 0

        validar2 = re.match('^[a-bA-B]+c[a-bA-B]+$', lenguaje)
        valen = len(lenguaje) % 2
        total = len(lenguaje)
        if valen == 1 and total >= 3 and validar2 is not None:
            pos = 15
            cont = 0
            for i in self.lista:
                self.lista[cont].destroy()
                cont = cont + 1
            for i in lenguaje:
                botonp = Button(self.root, text=i, fg="white", background="Light Blue",
                                command=self.PruebaDeAnimaciones)
                botonp.pack(padx=0, pady=0, ipadx=130, ipady=10)
                botonp.grid(row=0, column=1, columnspan=3, sticky='EWNS')
                botonp.place(x=(10) + pos, y=70)
                pos = pos + 15
                self.lista.append(botonp)
            return True
        else:

            messagebox.showerror("Validación", "Dato invalido")
            return False

    def iniciarGrafo(self):
        self.__indexP = -1
        self.__indexE = -1
        self.__pila = Pila()
        self.transicionA = -1
        self.generarPila()

        self.canvas = Canvas(width=380, height=220, bg="#ECEE38")
        self.canvas.pack(expand=NO)
        self.canvas.place(x=20, y=160)

        # Lineas de inicio
        self.canvas.create_line(0, 150, 23, 150, width=4, fill="black")
        self.canvas.create_line(12, 140, 23, 150, width=4, fill="black")
        self.canvas.create_line(12, 160, 23, 150, width=4, fill="black")

        # creacion del primer estado
        self.canvas.create_oval(23, 95, 65, 130, width=2, fill='white')  # circulo del primer estado
        self.canvas.create_oval(25, 120, 85, 180, width=5, fill='white')  # circulo del arco de transicion

        self.canvas.create_line(20, 125, 35, 128, width=2, fill="black")  # Linea uno de la flecha de transicion P
        self.canvas.create_line(35, 115, 35, 128, width=2, fill="black")  # Linea dos de la flecha de transicion P

        self.canvas.create_text(55, 150, text='P', fill='black')  # letra P

        # transiciones primer estado
        self.canvas.create_text(35, 85, text='a,#/#a', fill='black')
        self.canvas.create_text(35, 70, text='b,#/#b', fill='black')
        self.canvas.create_text(35, 55, text='a,a/aa', fill='black')
        self.canvas.create_text(35, 40, text='b,a/ab', fill='black')
        self.canvas.create_text(35, 25, text='a,b/ba', fill='black')
        self.canvas.create_text(35, 10, text='b,b/bb', fill='black')

        self.canvas.create_line(85, 150, 175, 150, width=5, fill='black')  # linea de transicion de p a q
        self.canvas.create_line(160, 160, 175, 150, width=4, fill="black")
        self.canvas.create_line(160, 140, 175, 150, width=4, fill="black")

        # transiciones de la linea 1
        self.canvas.create_text(125, 135, text='c,b/b', fill='black')
        self.canvas.create_text(125, 120, text='c,#/#', fill='black')
        self.canvas.create_text(125, 165, text='c,b/b', fill='black')

        # creacion del segundo estado
        self.canvas.create_oval(173, 95, 215, 130, width=2, fill='white')  # circulo del segundo estado
        self.canvas.create_oval(175, 120, 235, 180, width=5, fill='white')  # circulo del arco de transicion de segundo estado
        self.canvas.create_text(205, 150, text='q', fill='black')  # letra q

        self.canvas.create_line(170, 125, 185, 128, width=2, fill="black")  # Linea uno de la flecha de transicion Q
        self.canvas.create_line(185, 115, 185, 128, width=2, fill="black")  # Linea dos de la flecha de transicion Q

        # transiciones del segundo estado
        self.canvas.create_text(220, 85, text='a,a/λ', fill='black')
        self.canvas.create_text(220, 70, text='b,b/λ', fill='black')

        self.canvas.create_line(235, 150, 315, 150, width=5, fill='black')  # linea de transicion de q a r

        self.canvas.create_line(300, 160, 315, 150, width=4, fill="black")
        self.canvas.create_line(300, 140, 315, 150, width=4, fill="black")

        # transicion de la linea 2
        self.canvas.create_text(280, 165, text='λ,#/#', fill='black')

        # creacion del tercer estado
        self.canvas.create_oval(315, 120, 375, 180, width=5, fill='white')  # circulo tercer estado
        self.canvas.create_oval(320, 125, 370, 175, width=2, fill='white')  # circulo de estado de aceptacion
        self.canvas.create_text(345, 150, text='r', fill='black')  # letra r

    def generarPila(self):
        n = len(self.dato.get())
        n = (int)(n / 2)
        n = n + 1
        pos = 0
        i = 0
        for i in range(n):
            botonp = Button(self.root, text="_", fg="white", background="blue", command=self.PruebaDeAnimaciones)
            botonp.pack(padx=200, pady=200, ipadx=130, ipady=10)
            botonp.place(x=200, y=(120 - pos))
            pos = pos + 25
            self.listpila.append(botonp)
        self.listpila[0].configure(text="#")

    def iniciarAutomata(self):
        if self.validar() == False:
            return -1
        self.iniciarGrafo()
        self.automata = Automata(self.dato.get())
        self.hilo = threading.Thread(target=self.runAautomata)
        self.hilo.start()
        self.cambiarLetra(0)
        self.automata.setBandera(True)
        while (self.hilo.is_alive()):
            self.esperarCambios()
            self.actualizarGui()
            self.automata.setBandera(True)

        if (self.__indexE == 2):
            messagebox.showinfo("Resultado", "Es palindrome")
            self.root.destroy()
        else:
            messagebox.showinfo("Resultado", "No es palindrome")
            self.root.destroy()

    def esperarCambios(self):
        x = 0
        while (True):
            if (self.automata.getBandera() == True):
                time.sleep(0.2)
                x += 1
                if (x == 4):
                    break
            else:
                break

    def actualizarGui(self):
        if (self.__indexE != self.automata.getEstado()):
            self.cambiarEstado(self.automata.getEstado())
        if (self.transicionA != self.automata.getTransicion()):
            self.cambiarTransicionTexto(self.automata.getTransicion())
        if (self.__indexP != self.automata.getLetra()):
            self.cambiarLetra(self.automata.getLetra())
        self.cambiarPila(self.automata.getPila())

    def cambiarPila(self, pilaaux):
        j = 0
        for i in self.listpila:
            self.listpila[j].configure(text="_")
            j = j + 1
        j = 0
        for i in pilaaux.getVec():
            self.listpila[j].configure(text=pilaaux.getVec()[j])
            j = j + 1

    def cambiarEstado(self, x):

        if (x == 1):
            self.OffestadoCirculoP()
            self.transcicionPQ()
            self.OnEstadocirculoQ()
        if (x == 2):
            self.OffEstadocirculoQ()
            self.TransicionQR()
            self.TextotransicionesQ(3)
            self.estadoAceptacion()
        if (x == 0):
            self.lineaini()
            self.OnestadoCirculoP()
        self.__indexE = x

    def cambiarTransicionTexto(self, i):
        self.transicionA = self.automata.getTransicion()
        if (self.__indexE == 0):
            self.transicionP()
            self.textoTransicionesP(i)
        if (self.__indexE == 1):
            self.TransicionQ()
            self.TextotransicionesQ(i)

    def cambiarLetra(self, i):
        if (self.__indexP == -1):
            self.lista[self.__indexP + 1].configure(background="red")
        self.root.update()
        if (len(self.dato.get()) > i):
            self.lista[i].configure(background="red")

    def runAautomata(self):
        self.automata.run()

    def PruebaDeAnimaciones(self):
        self.lineaini()
        self.OnestadoCirculoP()
        self.transicionP()
        j = 1
        for i in range(1, 10):
            self.textoTransicionesP(j)
            j += 1
        self.OffestadoCirculoP()

        self.transcicionPQ()
        self.OnEstadocirculoQ()
        self.TransicionQ()
        k = 1
        for i in range(1, 4):
            self.TextotransicionesQ(k)
            k += 1
        self.OffEstadocirculoQ()
        self.TransicionQR()
        self.estadoAceptacion()

    def lineaini(self):
        self.canvas.create_line(0, 150, 23, 150, width=4, fill="red")
        self.canvas.create_line(12, 140, 23, 150, width=4, fill="red")
        self.canvas.create_line(12, 160, 23, 150, width=4, fill="red")
        self.root.update()
        time.sleep(0.5)
        self.canvas.create_line(0, 150, 23, 150, width=4, fill="black")
        self.canvas.create_line(12, 140, 23, 150, width=4, fill="black")
        self.canvas.create_line(12, 160, 23, 150, width=4, fill="black")

    def transicionP(self):
        self.canvas.create_oval(23, 95, 65, 130, width=2, fill='blue')  # circulo del primer estado
        self.root.update()
        time.sleep(0.5)
        self.canvas.create_oval(23, 95, 65, 130, width=2, fill='white')  # circulo del primer estado

    def OnestadoCirculoP(self):
        self.canvas.create_oval(25, 120, 85, 180, width=5, fill='blue')  # circulo del arco de transicion
        self.textoP()
        self.root.update()
        time.sleep(0.5)

    def OffestadoCirculoP(self):
        self.canvas.create_oval(25, 120, 85, 180, width=5, fill='white')  # circulo del arco de transicion
        self.canvas.create_line(20, 125, 35, 128, width=2, fill="black")  # Linea uno de la flecha de transicion
        self.canvas.create_line(35, 115, 35, 128, width=2, fill="black")  # Linea dos de la flecha de transicion
        self.textoP()
        self.root.update()
        time.sleep(0.5)

    def textoP(self):
        self.canvas.create_text(55, 150, text='P', fill='black')  # letra P

    def textoTransicionesP(self, i):
        if i == 9:
            self.canvas.create_text(125, 135, text='c,b/b', fill='blue')
            self.root.update()
            time.sleep(0.5)
            self.canvas.create_text(125, 135, text='c,b/b', fill='black')
        if i == 7:
            self.canvas.create_text(125, 120, text='c,#/#', fill='blue')
            self.root.update()
            time.sleep(0.5)
            self.canvas.create_text(125, 120, text='c,#/#', fill='black')
        if i == 8:
            self.canvas.create_text(125, 165, text='c,b/b', fill='blue')
            self.root.update()
            time.sleep(0.5)
            self.canvas.create_text(125, 165, text='c,b/b', fill='black')
        if i == 6:
            self.canvas.create_text(35, 85, text='a,#/#a', fill='blue')
            self.root.update()
            time.sleep(0.5)
            self.canvas.create_text(35, 85, text='a,#/#a', fill='black')
        if i == 5:
            self.canvas.create_text(35, 70, text='b,#/#b', fill='blue')
            self.root.update()
            time.sleep(0.5)
            self.canvas.create_text(35, 70, text='b,#/#b', fill='black')
        if i == 4:
            self.canvas.create_text(35, 55, text='a,a/aa', fill='blue')
            self.root.update()
            time.sleep(0.5)
            self.canvas.create_text(35, 55, text='a,a/aa', fill='black')
        if i == 3:
            self.canvas.create_text(35, 40, text='b,a/ab', fill='blue')
            self.root.update()
            time.sleep(0.5)
            self.canvas.create_text(35, 40, text='b,a/ab', fill='black')
        if i == 2:
            self.canvas.create_text(35, 25, text='a,b/ba', fill='blue')
            self.root.update()
            time.sleep(0.5)
            self.canvas.create_text(35, 25, text='a,b/ba', fill='black')
        if i == 1:
            self.canvas.create_text(35, 10, text='b,b/bb', fill='blue')
            self.root.update()
            time.sleep(0.5)
            self.canvas.create_text(35, 10, text='b,b/bb', fill='black')

    def transcicionPQ(self):
        self.canvas.create_line(160, 160, 175, 150, width=4, fill="blue")
        self.canvas.create_line(160, 140, 175, 150, width=4, fill="blue")
        self.canvas.create_line(85, 150, 175, 150, width=5, fill='blue')  # linea de transicion de p a q
        self.root.update()
        time.sleep(0.5)
        self.canvas.create_line(85, 150, 175, 150, width=5, fill='black')
        self.canvas.create_line(160, 160, 175, 150, width=4, fill="black")
        self.canvas.create_line(160, 140, 175, 150, width=4, fill="black")

        # transiciones de la linea 1

    def TransicionQ(self):
        self.canvas.create_oval(173, 95, 215, 130, width=2, fill='red')  # circulo del segundo estado
        self.textoEstadoQ()
        self.root.update()
        time.sleep(0.5)
        self.canvas.create_oval(173, 95, 215, 130, width=2, fill='white')

    def OnEstadocirculoQ(self):
        self.canvas.create_oval(175, 120, 235, 180, width=5,
                                fill='blue')  # circulo del arco de transicion de segundo estado
        self.textoEstadoQ()
        self.root.update()
        time.sleep(0.5)

    def OffEstadocirculoQ(self):
        self.canvas.create_oval(175, 120, 235, 180, width=5,
                                fill='white')  # circulo del arco de transicion de segundo estado
        self.canvas.create_line(170, 125, 185, 128, width=2, fill="black")  # Linea uno de la flecha de transicion Q
        self.canvas.create_line(185, 115, 185, 128, width=2, fill="black")  # Linea dos de la flecha de transicion Q
        self.textoEstadoQ()
        self.root.update()

    def textoEstadoQ(self):
        self.canvas.create_text(205, 150, text='q', fill='black')  # letra q

    def TextotransicionesQ(self, i):
        print("trasicion texto q ", i)
        if i == 2:
            self.canvas.create_text(220, 85, text='a,a/λ', fill='blue')
            self.root.update()
            time.sleep(0.5)
            self.canvas.create_text(220, 85, text='a,a/λ', fill='black')

        if i == 1:
            self.canvas.create_text(220, 70, text='b,b/λ', fill='blue')
            self.root.update()
            time.sleep(0.5)
            self.canvas.create_text(220, 70, text='b,b/λ', fill='black')
        if i == 3:
            self.canvas.create_text(280, 165, text='λ,#/#', fill='blue')
            self.root.update()
            time.sleep(0.5)
            self.canvas.create_text(280, 165, text='λ,#/#', fill='black')

    def TransicionQR(self):

        self.canvas.create_line(300, 160, 315, 150, width=4, fill="blue")
        self.canvas.create_line(300, 140, 315, 150, width=4, fill="blue")

        self.canvas.create_line(235, 150, 315, 150, width=5, fill='blue')  # linea de transicion de q a r
        self.root.update()
        time.sleep(0.5)
        self.canvas.create_line(235, 150, 315, 150, width=5, fill='black')
        self.canvas.create_line(300, 160, 315, 150, width=4, fill="black")
        self.canvas.create_line(300, 140, 315, 150, width=4, fill="black")

    def estadoAceptacion(self):
        self.canvas.create_oval(315, 120, 375, 180, width=5, fill='white')  # circulo tercer estado
        self.canvas.create_oval(320, 125, 370, 175, width=2, fill='blue')  # circulo de estado de aceptacion
        self.canvas.create_text(345, 150, text='r', fill='black')  # letra r
        self.root.update()


x = mostrar()