class Bomba:  
    def __init__(self, capacidade, preco):
        self.capacidade = capacidade
        self.preco = preco   
      
    def porValor(self,valor):
        litros = valor / self.preco
        self.capacidade = self.capacidade - litros
        return litros

    def porLitro(self, litros):
        valor = litros * self.preco
        self.capacidade = self.capacidade - litros
        return valor
      
    def alterarPreco(self, preco):
        self.preco = preco
      
    def encherBomba(self, litros):
        self.capacidade = self.capacidade + litros

bomba = Bomba(2000, 6.75)
print ("Abasteceu %f litros" % bomba.porValor(50))
print ("Abasteceu %f reais" % bomba.porLitro(50))
bomba.alterarPreco(2.49)
print ("Abasteceu %f reais" % bomba.porLitro(50),bomba.encherBomba(50))
print ("Capacidade: %f litros" % bomba.capacidade)