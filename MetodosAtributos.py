class Carro:
    def __init__ (self, cor, modelo, ano, odometro,):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.odometro = odometro 
    def get_cor(self):
        return self.cor
    def set_cor(self,novacor):
        self.cor = novacor


Mobi_Like = Carro (cor = "Branco", modelo = "Mobi", ano = 2020, odometro = 100000)

print("A  cor é:", Mobi_Like.get_cor())

Mobi_Like.set_cor("Vermelho")

print("A nova cor é:", Mobi_Like.get_cor() )
