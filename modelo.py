#Clase padre Software
class Software:

#Método inicializador o constructor donde se crean las instancias atributos de la clase
    def __init__(self, id, lineasCod, horasTrab):
        self.__id = id
        self.__lineasCod = lineasCod
        self.__horasTrab = horasTrab
          
#Método abstracto que devuelve el cobro.
    def cobro(self):
        return 0.5*self.__lineasCod*self.__horasTrab

#Clase hija Software Extranjero
class SoftwareExtranjero(Software):

#Método inicializador o constructor donde se crean las instancias atributos de la clase
    def __init__(self, id, lineasCod, horasTrab, empExt, impuesto):
        super().__init__(id, lineasCod, horasTrab)
        self.__empExt = empExt
        self.__impuesto = impuesto

#Métodos getter y setters (pythonicos) para añadir u obtener valores de los atributos de cada clase.
#Cada uno de ellos insertan y devuelven los valores de cada atributo.
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def lineasCod(self):
        return self.__lineasCod

    @lineasCod.setter
    def lineasCod(self, lineasCod):
        self.__lineasCod = lineasCod
    
    @property
    def horasTrab(self):
        return self.__horasTrab

    @horasTrab.setter
    def horasTrab(self, horasTrab):
        self.__horasTrab = horasTrab
    
    @property
    def empExt(self):
        return self.__empExt

    @empExt.setter
    def empExt(self, empExt):
        self.__empExt = empExt

    @property
    def impuesto(self):
        return self.__impuesto

    @impuesto.setter
    def impuesto(self, impuesto):
        self.__impuesto = impuesto

#Método para calcular el cobro del software extranjero.
    def cobro(self):
        return super().cobro()*self.__impuesto

#Clase hija Software Nacional
class SoftwareNacional(Software):

#Método inicializador o constructor donde se crean las instancias atributos de la clase
    def __init__(self, id, lineasCod, horasTrab, organismo):
        super().__init__(id, lineasCod, horasTrab)
        self.__organismo = organismo
    
#Métodos getter y setters (pythonicos) para añadir u obtener valores de los atributos de cada clase.
#Cada uno de ellos insertan y devuelven los valores de cada atributo.
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def lineasCod(self):
        return self.__lineasCod

    @lineasCod.setter
    def lineasCod(self, lineasCod):
        self.__lineasCod = lineasCod
    
    @property
    def horasTrab(self):
        return self.__horasTrab

    @horasTrab.setter
    def horasTrab(self, horasTrab):
        self.__horasTrab = horasTrab
    
    @property
    def organismo(self):
        return self.__organismo

    @organismo.setter
    def organismo(self, organismo):
        self.__organismo = organismo

#Método para calcular el cobro del software nacional.
    def cobro(self):
        return super().cobro()