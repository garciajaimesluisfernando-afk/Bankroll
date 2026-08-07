class bankroll():
    def __init__(self, saldo):
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
                
FerBank = bankroll(100)
apuesta1 = apuesta(1.5, FerBank)
apuesta1.monto_a_Apostar()
apuesta1.resolver("w")
print(FerBank.saldo)
