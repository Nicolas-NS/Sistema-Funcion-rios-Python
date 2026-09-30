from time import sleep
from rich import print
from modularizacoes_util import ui
from services import cadastra_funcionario, pesquisar_funcionario,edita_funcionario,deletar_funcionario,carrega_funcionarios


caminho = "funcionario.json"

while True:
    opcao = ui.menu(["🧑 Cadastrar Funcionários","📖 Listar Funcionários","🔎 Pesquisar","✏️  Editar","🗑️  Deletar","🚪 Sair",])
    
    if opcao == 1:
        ui.titulo("Cadastro de Funcionários")
        nome = ui.input_texto("nome: ")
        idade = ui.input_idade("Idade: ")
        cargo = ui.input_texto("Cargo: ")
        salario = ui.input_float_positivo('Salário: ')
        cadastra_funcionario(caminho,nome,idade,cargo,salario)
        ui.linha()
        input("Apert Enter: ")
        
    elif opcao == 2:
        ui.titulo("Lista de funcionarios", cor='dark_blue')
        
        funcionarios = carrega_funcionarios(caminho)

        if funcionarios == None:
            ui.titulo("Arquivo não encontrado", cor='red')
        else:
            total = len(funcionarios)
            for n, p in enumerate(funcionarios):
                print(f"""[{n+1}] {p['nome']} [red]
    Idade: [/red]{p['idade']}[red]
    Cargo: [/red]{p['cargo']}[red]
    Salário: [/red]R$ {p['salario']:,.2f}""".replace(",", "X").replace(".", ",").replace("X", "."))
            print()
                    
            print(f"[red]total de funcionários: [/red] {total} ") 
            ui.linha(carat="=",cor="red")
        input("Apert Enter: ")
            
    
    elif opcao == 3:
        ui.titulo("Pesquisa de Funcionário")
        resultado = pesquisar_funcionario(caminho)

        if resultado is None:
            ui.titulo("Funcionário não encontrado!", cor="red")
        else:
            ui.titulo("Funcionário encontrado!")
            print(f"""[red]nome: [/red]{resultado['nome']}[red]
Idade: [/red]{resultado['idade']}[red]
Cargo: [/red]{resultado['cargo']}[red]
Salário: [/red]R${resultado['salario']:,.2f}""".replace(",", "X").replace(".", ",").replace("X", "."))
        ui.linha()
        input("Apert Enter: ")
        
    elif opcao == 4:
        resultado = edita_funcionario(caminho)
        if resultado == None:
            print("Arquivo não encontrado!")
        ui.linha()
        input("Apert Enter: ")
        
    elif opcao == 5:
        ui.titulo("Deletar Funcionnário")
        deletar_funcionario(caminho)
        ui.linha()
        input("Apert Enter: ")
        
    elif opcao == 6:
        print("Saindo do Sistema.", end = " ", flush=True)
        for p in range(0,3):
            sleep(0.5)
            print(".", end=" ",flush=True)
        break
    else: 
        print("Opção invalida!")


 
