import tkinter as tk

def calcula():
	print("Vamos a calcular")
	op1 = operando1.get
	op1 = operando2.get
	sum = op1 +op1
	resultado.config(text=suma)

ventana = tk.Tk()
ventana.geometry("600x400")

etiqueta = tk.Label(text="Operando 1")
etiqueta.pack()

operando1= tk.Entry()
operando1.pack(padx=10,pady=10)

etiqueta = tk.Label(text="Operando 2")
etiqueta.pack()

operando2= tk.Entry()
operando2.pack(padx=20,pady=20)

boton = tk.Button(text="Vamos a calcular",command=calcula)
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Resultado")
resultado.pack(padx=10,pady=10)

ventana.mainloop() # no te salgas, bucle infinito
