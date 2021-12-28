from modelo import*
import pickle
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
    def añadirSoftware(self, software):
        self.__listaSoftware.append(software)
        self.guardarFichero()

#Método para calcular el cobro total de todos los softwares contratados.
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
        for software in self.__listaSoftware:
            if isinstance(software, SoftwareExtranjero):
                if software.id == id:
                   cobro = software.cobro()
            if isinstance(software, SoftwareNacional):
                if software.id == id:
                   cobro = software.cobro()
        return cobro

#Método para contar la cantidad de contratos por un organismo nacional.
    def contratosOrganismo(self, organismo):
        total = 0
        for software in self.__listaSoftware:
            if isinstance(software, SoftwareNacional):
                if software.organismo == organismo:
                    total+=1
        return total

            
#Método para crear un fichero con la lista de softwares
    def guardarFichero(self):
        fichero = open("listaSoftware.dat", "wb")
        pickle.dump(self.listaSoftware, fichero)
        fichero.close()

#Método para cargar datos del fichero
    def leerFichero(self):
        try:
            fichero = open("listaSoftware.dat", "rb")
            self.__listaSoftware = pickle.load(fichero)
        except:
            FileNotFoundError



