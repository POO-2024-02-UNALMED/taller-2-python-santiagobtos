class Auto:
    cantidadCreados=0
    def __init__(self,modelo, precio, asientos, marca, motor, registro ):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
    def cantidadAsientos(self):
        contador=0
        for i in range(len(self.asientos)):
            if self.cantidadAsientos[i]!=None:
                contador+=1
        return contador
    def verificarIntegridad(self):
        if self.registro==self.motor.registro:
            for i in range(len(self.asientos)):
                if self.asientos[i].registro!=self.registro:
                    return "Las piezas no son originales"
                    break
                return "Auto original"
                
        else:
            return "Las piezas no son originales"

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    def cambiarRegistro(self,numero):
        self.registro=numero
    def asignarTipo(self, type):
        if type=="gasolina" or type=="electrico":
            self.tipo=type
    

class Asiento:
    def __init__(self, color, precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self,colo):
        if colo=="negro":
            self.color="negro"
        elif colo=="blanco":
            self.color="blanco"
        elif colo=="amarillo":
            self.color="amarillo"
        elif colo=="rojo":
            self.color="rojo"
        elif colo=="verde":
            self.color="verde"
   


        