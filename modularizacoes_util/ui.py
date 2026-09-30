from rich import print

def linha(tam=42, carat='-',cor = "white"):
    """
    Exibe uma linha horizontal composta por um caractere repetido.

    Parâmetros:
        tam (int): Quantidade de caracteres da linha. Padrão: 42.
        carat (str): Caractere utilizado para formar a linha.
        Padrão: '-'.

    Exemplo:
        linha()
        ------------------------------------------

        linha(30, '=')
        ==============================
    """
    print(f"[{cor}]{tam * carat}[/{cor}]")


def titulo(txt='MENU PRINCIPAL', cor = "white"):
    """
    Exibe um título centralizado entre duas linhas.

    Parâmetros:
        txt (str): Texto que será exibido como título.
        Padrão: 'MENU PRINCIPAL'.

    Exemplo:
        titulo()
        ==========================================
                    MENU PRINCIPAL
        ==========================================

        titulo('CADASTRO DE CLIENTES')
    """
    linha(carat='=',cor=cor)
    print(f"[{cor}]{txt.center(42)}[{cor}]")
    linha(carat='=',cor=cor)
    
    
    
def validacao_int(mgs):
    """
    Solicita ao usuário um número inteiro e valida a entrada.

    Continua solicitando o valor até que o usuário digite
    um número inteiro válido.

    Parâmetros:
        mgs (str): Mensagem exibida para o usuário.

    Retorna:
        int: O número inteiro informado pelo usuário.

    Exemplo:
        idade = validacao_int('Digite sua idade: ')
    """
    while True:
        try:
            n = int(input(mgs))
        except ValueError:
            print("[red]Digite um número inteiro válido![/red]")
            continue
        else:
            return n

def input_int(texto):

    while True:

        try:
            return int(input(texto))

        except ValueError:
            print("[red]Digite um número inteiro válido![/red]")

def input_float_positivo(texto):

    while True:

        try:
            valor = float(input(texto))

            if valor < 0:
                print("[red]O valor não pode ser negativo![/red]")
                continue

            return valor

        except ValueError:
            print("[red]Digite um valor válido![/red]")
            
def input_idade(texto):

    while True:

        try:
            idade = int(input(texto))

            if idade < 14 or idade > 90:
                print("[red]Digite uma idade válida![/red]")
                continue

            return idade

        except ValueError:
            print("[red]Digite apenas números![/red]")

def input_texto(texto):

    while True:

        valor = input(texto).strip()

        if valor:
            return valor

        print("[red]Esse campo não pode ficar vazio![/red]")

def menu(lista, txt='MENU PRINCIPAL', cor = "white"):
    """
    Exibe um menu numerado e solicita uma opção ao usuário.

    Parâmetros:
        lista (list): Lista contendo as opções do menu.
        txt (str): Título exibido no topo do menu.
        Padrão: 'MENU PRINCIPAL'.

    Retorna:
        int: Número da opção escolhida pelo usuário.

    Exemplo:
        opcao = menu([
            'Cadastrar cliente',
            'Listar clientes',
            'Sair'
        ])

        O menu será exibido como:

        ==========================================
                    MENU PRINCIPAL
        ==========================================
        1-Cadastrar cliente
        2-Listar clientes
        3-Sair
        ------------------------------------------
        opção:
    """
    titulo(txt,cor)

    c = 1

    for item in lista:
        print(f"[{cor}]{c}-{item}[/{cor}]")
        c += 1

    linha()

    opc = validacao_int(f"Opção: ")

    return opc