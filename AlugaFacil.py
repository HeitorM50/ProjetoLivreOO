import pickle

class Carro:
    def __init__(self, placa, modelo, tarifa_diaria):           #criação da classe carro com os métodos e atributos
        self.placa = placa
        self.modelo = modelo
        self.__tarifa_diaria = tarifa_diaria
        self.__disponivel = True
#==========================================================================
    def get_tarifa_diaria(self):
        return self.__tarifa_diaria                             #Getters e Setters para retornar valores de tarifa e disponibilidade

    def get_disponivel(self):
        return self.__disponivel

    def set_disponivel(self, disponibilidade):
        self.__disponivel = disponibilidade
#==========================================================================
    def alugar(self):                                              # Métodos de Alugar e devolver 
        if self.__disponivel:
            self.__disponivel = False
            print(f"O carro {self.modelo} ({self.placa}) foi alugado!")
        else:
            print(f"O carro {self.modelo} ({self.placa}) não está disponível.")

    def devolver(self):
        self.__disponivel = True
        print(f"O carro {self.modelo} ({self.placa}) foi devolvido!")

    def __str__(self):
        status = "Disponível" if self.__disponivel else "Indisponível"
        return f"Modelo: {self.modelo}, Placa: {self.placa}, Tarifa Diária: R${self.__tarifa_diaria:.2f}, Status: {status}"

#==========================================================================
class CarroEconomico(Carro):                                        #Herança da Classe Carro
    def __init__(self, placa, modelo, tarifa_diaria):
        super().__init__(placa, modelo, tarifa_diaria * 0.9)         #Chama todos os métodos e atributos

    def __str__(self):
        status = "Disponível" if self.get_disponivel() else "Indisponível"
        return f"[Econômico] Modelo: {self.modelo}, Placa: {self.placa}, Tarifa Diária: R${self.get_tarifa_diaria():.2f}, Status: {status}"

#==========================================================================
class SistemaAluguelCarros:
    def __init__(self):
        self.carros = self.inicializar_carros()

    def inicializar_carros(self):
        return [
            Carro("ABC1234", "Toyota Corolla", 120.00),
            Carro("XYZ5678", "Honda Civic", 130.00),
            CarroEconomico("LMN2468", "Up  TSI", 150.00),
            CarroEconomico("PQR1357", "Mobi Like", 180.00),
            Carro("DEF7890", "Volkswagen Golf", 140.00),
            CarroEconomico("GHI2345", "Chevrolet Onix", 100.00)
        ]
#==========================================================================
    def listar_carros(self):                                      #Imprime a lista de carros com o laço for
        for i, carro in enumerate(self.carros):
            print(f"{i + 1}. {carro}")
#==========================================================================
    def alugar_carro(self, indice_carro):               #cria o objeto carro que terá um indice de 0 a 7, o -1 inclui o 0 para o usuário
        try:
            carro = self.carros[indice_carro - 1]
            carro.alugar()
        except IndexError:
            print("Carro inválido.")

    def devolver_carro(self, indice_carro):
        try:
            carro = self.carros[indice_carro - 1]
            carro.devolver()
        except IndexError:
            print("Carro inválido.")
#==========================================================================
    def salvar_dados(self, nome_arquivo):                       
        with open(nome_arquivo, 'wb') as arquivo:               #Uso da Biblioteca Pickle para salvar dados e carregar dados         
            pickle.dump(self.carros, arquivo)
        print("Dados salvos com sucesso!")

    def carregar_dados(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                self.carros = pickle.load(arquivo)
            print("Dados carregados com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
#==========================================================================
def main():
    sistema = SistemaAluguelCarros()
    nome_arquivo = "dados_aluguel.pkl" 

    while True:
        print("\n=====ALUGAFÁCIL=====")
        print("1) Listar carros")
        print("2) Alugar carro")
        print("3) Devolver carro")
        print("4) Salvar dados")
        print("5) Carregar dados")
        print("6) Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            sistema.listar_carros()
            input("\nPressione Enter para voltar ao menu") 

        elif escolha == '2':
            sistema.listar_carros()
            try:
                indice_carro = int(input("\nEscolha o número do carro que deseja alugar: "))
                sistema.alugar_carro(indice_carro)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        elif escolha == '3':
            sistema.listar_carros()
            try:
                indice_carro = int(input("\nEscolha o número do carro que queira devolver: "))
                sistema.devolver_carro(indice_carro)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        elif escolha == '4':
            sistema.salvar_dados(nome_arquivo)

        elif escolha == '5':
            sistema.carregar_dados(nome_arquivo)

        elif escolha == '6':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()