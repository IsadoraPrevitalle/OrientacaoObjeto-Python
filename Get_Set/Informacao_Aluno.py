class Aluno:
    def __init__(self,nome,ra,n1,n2):
        self.__nome = nome
        self.__ra = ra
        self.__nota1 = n1
        self.__nota2 = n2
        self.__media = 0

    def get_nome(self):
        print("Nome: ",self.__nome)

    def set_nome(self,nome):
        self.__numero = nome



    def get_ra(self):
        print("RA: ",self.__ra)

    def set_ra(self,ra):
        self.__ra = ra




    def get_nota1(self):
        print('Nota 1 = ',self.__nota1)

    def set_nota1(self, n1):
        self.__nota1 = n1



    def get_nota2(self):
        print('Nota 2 = ', self.__nota2)

    def set_nota2(self, n2):
        self.__nota2 = n2


    def set_media(self):
        self.__media = (self.__nota1 + self.__nota2)/2
        print("{} sua nota final, dada sua nota 1 = {} e nota 2 = {} é {} ".format(self.__nome, self.__nota1, self.__nota2, self.__media))
        



