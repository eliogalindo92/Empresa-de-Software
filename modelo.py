#Clase padre Softare
class Software:
    def __init__(self, id, lineasCod, horasTrab):
        self.__id = id
        self.__lineasCod = lineasCod
        self.__horasTrab = horasTrab
        
    #Método para calcular 
    def cobro(self):
        return 0.5*self.__horasTrab

#Clase hija Software Extranjero
class SoftwareExtranjero(Software):
    def __init__(self, id, lineasCod, horasTrab, empExt, impuesto):
        super().__init__(id, lineasCod, horasTrab)
        self.__empExt = empExt
        self.__impuesto = impuesto


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    

    def cobro(self):
        return super().cobro()*self.__impuesto

#Clase hija Software Nacional
class SoftwareNacional(Software):
    def __init__(self, id, lineasCod, horasTrab, organismo):
        super().__init__(id, lineasCod, horasTrab)
        self.__organismo = organismo
    

    def cobro(self):
        return super().cobro()