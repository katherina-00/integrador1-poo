import sys
from ClaseManejadorCama import ManejadorCama
from ClaseManejadorMedicamento import ManejadorMedicamento
from menu import muestraMenu
if __name__=="__main__":

    c = ManejadorCama(3)
    c.CrearCamas()

    med = ManejadorMedicamento()
    med.CrearMedicamento()

    while True:
            op = muestraMenu()
            if op == '1':
                nombre=input("Ingrese nombre del paciente: ")
                c.darAlta(nombre,med)
            elif op == '2':
                diagnostico=input("Ingrese diagnostico: ")
                c.listarDiagnostico(diagnostico)
            elif op == '3':
                sys.exit(0)
