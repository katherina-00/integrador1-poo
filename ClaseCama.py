class cama:
    __idCama: int(0)
    __habitacion: int(0)
    __estado: bool(None)
    __NyA: ""
    __diagnostico: ""
    __fechaInternacion: ""
    __fechaAlta: None

    def __init__(self,idCama,habitacion,estado,NyA,diagnostico,fechaInternacion,fechaAlta):
        self.__idCama = idCama
        self.__habitacion = habitacion
        self.__estado = estado
        self.__NyA = NyA
        self.__diagnostico = diagnostico
        self.__fechaInternacion = fechaInternacion
        self.__fechaAlta = fechaAlta

    def __str__(self):
        return " %d %d %s %s %s %s %s " % (self.__idCama, self.__habitacion,self.__estado,self.__NyA, self.__diagnostico, self.__fechaInternacion,self.__fechaAlta)

    def setAlta(self,alta):
        self.__fechaAlta = alta
    def getIdCama(self):
        return self.__idCama
    def getHabitacion(self):
        return self.__habitacion
    def getEstado(self):
        return self.__estado
    def getNyA(self):
        return self.__NyA
    def getDiagnostico(self):
        return self.__diagnostico
    def getInternacion(self):
        return self.__fechaInternacion
    def getAlta(self):
        return self.__fechaAlta
'''
La clínica cuenta con 30 camas de internación, de cada cama se registra: 
idCama (1 a 30),
habitación, estado (booleano, true indica ocupada, false indica libre), 
nombre y apellido del
paciente (valor None si no está ocupada), diagnóstico, fecha de internación, 
fecha de alta (dato
que se carga en el ítem 3). Los datos de las camas vienen en un archivo 
separado por comas
denominado “camas.csv”.
'''
