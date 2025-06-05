from operacoesbd import *

def listar_manifestacoes(conexao):
    consulta = "select * from manifestacoes"
    manifestacoes = listarBancoDados(conexao, consulta)
    if len(manifestacoes) == 0: #verifica se a lista está vazia
        print("Nenhuma manifestação cadastrada.")
    else:
        for manifestacao in manifestacoes:
            print(f"Código: {manifestacao[0]}\nTítulo: {manifestacao[1]}\nTipo: {manifestacao[2]}\nAutor: {manifestacao[3]}\nDescrição: {manifestacao[4]}\n")

def listar_manifestacoes_por_tipo(conexao):
    while True: #loop para garantir que o tipo da manifestação seja válido
        tipo = int(input("""Escolha o tipo da manifestação:
1. Reclamação
2. Sugestão
3. Elogio
Opcão: """)) #solicita o tipo da manifestação
        print() #imprime uma linha em branco para melhor visualização
        if tipo in (1, 2, 3): #verifica se o tipo da manifestação é válido
            if tipo == 1:
                tipo = "Reclamação"
            elif tipo == 2:
                tipo = "Sugestão"
            elif tipo == 3:
                tipo = "Elogio"
            consulta = "select * from manifestacoes where tipo = %s"
            dados = [tipo] #cria uma lista com o tipo da manifestação
            manifestacoes = listarBancoDados(conexao, consulta, dados) #chama a função listarBancoDados do arquivo operacoesbd.py
            if len(manifestacoes) == 0: #verifica se a lista está vazia
                print(f"Nenhuma manifestação do tipo {tipo} cadastrada.")
            else:
                for manifestacao in manifestacoes:
                    print(f"Código: {manifestacao[0]}\nTítulo: {manifestacao[1]}\nTipo: {manifestacao[2]}\nAutor: {manifestacao[3]}\nDescrição: {manifestacao[4]}\n")
            break #sai do loop se o tipo for válido
        else:
            print("Tipo inválido. Digite novamente.")

def criar_manifestacao(conexao):
    titulo = input("Digite o título da manifestação: ").strip() #remove espaços em branco
    nome = input("Digite o seu nome: ").strip() #remove espaços em branco
    while True: #loop para garantir que o tipo da manifestação seja válido
            tipo = int(input("""
Escolha o tipo da manifestação:
1. Reclamação
2. Sugestão
3. Elogio
4. denúncia
Opcão: """)) #solicita o tipo da manifestação
            print() #imprime uma linha em branco para melhor visualização
            if tipo in (1, 2, 3, 4): #verifica se o tipo da manifestação é válido
                if tipo == 1:
                    tipo = "Reclamação"
                elif tipo == 2:
                    tipo = "Sugestão"
                elif tipo == 3:
                    tipo = "Elogio"
                elif tipo == 4:
                    tipo = "Denúncia"
                descricao = input("Digite a mensagem da manifestação: ").strip() #remove espaços em branco
                break #sai do loop se o tipo for válido
            else:
                print("Tipo inválido. Digite novamente.")
    consulta = "insert into manifestacoes (titulo, tipo, autor, descricao) values (%s, %s, %s, %s)" #consulta para inserir os dados da manifestação
    dados = (titulo, tipo, nome, descricao) #cria uma tupla com os dados da manifestação
    insertNoBancoDados(conexao, consulta, dados) #chama a função insertNoBancoDados do arquivo operacoesbd.py

def pesquisar_manifestacao(conexao):
    consulta = "select * from manifestacoes"
    manifestacoes = listarBancoDados(conexao, consulta) #chama a função listarBancoDados do arquivo operacoesbd.py

    if len(manifestacoes) == 0: #verifica se a lista está vazia
        print("Nenhuma manifestação cadastrada.")
    else:
        codigo = int(input("Digite o código da manifestação que deseja pesquisar: "))
        print() #imprime uma linha em branco para melhor visualização
        consulta = "select * from manifestacoes where codigo = %s"
        dados = [codigo]
        manifestacao = listarBancoDados(conexao, consulta, dados)
        if len(manifestacao) == 0:
            print("Manifestação não encontrada.")
        else:
            print(f"Código: {manifestacao[0][0]}\nTítulo: {manifestacao[0][1]}\nTipo: {manifestacao[0][2]}\nAutor: {manifestacao[0][3]}\nDescrição: {manifestacao[0][4]}\n")
    
def excluir_manifestacao(conexao):
    consulta = "select * from manifestacoes"
    manifestacoes = listarBancoDados(conexao, consulta)

    if len(manifestacoes) == 0: #verifica se a lista está vazia
        print("Nenhuma manifestação cadastrada.")
    else:
        codigo = int(input("Digite o código da manifestação que deseja excluir: "))
        print() #imprime uma linha em branco para melhor visualização
        consulta = "delete from manifestacoes where codigo = %s"
        dados = [codigo]
        linhas_afetadas = excluirBancoDados(conexao, consulta, dados)
        if linhas_afetadas == 0:
            print("Manifestação não encontrada.")
        else:
            print(f"Manifestação com código {codigo} excluída com sucesso.")

def exibir_quantidade_manifestacoes(conexao):
    consulta = "select count(*) from manifestacoes"
    quantidade = listarBancoDados(conexao, consulta)
    print(f"Quantidade de manifestações cadastradas: {quantidade[0][0]}")
    



