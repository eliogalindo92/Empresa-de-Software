from modelo import*
from controladora import Empresa

#Instancia de la clase Empresa(Controladora)
empresa = Empresa()

for i in range(3):
    print("Seleccione el software a añadir a la lista:\n 1. Software extranjero\n 2. Software nacional")
    valor = int(input("Teclee la opción deseada: "))

    if valor == 1:
        id = str(input("Teclee el id del software: "))
        lineasCod = int(input("Teclee la cantidad de líneas de código del software: "))
        horasTrab = float(input("Teclee las horas trabajadas en el software: "))
        empExt = str(input("Teclee el nombre de la empresa extranjera: "))
        impuesto = float(input("Teclee el impuesto a cobrar: ")) 
        Software = SoftwareExtranjero(id, lineasCod, horasTrab, empExt, impuesto)
        empresa.añadirSoftware(Software)
        print(f"Cantidad de softwares en la lista: {len(empresa.listaSoftware)}")
    
    elif valor == 2:
        id = str(input("Teclee el id del software: "))
        lineasCod = int(input("Teclee la cantidad de líneas de código del software: "))
        horasTrab = float(input("Teclee las horas trabajadas en el software: "))
        organismo = str(input("Teclee el nombre del organismo: "))
        Software = SoftwareNacional(id, lineasCod, horasTrab, organismo)
        empresa.añadirSoftware(Software)
        print(f"Cantidad de softwares en la lista: {len(empresa.listaSoftware)}")

    else:
        print("Seleccione una opción válida")


#Almaceno en cada variable el resultado que me devuelven los métodos creados en la clase Empresa y los imprimo
cobroTotal = empresa.cobroTotal()
cobroDadoID = empresa.cobroID('2')
contratosDadoOrg = empresa.contratosOrganismo('Desoft')
print(cobroTotal)
print(contratosDadoOrg)
print(cobroDadoID)
