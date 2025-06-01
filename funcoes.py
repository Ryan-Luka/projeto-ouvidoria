manifestacoes = [] #lista para armazenar as manifestações

def listar_manifestacoes():
    if len(manifestacoes) == 0: #verifica se a lista está vazia
            print("Nenhuma manifestação cadastrada.")
    else:
        print("Manifestações cadastradas:")
        for manifestacao in range(len(manifestacoes)):
            print(f"{manifestacao+1}:") #imprime o número da manifestação
            for chave, valor in manifestacoes[manifestacao].items():
                 print(f"{chave.capitalize()}: {valor}") #imprime a chave e o valor da manifestação
            print()
            # print(f"{manifestacao+1}. {manifestacoes[manifestacao]}")#imprime a lista de manifestações

def criar_manifestacao_por_tipo():
    tipos = ("reclamação", "sugestão", "elogio", "denúncia") #tupla com os tipos de manifestações
    tipo = "" #variável para armazenar o tipo da manifestação
    while tipo not in tipos: #loop para garantir que o tipo informado seja válido
        print("Tipo inválido. Digite novamente.")
        tipo = input("Digite o tipo da manifestação (reclamação, sugestão, elogio, denúncia): ").strip().lower() #remove espaços em branco e converte para minúsculas
    mensagem = input("Digite a mensagem da manifestação: ").strip() #remove espaços em branco
    
    manifestacao = {
        "tipo": tipo,
        "descricao": mensagem
    }

    manifestacoes.append(manifestacao) #adiciona a manifestação na lista

def listar_manifestacoes_por_tipo():
    if len(manifestacoes) == 0: #verifica se a lista está vazia
        print("Nenhuma manifestação cadastrada.")
    else:
        tipo = input("Digite o tipo da manifestação (reclamação, sugestão, elogio, denúncia): ").strip().lower() #remove espaços em branco e converte para minúsculas
        print(f"Manifestações do tipo '{tipo}':")
        for manifestacao in manifestacoes:
            if manifestacao['tipo'] == tipo: #verifica se o tipo da manifestação é igual ao tipo informado
                print(f"- {manifestacao['descricao']}") #imprime a descrição da manifestação

def criar_manifestacao():
    while True: #loop para garantir que a manifestação não seja vazia
        reclamacao = input("Digite a manifestação: ").strip() #remove espaços em branco
        if reclamacao == "": #verifica se a manifestação é vazia
            print("Manifestação não pode ser vazia.")
        else:
            manifestacoes.append(reclamacao) #se a manifestação não for vazia, adiciona a manifestação na lista
            print("Manifestação criada com sucesso!")
            break #sai do loop

def pesquisar_manifestacao():
    if len(manifestacoes) == 0: #verifica se a lista está vazia
            print("Nenhuma manifestação cadastrada.")
    else:
        buscar = int(input("Digite o número da manifestação: "))
        if buscar >= 1 and buscar <= len(manifestacoes):
            print("Manifestação encontrada:")
            print(f"{buscar}. {manifestacoes[buscar-1]}") #imprime a manifestação encontrada
        else:
            print("Manifestação não encontrada.") #imprime mensagem de erro se não encontrar

def excluir_manifestacao():
    if len(manifestacoes) == 0: #verifica se a lista está vazia
            print("Nenhuma manifestação cadastrada.")
    else:
        buscar = int(input("Digite o número da manifestação: "))
        if buscar >= 1 and buscar <= len(manifestacoes):
            manifestacoes.pop(buscar-1) #remove a manifestação da lista
            print("Manifestação excluída.")
        else:
            print("Manifestação não encontrada.") #imprime mensagem de erro se não encontrar

def quantidade_manifestacoes():
    if len(manifestacoes) == 0: #verifica se a lista está vazia
            print("Nenhuma manifestação cadastrada.")
    else:
        print(f"Quantidade de manifestações: {len(manifestacoes)}") #imprime a quantidade de manifestações

