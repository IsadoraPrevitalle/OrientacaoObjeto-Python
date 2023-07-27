class Loja:
    def __init__(self, id, cliente, crédito):
        self.chave = id
        self.nome = cliente
        self.saldo = crédito
        self.limiteAtual = 0
        self.preco = 0


    def soma (self, quantidade, valor):
        self.preco = quantidade * valor
        self.LimiteAtual = self.saldo - self.preco

    def extrato (self):
        print("Prezada cliente {}, seu limite de crédito passou de {},00 para {},00 ao efetuar esta compra \nTenhe um bom dia e volte sempre".format(self.nome,self.saldo,self.LimiteAtual))

nom = input("Entre com seu nome ")
prod = input("Entre com o nome do produto ")
qt = int(input("Entre com a quantidade de produtos "))
v = int(input("Entre com o valor do produto "))

cliente1 = Loja(1, nom, 1500)

cliente1.soma(qt,v)
cliente1.extrato()