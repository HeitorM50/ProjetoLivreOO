PROJETO LIVRE DE OO - ESPECIFICAÇÕES 
1) aplicar ao projeto de OO
- herança 
- polimorfismo 
- encapsulamento 
2) recomendado: 
- usar como rascunho a UML 
- identificar classes 
- modelar as relações 
- comparações 
- abstrações 
- associação 
- dependências ( relação de de dependecia entre duas classes)
3) ReadME 
4) serialização de objetos 
- txt
- json
5) Utilização do terminal para IO
6) Pode usar interfaces gráficas 
7) Tema bem definido 
8) Preparar tudo em um repositório no GitHub
=========================================================================
> Foi implementado ao projeto , 5 exercicios dos conteúdos solicitado pelo professor :
CriarTelevisão.py que demosntra a utilização de uma classe construtora e do uso de métodos e atributos 
Encapsulamento.py que demonstra a utilização de encapsular instâncias de uma classe
MetodosAtributos.py demonstra a criação de um objeto 
HerançaePolimorfismo.py demonstra a utilização de herança e polimorfismo 
AlugaFacil.py junta todos os outros exercícios em um só código e com interação com o usuário e uso de JSON para serialização
=========================================================================
AlugaFacil.py :
 
Pré-requisitos:
- Python 3.10 ou superior
- Biblioteca padrão do Python (json, tkinter)

Passos:
1) Clone ou baixe o repositório.
2) Execute o arquivo principal.

-> O AlugaFácil é um sistema de gerenciamento de aluguel de carros, desenvolvido em Python com uma interface gráfica utilizando o módulo tkinter. O sistema permite listar carros disponíveis, alugar um carro, salvar os dados de carros em um arquivo JSON e carregar os dados salvos para continuar o gerenciamento.

-> Funcionalidades:
>Listar carros disponíveis e indisponíveis: Exibe os carros cadastrados com informações como modelo, placa, tarifa diária e status (disponível ou indisponível).
>Alugar um carro: Permite que o usuário selecione um carro pelo número correspondente na lista para alugar.
>Salvar dados: Armazena os dados dos carros em um arquivo JSON para uso posterior.
>Carregar dados: Recupera os dados salvos do arquivo JSON.
>Interface gráfica: Fácil de usar, com botões e campos de texto para interação.

-> Classes Principais:
- Carro:

-Representa um carro individual com atributos como placa, modelo, tarifa diária e status de disponibilidade.
-Métodos:
-alugar(): Marca o carro como alugado.
-devolver(): Marca o carro como disponível novamente.
-to_dict() e from_dict(): Conversões para salvar e carregar dados.

- SistemaAluguelCarros:

-Gerencia a lista de carros.
-Métodos:
-listar_carros(): Retorna uma lista formatada dos carros cadastrados.
-alugar_carro(indice): Aluga um carro com base no índice da lista.
-salvar_dados(arquivo): Salva a lista de carros em um arquivo JSON.
-carregar_dados(arquivo): Carrega os dados dos carros de um arquivo JSON.

-> Interface Gráfica (Tkinter)
A interface gráfica inclui:
- Um campo de texto para exibir a lista de carros.
- Botões para listar carros, alugar, salvar e carregar dados.
- Campo de entrada para selecionar o carro desejado pelo número.