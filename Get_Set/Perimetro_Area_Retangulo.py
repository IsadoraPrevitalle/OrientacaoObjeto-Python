class Retangulo:
    def __init__(self,base, alt):
        self.__base = base
        self.__altura = alt
        self.perimetro = 0
        self.area =0

    def get_base(self):
        print("Base: ",self.__base)

    def set_base(self,base):
        self.__base = base


    def get_altura(self):
        print("Altura: ",self.__altura)

    def set_altura(self,alt):
        self.__altura = alt

    def set_perimetro(self):
        self.__perimetro = (self.__altura*2) + (self.__base*2)

    def set_area(self):
        self.__area = self.__altura * self.__base


    def get_resultado(self,nome):
        print("Para o {}, dadas as medidas de base = {} e altura = {}, o resultado de seu perimetro é {}, e de sua area {} ".format(nome,self.__base, self.__altura,self.__perimetro, self.__area,))



