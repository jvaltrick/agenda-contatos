from my_functions import *

while True:
    print("\nMenu da Agenda de Contatos:")
    print("1. Adicionar contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar contato")
    print("4. Adicionar contato aos favoritos")
    print("5. Remover contato dos favoritos")
    print("6. Visualizar lista de contatos favoritos")
    print("7. Remover contato")
    print("8. Sair")

    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(nome, telefone, email)
    elif escolha == 2:
        visualizar_contatos(contatos)
    elif escolha == 3:
        visualizar_contatos(contatos)
        contato = int(input("Digite o número do contato que deseja editar: "))
        editar_contato(contatos, contato)
    elif escolha == 4:
        visualizar_contatos(contatos)
        contato = int(input("Digite o número do contato que deseja favoritar: "))
        marcar_contato_favorito(contatos, contato)
    elif escolha == 5:
        visualizar_favoritos(contatos)
        contato = int(input("Digite o número do contato que deseja remover dos favoritos: "))
        desmarcar_contato_favorito(contatos, contato)
    elif escolha == 6:
        visualizar_favoritos(contatos)
    elif escolha == 7:
        visualizar_contatos(contatos)
        contato = int(input("Digite o número do contato que deseja apagar: "))
        remover_contato(contatos, contato)
    else:
        break

print("\nAgenda Finalizada!")