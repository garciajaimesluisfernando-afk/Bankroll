import tkinter as tk
from bankroll import bankroll

ventana = tk.Tk()

def salir():
    ventana.destroy()

titulo = tk.Label(ventana, text = "Menu Principal", font = ("Arial", 18, "bold"), fg="white", bg="#2c3e50")
titulo.pack()

def Crear_Partida():
    
    nombre = entry_nombre.get()
    saldo = int(entry_monto.get())
    nuevapartida = bankroll(nombre, saldo)
    listapartidas.append(nuevapartida)
    label_partidacreada.config(text= f"partida creada: {nuevapartida.nombre} - {nuevapartida.saldo}")
    
def verpartidas():
    listastr = ""
    for x, y in enumerate(listapartidas):
        listastr = listastr + f"{x} --- {y.nombre}\n"
        
    lista_label.config(text= listastr)
        
    



crearpartida =tk.Button(ventana, text ="Crear Partida", font = ("Arial", 14, "bold"), fg="black", bg="#e7131d", command= Crear_Partida )
partidasactivas =tk.Button(ventana, text ="partidas", font = ("Arial", 14, "bold"), fg="black", bg="#e7131d", command= verpartidas)
salirboton =tk.Button(ventana, text ="salir", font = ("Arial", 14, "bold"), fg="black", bg="#e7131d", command= salir)

crearpartida.pack(pady=10)
partidasactivas.pack(pady=10)
salirboton.pack(pady=10)


label_nombre = tk.Label(ventana, text= "Ingresa el nombre de tu partida:")
label_nombre.pack()

entry_nombre = tk.Entry(ventana)
entry_nombre.pack()
    
label_monto = tk.Label(ventana, text="Con cuanto empiezas")
label_monto.pack()

entry_monto = tk.Entry(ventana)
entry_monto.pack()

listapartidas = []

label_partidacreada = tk.Label(ventana, text= "")
label_partidacreada.pack()

lista_label = tk.Label(ventana, text= "")
lista_label.pack()



    
ventana.mainloop()