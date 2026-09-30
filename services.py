import json
from rich import print
from modularizacoes_util import ui
import os

def carrega_funcionarios(caminho):
    if not os.path.exists(caminho):
            return None
    with open (caminho, 'r' ,encoding="utf-8") as arquivo:
        funcionarios = json.load(arquivo)
    return funcionarios

def salvar_funcionarios(caminho,funcionarios):
    with open (caminho,"w",encoding="utf-8") as arquivo:
        json.dump(funcionarios,arquivo,indent=4,ensure_ascii=False)
        
        
def cadastra_funcionario(caminho,nome,idade,cargo,salario):

    funcionarios = carrega_funcionarios(caminho)

    if funcionarios is None:
        funcionarios = []

    novo_funcionario = {
        "nome": nome,
        "idade": idade,
        "cargo": cargo,
        "salario": salario
    }

    funcionarios.append(novo_funcionario)

    salvar_funcionarios(caminho,funcionarios)
    
def mostra_funcionario(caminho):
    funcionarios = carrega_funcionarios(caminho)
    if funcionarios == None:
        return funcionarios
    return funcionarios
        

def pesquisar_funcionario(caminho):
    funcionarios = carrega_funcionarios(caminho)
    
    if funcionarios == None:
        print("arquivo não encontrado")
        return funcionarios
    else:
        n_pesquisa = input("nome do funcionário: ")
        
        for f in funcionarios:
            if n_pesquisa.lower().strip() == f['nome'].lower():
                
                return f
        return None
            
            
def edita_funcionario(caminho):
    funcionarios = carrega_funcionarios(caminho)
    
    if funcionarios == None:
        return funcionarios
    else:
        nome = input("Nome do funcionário: ")

        for funcionario in funcionarios:

            if funcionario["nome"].strip().lower() == nome.strip().lower():
                
                while True:
                    opcao = ui.menu(["nome",'idade','salário',"cargo"],txt="Editar informações")
                
                    if opcao == 1:
                        print(f"nome atual: {funcionario['nome']}")
                        novo = input("Novo nome: ")
                        funcionario["nome"] = novo
                        break
                    elif opcao == 2:
                        print(f"idade atual: {funcionario['idade']}")
                        novo = int(input("Nova idade: "))
                        funcionario["idade"] = novo
                        break
                    elif opcao == 3:
                        print(f"salário atual: {funcionario['salario']}")
                        novo = float(input("Novo salário: "))
                        funcionario["salario"] = novo
                        break
                    elif opcao == 4:
                        print(f"cargo atual: {funcionario['cargo']}")
                        novo = input("Novo cargo: ")
                        funcionario["cargo"] = novo
                        break
                    else: 
                        print("opçao invalida!")
                        

                salvar_funcionarios(caminho,funcionarios)
                print("arquivo atualizado com sucesso!")
                return

        ui.titulo("Funcionário não encontrado!")
    
def deletar_funcionario(caminho):
    funcionarios = carrega_funcionarios(caminho)
        
    if funcionarios == None:
        print("Arquivo não encontrado!")
        return funcionarios
    else:
        nome = input("Nome do funcionário: ")

        for funcionario in (funcionarios):
            if funcionario["nome"].strip().lower() == nome.strip().lower():
                confirma = input(f"Deseja remover funcionario {nome}? [S/N] ")
                if confirma[0].strip().lower().startswith("s"):
                    funcionarios.remove(funcionario)
                    
                    salvar_funcionarios(caminho,funcionarios)
                    ui.titulo(f"Funcionário {nome} removido do sistema!")
                    return
                else:
                    print("cancelado..")
                    return
        
        ui.titulo("Funcionário não encontrado!")
        return











