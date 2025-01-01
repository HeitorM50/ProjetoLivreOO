class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        return "Algum som genérico"

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!" 


class Gato(Animal):
    def fazer_som(self):
        return "Miau!"  

class Vaca(Animal):
    def fazer_som(self):
        return "Muuu!"  


def emitir_sons(animais):
    for animal in animais:
        print(f"{animal.nome} faz: {animal.fazer_som()}")

if __name__ == "__main__":

    cachorro = Cachorro("Rex")
    gato = Gato("Mimi")
    vaca = Vaca("Bela")

    lista_de_animais = [cachorro, gato, vaca]
    emitir_sons(lista_de_animais)
