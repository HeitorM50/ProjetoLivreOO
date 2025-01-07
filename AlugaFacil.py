import json

class Carro:
    def __init__(self, placa, modelo, tarifa_diaria):           
        self.placa = placa
        self.modelo = modelo
        self.tarifa_diaria = tarifa_diaria
        self.disponivel = True
#======================================================================================
    def get_tarifa_diaria(self):
        return self.tarifa_diaria

    def get_disponivel(self):
        return self.disponivel

    def set_disponivel(self, disponibilidade):
        self.disponivel = disponibilidade
#======================================================================================
    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O carro {self.modelo} ({self.placa}) foi alugado!")
        else:
            print(f"O carro {self.modelo} ({self.placa}) não está disponível.")

    def devolver(self):
        self.disponivel = True
        print(f"O carro {self.modelo} ({self.placa}) foi devolvido!")
#======================================================================================
    def to_dict(self):
        return {
            "placa": self.placa,
            "modelo": self.modelo,
            "tarifa_diaria": self.tarifa_diaria,
            "disponivel": self.disponivel
        }

    @classmethod
    def from_dict(cls, dados):
        carro = cls(dados["placa"], dados["modelo"], dados["tarifa_diaria"])
        carro.disponivel = dados["disponivel"]
        return carro

    def __str__(self):
        if self.disponivel: 
            status = "Disponível" 
        else:
            return "Indisponível"
        
        return f"Modelo: {self.modelo}, Placa: {self.placa}, Tarifa Diária: R${self.tarifa_diaria:.2f}, Status: {status}"
#======================================================================================
class SistemaAluguelCarros:
    def __init__(self):
        self.carros = self.inicializar_carros()

    def inicializar_carros(self):
        return [
            Carro("PBX6850", "Jeep Renegade", 120.00),
            Carro("JKO5678", "Honda Civic", 130.00),
            Carro("JPK7869", "Volkswagen Jetta", 150.00),
            Carro("PQR1357", "Renault Logan", 180.00),
            Carro("DEF7890", "Volkswagen Golf", 140.00),
            Carro("GHI2180", "Volkswagen Up TSI", 100.00)
        ]
#======================================================================================
    def listar_carros(self):
        for i, carro in enumerate(self.carros):
            print(f"{i + 1}. {carro}")

    def alugar_carro(self, indice_carro):
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
#======================================================================================
    def salvar_dados(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump([carro.to_dict() for carro in self.carros], arquivo, indent=4)
        print("Dados salvos com sucesso!")

    def carregar_dados(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
                self.carros = [Carro.from_dict(carro) for carro in dados]
            print("Dados carregados com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
#======================================================================================
def main():
    sistema = SistemaAluguelCarros()
    nome_arquivo = "dados_aluguel.json"  

    while True:
        print("\n===== ALUGA FÁCIL =====")
        print("1) Listar carros")
        print("2) Alugar carro")
        print("3) Devolver carro")
        print("4) Salvar dados")
        print("5) Carregar dados")
        print("6) Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            sistema.listar_carros()
            input("\nPressione Enter para voltar ao menu...")  

        elif escolha == '2':
            sistema.listar_carros()
            try:
                indice_carro = int(input("\nEscolha o número do carro a alugar: "))
                sistema.alugar_carro(indice_carro)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        elif escolha == '3':
            sistema.listar_carros()
            try:
                indice_carro = int(input("\nEscolha o número do carro a devolver: "))
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
