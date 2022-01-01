from modelo import*
from controladora import Empresa
empresa = Empresa()
def agregarSoftware():
    continuar = "si"
    while True:
        if continuar == "no":
           break
        else: 
            print("Seleccione el tipo de software a añadir a la lista:\n 1. Software extranjero\n 2. Software nacional\n 3. Cancelar")
            valor = str(input("Teclee la opción deseada aquí: "))

            if valor == "1":
                   id = str(input("Teclee el id del software: "))
                   lineasCod = int(input("Teclee la cantidad de líneas de código del software: "))
                   horasTrab = float(input("Teclee las horas trabajadas en el software: "))
                   empExt = str(input("Teclee el nombre de la empresa extranjera: "))
                   impuesto = float(input("Teclee el impuesto a cobrar: ")) 
                   nuevoSoftware = SoftwareExtranjero(id, lineasCod, horasTrab, empExt, impuesto)
                   empresa.añadirSoftware(nuevoSoftware)
                   print(f"Cantidad de softwares en la lista: {len(empresa.listaSoftware)}")
                   continuar = str(input("¿Desea agregar un nuevo software? (si/no): "))
    
            elif valor == "2":
                    id = str(input("Teclee el id del software: "))
                    lineasCod = int(input("Teclee la cantidad de líneas de código del software: "))
                    horasTrab = float(input("Teclee las horas trabajadas en el software: "))
                    organismo = str(input("Teclee el nombre del organismo: "))
                    nuevoSoftware = SoftwareNacional(id, lineasCod, horasTrab, organismo)
                    empresa.añadirSoftware(nuevoSoftware)
                    print(f"Cantidad de softwares en la lista: {len(empresa.listaSoftware)}")
                    continuar = str(input("Desea agregar un nuevo software (si/no): "))
            
            elif valor == "3":
                    opciones()


            else:
                    print("ERROR: Seleccione una opción válida")
    opciones()

def calcularCobro():
    print(f"El cobro total de todos los softwares es: {empresa.cobroTotal()}")
    opciones()

def verContratos():
    continuar = "si"
    while True:
        if continuar == "no":
           break
        else:
           organismo = str(input("Teclee el nombre del organismo: "))
           contratos = empresa.contratosOrganismo(organismo)
           print(f"El total de contratos de {organismo} es: {contratos}")
           continuar = str(input("¿Desea verificar los contratos de otro organismo?  (si/no): "))
    opciones()


def opciones():
    softwares = empresa.listaSoftware.__len__()
    print(f"Empresa de Software. Total de softwares registrados: {softwares}")
    print(" 1. Agregar un software a la lista\n 2. Calcular el cobro total de todos los softwares\n 3. Ver contratos de un organismo nacional\n 4. Salir")
  
    opcion =  str(input("Teclee la opción seleccionada aquí: "))
    if opcion == "1":
        agregarSoftware()
    elif opcion == "2":
        calcularCobro()
    elif opcion == "3":
         verContratos()
    elif opcion == "4":
         quit()
    else:
        print("ERROR: Seleccione una opción válida")
        opciones()

if __name__ == "__main__":
   empresa.leerFichero()
   opciones()
