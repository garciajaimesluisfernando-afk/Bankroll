class bankroll():
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo
        
class apuesta():
    def __init__(self, momio, bank):
        self.cantidadapostada = None
        self.momio = momio
        self.bank = bank
        self.ganada = None
        self.metodo = None
        
    def resolver(self, status):
        if status == "w":
            self.ganada = True
            
        else:
            self.ganada = False
            
        if self.ganada == True:
            ganancia = self.cantidadapostada * self.momio - self.cantidadapostada
            self.bank.saldo = self.bank.saldo + ganancia
        
        elif self.ganada == False:
            self.bank.saldo = self.bank.saldo - self.cantidadapostada
            
    def monto_a_Apostar(self):
        
        while True:
            porcentaje = input("que nivel de confianza tienes en esta apuesta (porcentaje): ")
            
            try:
                porcentaje = int(porcentaje)
                if porcentaje > 0 and porcentaje <= 100:
                    porcentajeenpesos = (porcentaje * self.bank.saldo) / 100
                    self.cantidadapostada = porcentajeenpesos
                    print("apuesta esta cantidad: ", porcentajeenpesos)
                    break
                else: 
                    print("ingresa un porcentaje valido")
            
            except:
                print("caracter invalido")
                
                
print("----Menu Principal----")
print("1. crear partida 2. ver historial de partidas  3. resolver apuesta 4. ver saldo , 5. salir")

listapartidas = []
while True:
    seleccion = input("que quieres hacer: ")
    if seleccion == "1":
        crearpartida = input("ingresa el nombre de tu partida:  ")
        cantidadinicial = input(("cuanto tienes en tu bank: "))
        cantidadinicial = int(cantidadinicial)
        crearpartida = bankroll(crearpartida, cantidadinicial)
        listapartidas.append(crearpartida)
        print("empiezas con: ", crearpartida.saldo)
        
    elif seleccion == "5":
        break
 
for partida in listapartidas:
    print(partida.nombre, "-", partida.saldo)  
