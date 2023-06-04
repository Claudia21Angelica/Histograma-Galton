import tkinter as tk
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MaquinaGalton:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Máquina de Galton")
        self.root.geometry("850x650")

        # Crear entrada de texto para el número de pelotas
        label = tk.Label(self.root, text="Este programa tiene la finalidad de representar un histograma de Galton.\n\nFavor de ingresar el número de pelotas que desea visualizar en la gráfica:")
        label.pack()
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()

        # Crear botón para graficar el histograma
        button1 = tk.Button(self.root, text="Realizar la gráfica", command=self.plotHistogram)
        button1.pack()

        # Configurar la máquina de Galton
        self.n = 12
        self.ballCounts = [0] * (self.n + 1)
        self.canvas = None
        self.error_label = None

    def run(self):
        self.root.mainloop()

    def plotHistogram(self):
        #Validación para posibles errores al ingresar datos.
        try:
            # Obtener el valor ingresado en la entrada
            value = self.entry1.get()

            # Validar si el valor ingresado es un número válido
            if not value.isdigit():
                raise ValueError("Ingrese un número entero válido.")

            m = int(value)

            if m <= 0:
                raise ValueError("El número de pelotas debe ser un entero positivo.")

            # Reiniciar el contador de las pelotas
            self.ballCounts = [0] * (self.n + 1)

            # Generar las pelotas
            for _ in range(m):
                k = 0
                for _ in range(self.n):
                    if random.random() < 0.5:
                        k += 1
                self.ballCounts[k] += 1

            # Borrar la figura existente, solo si hay una actualmente.
            if self.canvas is not None:
                self.canvas.get_tk_widget().destroy()

            # Borrar el mensaje de error, solo si hay uno actualmente.
            if self.error_label is not None:
                self.error_label.destroy()

            # Crear una nueva figura y graficar el histograma.
            fig = Figure(figsize=(6, 5), dpi=100)
            plot = fig.add_subplot(111)
            x = list(range(self.n + 1))
            y = self.ballCounts
            plot.bar(x, y)
            plot.set_xlabel("Distribución de canicas")
            plot.set_ylabel("Cantidad de canicas")
            plot.set_title("Histograma de la máquina de Galton")

            # Mostrar la figura en pantalla
            self.canvas = FigureCanvasTkAgg(fig, master=self.root)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()
        except ValueError as e:
            self.showErrorMessage(str(e))
        except Exception as e:
            self.showErrorMessage("Ocurrió un error durante la ejecución del programa.")

    def showErrorMessage(self, message):
        self.error_label = tk.Label(self.root, text=message, fg="red")
        self.error_label.pack()

    def clearHistogram(self):
        self.ballCounts = [0] * (self.n + 1)
        if self.canvas is not None:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None

galton = MaquinaGalton()
galton.run()