from modelo import*

class Empresa:

    __listaSoftware = []
    @property
    def listaSoftware(self):
        return self.__listaSoftware

    @listaSoftware.setter
    def listaSoftware(self, listaSoftware):
        self.listaSoftware = listaSoftware

    def añadirSoftware(self, sofware):
        self.__listaSoftware.append(sofware)