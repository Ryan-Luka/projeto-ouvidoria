from operacoesbd import *

def listar_manifestacoes(conexao):
    consulta = "select * from manifestacoes"
    manifestacoes = listarBancoDados(conexao, consulta)
    for manifestacao in manifestacoes:
        print(f"Código: {manifestacao[0]}\nTipo: {manifestacao[1]}\nDescrição: {manifestacao[2]}")
    print()


def criar_manifestacao(conexao):
    while True: #loop para garantir que o tipo da manifestação seja válido
            tipo = int(input("""
Escolha o tipo da manifestação:
1. Reclamação
2. Sugestão
3. Elogio
4. denúncia
Opcão: """)) #solicita o tipo da manifestação
            if tipo in (1, 2, 3, 4): #verifica se o tipo da manifestação é válido
                if tipo == 1:
                    tipo = "Reclamação"
                elif tipo == 2:
                    tipo = "Sugestão"
                elif tipo == 3:
                    tipo = "Elogio"
                elif tipo == 4:
                    tipo = "Denúncia"
                mensagem = input("Digite a mensagem da manifestação: ").strip() #remove espaços em branco
                break #sai do loop se o tipo for válido
            else:
                print("Tipo inválido. Digite novamente.")
    consulta = "insert into manifestacoes (tipo, descricao) values (%s, %s)"
    dados = (tipo, mensagem) #cria uma tupla com os dados da manifestação
    insertNoBancoDados(conexao, consulta, dados) #chama a função insertNoBancoDados do arquivo operacoesbd.py

def pesquisar_manifestacao(conexao):
    consulta = "select * from manifestacoes"
    manifestacoes = listarBancoDados(conexao, consulta) #chama a função listarBancoDados do arquivo operacoesbd.py

    if len(manifestacoes) == 0: #verifica se a lista está vazia
        print("Nenhuma manifestação cadastrada.")
    else:
        codigo = int(input("Digite o código da manifestação que deseja pesquisar: "))
        consulta = "select * from manifestacoes where codigo = %s"
        dados = [codigo]
        manifestacao = listarBancoDados(conexao, consulta, dados)
        if len(manifestacao) == 0:
            print("Manifestação não encontrada.")
        else:
            print(f"Código: {manifestacao[0][0]}\nTipo: {manifestacao[0][1]}\nDescrição: {manifestacao[0][2]}")
    
def excluir_manifestacao(conexao):
    consulta = "select * from manifestacoes"
    manifestacoes = listarBancoDados(conexao, consulta)

    if len(manifestacoes) == 0: #verifica se a lista está vazia
        print("Nenhuma manifestação cadastrada.")
    else:
        codigo = int(input("Digite o código da manifestação que deseja excluir: "))
        consulta = "delete from manifestacoes where codigo = %s"
        dados = [codigo]
        linhas_afetadas = excluirBancoDados(conexao, consulta, dados)
        if linhas_afetadas == 0:
            print("Manifestação não encontrada.")
        else:
            print(f"Manifestação com código {codigo} excluída com sucesso.")

def exibir_quantidade_manifestacoes(conexao):
    conexao = criarConexao('localhost', 'root', '123456', 'ouvidoria')

    consulta = "select count(*) from manifestacoes"
    quantidade = listarBancoDados(conexao, consulta)
    if len(quantidade) == 0:
        print("Nenhuma manifestação cadastrada.")
    else:
        print(f"Quantidade de manifestações cadastradas: {quantidade[0][0]}")
    



