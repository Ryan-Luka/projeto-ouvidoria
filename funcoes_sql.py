from operacoesbd import *
import os

def listar_manifestacoes(conexao): #lista todas as manifestações cadastradas
    consulta = "select * from manifestacoes"
    manifestacoes = listarBancoDados(conexao, consulta)
    
    if len(manifestacoes) == 0: #verifica se a lista está vazia
        print("Nenhuma manifestação cadastrada.")
    else:
        print("Lista de Manifestações: \n")
        for manifestacao in manifestacoes:
            print(f"Código: {manifestacao[0]}\nTítulo: {manifestacao[1]}\nTipo: {manifestacao[2]}\nAutor: {manifestacao[3]}\nDescrição: {manifestacao[4]}\n")

def listar_manifestacoes_por_tipo(conexao):
    tipos_manifestacao = {
        1: "Reclamação",
        2: "Sugestão",
        3: "Elogio",
        4: "Denúncia"
    }
    
    consulta = "select * from manifestacoes"
    manifestacoes = listarBancoDados(conexao, consulta)
    
    if len(manifestacoes) == 0: #verifica se a lista está vazia
        print("Nenhuma manifestação cadastrada.")
    else:
        while True:
            try:
                print("Escolha o tipo da manifestação:")
                for chave, valor in tipos_manifestacao.items():
                    print(f"{chave}. {valor}")
                opcao = int(input("Opção: "))
                if opcao in tipos_manifestacao:
                    tipo_escolhido = tipos_manifestacao[opcao]
                    break
                else:
                    print("\nTipo inválido. Digite novamente... \n")
            except ValueError:
                print("\nEntrada inválida. Digite um número válido.\n")

        os.system('cls' if os.name == 'nt' else 'clear') #limpa a tela do terminal

        consulta = "select * from manifestacoes where tipo = %s"
        dados = [tipo_escolhido]
        manifestacoes = listarBancoDados(conexao, consulta, dados) #chama a função listarBancoDados do arquivo operacoesbd.py
                
        if len(manifestacoes) == 0: #verifica se a lista está vazia
            print(f"Nenhuma manifestação do tipo {tipo_escolhido} cadastrada.")
        else:
            print(f"Lista de Manifestações do tipo {tipo_escolhido}: \n")
            for manifestacao in manifestacoes:
                print(f"Código: {manifestacao[0]}\nTítulo: {manifestacao[1]}\nTipo: {manifestacao[2]}\nAutor: {manifestacao[3]}\nDescrição: {manifestacao[4]}\n")

def criar_manifestacao(conexao): #cria uma nova manifestação
    titulo = input("Digite o título da manifestação: ").strip() #remove espaços em branco
    nome = input("Digite o seu nome: ").strip() #remove espaços em branco
    
    tipos_manifestacao = {
        1: "Reclamação",
        2: "Sugestão",
        3: "Elogio",
        4: "Denúncia"
    }
    
    while True: #loop para garantir que o tipo da manifestação seja válido
        try:
            print("Escolha o tipo da manifestação:")
            for chave, valor in tipos_manifestacao.items():
                print(f"{chave}. {valor}")
            opcao = int(input("Opção: "))
            if opcao in tipos_manifestacao:
                tipo_escolhido = tipos_manifestacao[opcao]
                break
            else:
                print("\nTipo inválido. Digite novamente... \n")
        except ValueError:
            print("\nEntrada inválida. Digite um número válido.\n")

    while True: #loop para garantir que a descrição da manifestação seja válida
        descricao = input("\nDigite a mensagem da manifestação: ").strip() #remove espaços em branco
        if len(descricao) <= 3: #verifica se a descrição é maior que 3 caracteres
            print("\nA descrição deve ter mais de 3 caracteres. Digite novamente.\n")
        else:
            break #sai do loop se a descrição for válida

    consulta = "insert into manifestacoes (titulo, tipo, autor, descricao) values (%s, %s, %s, %s)" #consulta para inserir os dados da manifestação
    dados = (titulo, tipo_escolhido, nome, descricao) #cria uma tupla com os dados da manifestação
    insertNoBancoDados(conexao, consulta, dados) #chama a função insertNoBancoDados do arquivo operacoesbd.py
    print("\nManifestação cadastrada com sucesso!") #imprime mensagem de sucesso

def exibir_quantidade_manifestacoes(conexao): #exibe a quantidade de manifestações cadastradas
    consulta = "select count(*) from manifestacoes"
    quantidade = listarBancoDados(conexao, consulta)
    print(f"Quantidade de manifestações cadastradas: {quantidade[0][0]}")

def pesquisar_manifestacao(conexao):
    consulta = "select * from manifestacoes"
    manifestacoes = listarBancoDados(conexao, consulta) #chama a função listarBancoDados do arquivo operacoesbd.py

    if len(manifestacoes) == 0: #verifica se a lista está vazia
        print("Nenhuma manifestação cadastrada.")
    else:
        while True:
            try:
                codigo = int(input("Digite o código da manifestação que deseja pesquisar: "))
                print() #imprime uma linha em branco para melhor visualização
                consulta = "select * from manifestacoes where codigo = %s"
                dados = [codigo]
                manifestacao = listarBancoDados(conexao, consulta, dados)
                if len(manifestacao) == 0:
                    print("Manifestação não encontrada.")
                    break
                else:
                    print(f"Código: {manifestacao[0][0]}\nTítulo: {manifestacao[0][1]}\nTipo: {manifestacao[0][2]}\nAutor: {manifestacao[0][3]}\nDescrição: {manifestacao[0][4]}\n")
                    break
            except ValueError:
                print("\nEntrada inválida. Digite um número válido.\n")
    
def excluir_manifestacao(conexao):
    consulta = "select * from manifestacoes"
    manifestacoes = listarBancoDados(conexao, consulta)

    if len(manifestacoes) == 0: #verifica se a lista está vazia
        print("Nenhuma manifestação cadastrada.")
    else:
        while True:
            try:
                codigo = int(input("Digite o código da manifestação que deseja excluir: "))
                print() #imprime uma linha em branco para melhor visualização
                consulta = "delete from manifestacoes where codigo = %s"
                dados = [codigo]
                linhas_afetadas = excluirBancoDados(conexao, consulta, dados)
                if linhas_afetadas == 0:
                    print("Manifestação não encontrada.")
                    break
                else:
                    print(f"Manifestação com código {codigo} excluída com sucesso.")
                    break
            except ValueError:
                print("\nEntrada inválida. Digite um número válido.\n")

    



