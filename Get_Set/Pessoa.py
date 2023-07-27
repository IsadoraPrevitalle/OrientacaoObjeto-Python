class Nome:
    def __init__(self,nom, idd, nac):
        self.__nome = nom
        self.__idade = idd
        self.__nacionalidade = nac
        self.__horas =0

    def get_nome(self):
        print("Nome: {}".format(self.__nome))

    def set_nome(self,nom):
        self.__nome = nom


    def get_idade(self):
        print("Idade: {}".format(self.__idade))

    def set_idade(self,idd):
        self.__idade = idd


    def get_nacionalidade(self):
        print("Nacionalidade: {}".format(self.__nacionalidade))

    def set_nacionalidade(self,nac):
        self.__nacionalidade = nac


    def set_horas(self):
        self.__horas = (self.__idade * 365) * 24

    def set_maiorm(self):
        if (self.__idade >= 18):
            print("{} viveu {} horas, e é maior de idade".format(self.__nome, self.__horas))
        else:
            print("{} viveu {} horas, e é menor de idade".format(self.__nome, self.__horas))
