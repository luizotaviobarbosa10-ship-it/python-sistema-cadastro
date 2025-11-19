import os

usuarios = []

def carregar_dados():
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as f:
            for linha in f:
                usuarios.append(linha.strip())

def salvar_dados():
    with open("usuarios.txt", "w") as f:
        for u in usuarios:
            f.write(u + "\n")

def cadastrar():
    nome = input("Digite o nome do usuário: ")
    usuarios.append(nome)
    salvar_dados()
    print("Usuário cadastrado!")

def listar():
    print("\n--- Usuários cadastrados ---")
    for u in usuarios:
        print("- ", u)

def excluir():
    nome = input("Nome do usuário para excluir: ")
    if nome in usuarios:
        usuarios.remove(nome)
        salvar_dados()
        print("Usuário excluído!")
    else:
        print("Usuário não encontrado.")

def menu():
    carregar_dados()
    while True:
        print("\n1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Excluir usuário")
        print("4 - Sair")
        opc = input("Escolha: ")

        if opc == "1":
            cadastrar()
        elif opc == "2":
            listar()
        elif opc == "3":
            excluir()
        else:
            break

menu()
