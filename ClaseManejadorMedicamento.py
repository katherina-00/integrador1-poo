import csv
from ClaseMedicamento import medicamento
class ManejadorMedicamento:
    def __init__(self):
        self.__ListaMedicamento = []
    def __str__(self):
        s = ""
        for med in self.__ListaMedicamento:
            s += str(med) + '\n'
        return s

    def agregarMedicamento(self,unMedicamento):
        self.__ListaMedicamento.append(unMedicamento)

    def CrearMedicamento(self):
        bandera=True
        with open("medicamentos.csv","r") as file:
            reader = csv.reader(file,delimiter=";")
            for fila in reader:
                if bandera:
                    bandera = False
                else:
                    idCama = int(fila[0])
                    idMedicamento = int(fila[1])
                    nombreComercial = (fila[2])
                    monodroga = (fila[3])
                    presentacion = (fila[4])
                    cantidadAplicada = int(fila[5])
                    precioParticular = int(fila[6])
                    unMedicamento = medicamento(idCama,idMedicamento,nombreComercial,monodroga,presentacion,cantidadAplicada,precioParticular)
                    self.agregarMedicamento(unMedicamento)

    def DarAlta(self,idcama):
        total=int(0)
        print("Medicamento/Monodroga:  Presentacion:  Cantidad:  Precio: ")
        for medicamento in self.__ListaMedicamento:
            if medicamento.getIdCama() == idcama:
                print("{:<15} {:>20} {:>5} {:>12}".format(medicamento.getMonodroga(),medicamento.getPresentacion(),medicamento.getCantidadAplicada(),medicamento.getPrecioParticular()))
                total += int(medicamento.getPrecioParticular())
        print("Total adeudado: {:>39}".format(total))


