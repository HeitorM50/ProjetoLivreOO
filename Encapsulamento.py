class Pet:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
    def Imprimir_pet(self):
        print (f'Nome do Pet:', self.nome)
        print (f'Peso do Pet:', self.peso)
    
    def alimentarPet(self,comida):
        self.peso + comida 
    
class Abrigo:
    __catalogo = []

    def adicionarPet (self,pet):
        self.__catalogo.append(pet)
    
    def ImprimirAbrigo(self):
        print('Pets no Abrigo:')
        print('-----------------------')

        for pet in self.__catalogo:
            pet.Imprimir_pet()
            print('--------------')


abrigo = Abrigo()

pet = Pet('Jujuba', 10)
abrigo.adicionarPet(pet)

pet = Pet('Carlinhos', 90)
abrigo.adicionarPet(pet)

abrigo.ImprimirAbrigo()