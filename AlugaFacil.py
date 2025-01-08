import json
from tkinter import *

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
            {"placa": "PBX6850", "modelo": "Jeep Renegade", "tarifa_diaria": 160.00, "disponivel": True},
            {"placa": "JKO5678", "modelo": "Honda Civic", "tarifa_diaria": 130.00, "disponivel": True},
            {"placa": "JPK7869", "modelo": "Volkswagen Up TSI", "tarifa_diaria": 100.00, "disponivel": True},
            {"placa": "JPK7869", "modelo": "Fiat Mobi Like", "tarifa_diaria": 90.00, "disponivel": True},
            {"placa": "JPK7869", "modelo": "Renault Logan", "tarifa_diaria": 150.00, "disponivel": True},
            {"placa": "JPK7869", "modelo": "Chevrolet Onix", "tarifa_diaria": 120.00, "disponivel": True},
        ]

    def listar_carros(self):
        texto_carros = ""
        for i, carro in enumerate(self.carros, start=1):
            status = "Disponível" if carro["disponivel"] else "Indisponível"
            texto_carros += f"{i}. {carro['modelo']} ({carro['placa']}) - R${carro['tarifa_diaria']:.2f} - {status}\n"
        return texto_carros

    def alugar_carro(self, indice):
        try:
            carro = self.carros[indice - 1]
            if carro["disponivel"]:
                carro["disponivel"] = False
                return f"O carro {carro['modelo']} foi alugado com sucesso!"
            else:
                return f"O carro {carro['modelo']} não está disponível para aluguel."
        except IndexError:
            return "Carro inválido. Por favor, escolha um número da lista."

    def salvar_dados(self, arquivo):
        try:
            with open(arquivo, 'w') as f:
                json.dump(self.carros, f, indent=4)
            return "Dados salvos com sucesso!"
        except Exception as e:
            return f"Erro ao salvar dados: {e}"

    def carregar_dados(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                self.carros = json.load(f)
            return "Dados carregados com sucesso!"
        except FileNotFoundError:
            return "Arquivo não encontrado."
        except Exception as e:
            return f"Erro ao carregar dados: {e}"
#======================================================================================
def exibir_lista_carros():
    texto_carros = sistema.listar_carros()
    resultado.config(state=NORMAL)
    resultado.delete(1.0, END)
    resultado.insert(END, texto_carros)
    resultado.config(state=DISABLED)
    mensagem.config(text="Digite o número do carro que deseja alugar:")

def alugar_carro_usuario():
    try:
        indice = int(entrada.get())
        mensagem_resultado = sistema.alugar_carro(indice)
        mensagem.config(text=mensagem_resultado)
        exibir_lista_carros()  
    except ValueError:
        mensagem.config(text="Por favor, insira um número válido.")

def salvar_dados():
    mensagem_resultado = sistema.salvar_dados("dados_aluguel.json")
    mensagem.config(text=mensagem_resultado)

def carregar_dados():
    mensagem_resultado = sistema.carregar_dados("dados_aluguel.json")
    mensagem.config(text=mensagem_resultado)
    exibir_lista_carros() 
#======================================================================================
janela = Tk()
janela.title("AlugaFácil")

sistema = SistemaAluguelCarros()

texto_orientacao = Label(janela, text="Bem-vindo à ALUGA FÁCIL")
texto_orientacao.grid(column=0, row=0)

resultado = Text(janela, height=10, width=50, wrap=WORD, state=DISABLED)
resultado.grid(column=0, row=1)

botao_listar = Button(janela, text="Exibir Lista de Carros", command=exibir_lista_carros)
botao_listar.grid(column=0, row=2)

mensagem = Label(janela, text="")
mensagem.grid(column=0, row=3)

entrada = Entry(janela, width=10)
entrada.grid(column=0, row=4)

botao_alugar = Button(janela, text="Alugar Carro", command=alugar_carro_usuario)
botao_alugar.grid(column=0, row=5)

botao_salvar = Button(janela, text="Salvar Dados", command=salvar_dados)
botao_salvar.grid(column=0, row=6)

botao_carregar = Button(janela, text="Carregar Dados", command=carregar_dados)
botao_carregar.grid(column=0, row=7)

janela.mainloop()


