import os
#Preenche um registro
def preenche_registro(t: list, reg: dict) -> None:
    print("PREENCHENDO O REGISTRO")
    reg['instagram'] = input("instagram: ")
    reg['nome'] = input("nome: ")
    reg['celular'] = input("celular: ")
    t.append(reg.copy())
    
#Exibir um registro específico
def exibe_registro(t: list, i: int) -> None:
    print(f"""
            REGISTRO...: {i}
            Instagram..: {t[i]['instagram']}
            Nome.......: {t[i]['nome']}
            Celular....: {t[i]['celular']}  
        """)
    print()
    
#Exibir todos o registros da tabela
def exibe_tabela(t: list) -> None:
    qtd_registros = len(t)
    for indice in range(qtd_registros):
        exibe_registro(t, indice)

        
#Preencher registros
def preencha_registros(t: list) -> None:
    print("PREENCHENDO REGISTROS MÚLTIPLOS (Digite '.' no Instagram para sair)")
    while True:
        reg = {}
        reg['instagram'] = input("Instagram (ou '.' para sair): ")
        if reg['instagram'] == '.':
            break
        reg['nome'] = input("Nome: ")
        reg['celular'] = input("Celular: ")
        t.append(reg.copy())
        
#Consultando registros
def consulta_registro(t: list, instagram: str) -> None:
    encontrado = False
    for i, reg in enumerate(t):
        if reg['instagram'] == instagram:
            exibe_registro(t, i)
            encontrado = True
            break
    if not encontrado:
        print("Instagram não existente")
    
#Principal
tabela = list()
contato = dict()

def rodar_sistema():
    while True:
        print(f"""
            MENU
            0 - SAIR
            1 - Cadastrar um contato
            2 - Exibe todos os registros da Tabela
            3 - Preencha registros
            4 - Consulta registros
            """)
        opcao = input("Digite a opção desejada: ")
        if opcao == '0':
            print("Encerrando o sistema!")
            break
        elif opcao == '1':
            preenche_registro(tabela, contato)
        elif opcao == '2':
            exibe_tabela(tabela)
        elif opcao == '3':
            preencha_registros(tabela)
        elif opcao == '4':     
            instagram_consulta = input("Digite o Instagram a ser consultado: ")
            consulta_registro(tabela, instagram_consulta)    
        else:
            print("Opção inválida, digite um item de 0 a 4.")
rodar_sistema()