class bankroll():
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo
        self.historial = []
        
    def agregaralhistorial(self, apuestaaingrersar):
        self.historial.append(apuestaaingrersar)
        
class apuesta():
    contador_id = 0
    def __init__(self, momio, bank):
        self.cantidadapostada = None
        self.momio = momio
        self.bank = bank
        self.ganada = None
        self.id = self.contador_id
        apuesta.contador_id += 1
        
        
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
                
    def __str__(self):
        return f"id: {self.id}, cantidad: {self.cantidadapostada}, status: {self.ganada} "
            
                
                
print("----Menu Principal----")
print("1. crear partida 2. partidas activas, 3. salir")

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
        
    elif seleccion == "2":
        
        for indice, partidas in enumerate(listapartidas):
            print(indice, "-", partidas.nombre)
            
        selectpartida = input("con que bank quieres trabajar?(numero): ")
        selectpartida = int(selectpartida)
        partidaseleccionada = listapartidas[selectpartida]
        
        print("1. detalles 2. agregar apuesta 3.historial apuestas 4. volver al menu principal")
        while True:
            seleccion2 = input("que le hacemos a tu bank?: ")
            if seleccion2 == "1":
                print("nombre: ", partidaseleccionada.nombre, "saldo: ", partidaseleccionada.saldo)
                
            
            elif seleccion2 == "2":
                momionuevo = input("cual es el momio de esta apuesta?: ")
                momionuevo = float(momionuevo)
                banknuevo = partidaseleccionada
                nuevaapuesta =apuesta(momionuevo, banknuevo)
                nuevaapuesta.monto_a_Apostar()
                partidaseleccionada.agregaralhistorial(nuevaapuesta)
                
            elif seleccion2 =="3":
                for x, y in  enumerate(partidaseleccionada.historial):
                    print(x, "-", y)
                
            elif seleccion2 == "4":
                break
                
                
    elif seleccion == "3":
        break
 
