from modelo import*
from controladora import Empresa

#softExt = SoftwareExtranjero(1, 100, 50, 'CodMAX', 600)
for i in range(6):
    print("Seleccione el software a añadir a la lista:\n 1. Software extranjero\n 2. Software nacional")
    valor = int(input("Teclee la opción deseada: "))

    if valor == 1:
        id = str(input("Teclee el id del software: "))
        lineasCod = int(input("Teclee la cantidad de líneas de código del software: "))
        horasTrab = float(input("Teclee las horas trabajadas en el software: "))
        empExt = str(input("Teclee el nombre de la empresa extranjera: "))
        impuesto = float(input("Teclee el impuesto a cobrar: ")) 
        Software = SoftwareExtranjero(id, lineasCod, horasTrab, empExt, impuesto)
        empresa = Empresa()
        empresa.añadirSoftware(Software)
        print(f"Cantidad de softwares en la lista: {len(empresa.listaSoftware)}")
    
    elif valor == 2:
        id = str(input("Teclee el id del software: "))
        lineasCod = int(input("Teclee la cantidad de líneas de código del software: "))
        horasTrab = float(input("Teclee las horas trabajadas en el software: "))
        organismo = str(input("Teclee el nombre del organismo: "))
        Software = SoftwareNacional(id, lineasCod, horasTrab, organismo)
        empresa = Empresa()
        empresa.añadirSoftware(Software)
        print(f"Cantidad de softwares en la lista: {len(empresa.listaSoftware)}")

    else:
        print("Seleccione una opción válida")
