contatos = []

def adicionar_contato(nome, telefone, email):
    contato = { 'nome': nome, 'telefone': telefone, 'email': email, 'favorito': False }
    contatos.append(contato)
    print(f"Contato {contato['nome']} adicionado com sucesso!")
    return

def visualizar_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        print(f"{indice}. Nome: {contato['nome']} | Telefone: {contato['telefone']} | Email: {contato['email']}")
    return

def editar_contato(contatos, indice):
    indice_ajustado = int(indice - 1)
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        nome_update = input("Digite o novo nome do contato: ")
        telefone_update = int(input("Digite o novo telefone do contato: "))
        email_update = input("Digite o novo email do contato: ")
        contatos[indice_ajustado]['nome'] = nome_update
        contatos[indice_ajustado]['telefone'] = telefone_update
        contatos[indice_ajustado]['email'] = email_update
    else:
        print("Contato não existe!")
    return

def marcar_contato_favorito(contatos, indice):
    indice_ajustado = int(indice - 1)
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        if contatos[indice_ajustado]['favorito'] == False:
            contato = contatos[indice_ajustado]
            contatos[indice_ajustado]["favorito"] = True
            print(f"Contato {contato['nome']} adicionado aos favoritos!")
        else:
            print(f"Contato já pertence aos favoritos!")
    else:
        print("Contato não existe!")
    return

def desmarcar_contato_favorito(contatos, indice):
    indice_ajustado = int(indice - 1)
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        if contatos[indice_ajustado]["favorito"]:
            contato = contatos[indice_ajustado]
            contatos[indice_ajustado]["favorito"] = False
            print(f"Contato {contato['nome']} removido dos favoritos!")
    else:
        print("Contato não é favorito ou não existe!")
    return

def visualizar_favoritos(contatos):
    print("\nLista de favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            print(f"{indice}. [✓] Nome: {contato['nome']} | Telefone: {contato['telefone']} | Email: {contato['email']}")
    return

def remover_contato(contatos, indice):
    indice_ajustado = int(indice - 1)
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        contato = contatos[indice_ajustado]
        contatos.remove(contato)
        print(f"Contato {contato['nome']} removido dos contatos!")
    else:
        print("Contato inválido")
    return