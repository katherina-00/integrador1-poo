class medicamento:
    __idCama: ""
    __idMedicamento: int(0)
    __nombreComercial: ""
    __monodroga: ""
    __presentacion: ""
    __cantidadAplicada: int(0)
    __precioParticular: int(0)

    def __init__(self,idCama,idMedicamento,nombreComercial,monodroga,presentacion,cantidadAplicada,precioParticular):
        self.__idCama = idCama
        self.__idMedicamento = idMedicamento
        self.__nombreComercial = nombreComercial
        self.__monodroga = monodroga
        self.__presentacion = presentacion
        self.__cantidadAplicada = cantidadAplicada
        self.__precioParticular = precioParticular

    def __str__(self):
        return "%d %d %s %s %s %d %d" % (self.__idCama,self.__idMedicamento,self.__nombreComercial,self.__monodroga,self.__presentacion,self.__cantidadAplicada,self.__precioParticular)

    def getIdCama(self):
        return self.__idCama
    def getIdMedicamento(self):
        return self.__idMedicamento
    def getNombreComercial(self):
        return self.__nombreComercial
    def getMonodroga(self):
        return self.__monodroga
    def getPresentacion(self):
        return self.__presentacion
    def getCantidadAplicada(self):
        return self.__cantidadAplicada
    def getPrecioParticular(self):
        return  self.__precioParticular
'''
A cada paciente internado, se le aplican medicamentos,
 los datos de los medicamentos se almacenan en un archivo “medicamentos.csv”, 
que guarda la siguiente información: idCama, idMedicamento (1 a 100), 
nombre comercial, monodroga, presentación, cantidad aplicada,
precio total (este archivo se genera sin un orden particular).
'''
