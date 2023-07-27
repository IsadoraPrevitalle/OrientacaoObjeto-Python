class Conta:
    def __init__(self,nume,tit,saldo,limite):
        self.numero = nume
        self.titular = tit
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo += valor

    def extrato(self):
        print("número {}\nsaldo: {} ".format(self.numero, self.saldo))

conta1 = Conta('1','Isadora',100,1000)
conta1.deposita(100)
conta1.extrato()
conta1.saca(50)
conta1.extrato()