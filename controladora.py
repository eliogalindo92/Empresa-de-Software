from modelo import*

class Empresa:

#lista polimórfica de todos los softwares contratados.
    __listaSoftware = []
   
#Métodos getter y setters (pythonicos) para añadir u obtener valores de los atributos de cada clase.
#Cada uno de ellos insertan y devuelven los valores de cada atributo.  
    @property
    def listaSoftware(self):
        return self.__listaSoftware

    @listaSoftware.setter
    def listaSoftware(self, listaSoftware):
        self.listaSoftware = listaSoftware

#Método para añadir softwares a la lista
    def añadirSoftware(self, sofware):
        self.__listaSoftware.append(sofware)

#Método para calcular el cobro total de todos los sofwares contratados.
    def cobroTotal(self):
        cobroTotal = 0
        cobroSoftExt = 0
        cobroSoftNac = 0
        for software in self.__listaSoftware:
            if isinstance(software, SoftwareExtranjero):
                cobroSoftExt = software.cobro()
            if isinstance(software, SoftwareNacional):
                cobroSoftNac = software.cobro()
        cobroTotal = cobroSoftExt + cobroSoftNac
        return cobroTotal


#Método para calcular el cobro dado el id del software.
    def cobroID(self, id):
        cobro = 0
        for sofware in self.__listaSoftware:
            if isinstance(sofware, SoftwareExtranjero):
                if sofware.id == id:
                    cobro = sofware.cobro()
            if isinstance(sofware, SoftwareNacional):
                if sofware.id == id:
                    cobro = sofware.cobro()
        return cobro

#Método para contar la cantidad de contratos por un organismo nacional.
    def contratosOrganismo(self, organismo):
        total = 0
        for software in self.__listaSoftware:
            if isinstance(software, SoftwareNacional):
                if software.__organismo == organismo:
                    total+=1
        return total

            
