import csv
import numpy as np
from ClaseCama import cama
class ManejadorCama:
    __cantidad: 0
    __dimension: 0

    def __init__(self,dimension):
        self.__ListaCamas=np.empty(dimension, dtype=cama)
        self.__dimension = dimension
        self.__cantidad = 0
        #self.__ListaCamas=[]

    def __str__(self):
        s = ""
        for camas in self.__ListaCamas:
            s += str(camas) + '\n'
        return s

    def agregarCama(self,unaCama):
        if self.__cantidad == self.__dimension:
            self.__ListaCamas.resize(self.__dimension)
        self.__ListaCamas[self.__cantidad] = unaCama
        self.__cantidad += 1

    def CrearCamas(self):
        bandera= True
        with open("camas.csv","r") as file:
            reader = csv.reader(file,delimiter=";")
            #reader = np.loadtxt(file, delimiter=";")
            for fila in reader:
                if bandera:
                    bandera = False
                else:
                    idCama = int(fila[0])
                    habitacion = int(fila[1])
                    estado = bool(fila[2])
                    NyA = (fila[3])
                    diagnostico = (fila[4])
                    fechaInternacion = (fila[5])
                    fechaAlta = (fila[6])
                    unaCama = cama(idCama,habitacion,estado,NyA,diagnostico,fechaInternacion,fechaAlta)
                    self.agregarCama(unaCama)

    def darAlta(self,p,med):
        alta=input("Ingrese la fecha de alta del paciente: \n")
        for indice, cama in enumerate(self.__ListaCamas):
            if cama.getNyA() == p:
                cama.setAlta(alta)
                print("Paciente: {}      Cama: {}        Habitacion: {}".format(p,cama.getIdCama(),cama.getHabitacion()))
                print("Diagnostico: {:>5}   Fecha de internacion: {}".format(cama.getDiagnostico(),cama.getInternacion()))
                print("Fecha de alta: {}".format(cama.getAlta()))
                med.DarAlta(cama.getIdCama())


    def listarDiagnostico(self,d):
        estado="desocupada"
        print("Datos de los pacientes: ")
        print("idCama:  Habitacion:  Estado:   Apellido y Nombre:  Diagnostico:  Fecha internacion:  Fecha alta: ")
        for indice, cama in enumerate(self.__ListaCamas):
            if cama.getEstado():
                if cama.getDiagnostico() == d:
                    estado="ocupada"
                    print("{:<10} {:>5} {:^15} {:>15} {:>14} {:>15} {:>12} ".format(cama.getIdCama(),cama.getHabitacion(),estado,cama.getNyA(),cama.getDiagnostico(),cama.getInternacion(),cama.getAlta()))
        if estado=="desocupada":
            print("ERROR. No se encontro el diagnostico solicitado")
