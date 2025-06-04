#RYAN LUKA SANTOS OLIVEIRA
#DANIEL ALISSON LOURENÇO DA SILVA
#KLISMA MATEUS CORDEIRO BARROS
#MATHEUS SANTOS DANTAS CAVALCANTI

from operacoesbd import * #importa todas as funções do arquivo operacoesbd.py
from funcoes_sql import * #importa todas as funções do arquivo funcoes_sql.py

conexao = criarConexao('localhost', 'root', '123456', 'ouvidoria')

while True:
    print("""
1. Listagem das manifestações
2. Listagem de manifestações por tipo
3. Criar uma nova manifestação
4. Pesquisar uma manifestação por código
5. Excluir uma manifestação por código
6. Exibir quantidade de manifestações
7. Sair do sistema
""")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        listar_manifestacoes(conexao)

    elif opcao == 2:
        print("manifestacoes por tipo")

    elif opcao == 3:
        criar_manifestacao(conexao)
        
    elif opcao == 4:
        pesquisar_manifestacao(conexao)
    
    elif opcao == 5:
        excluir_manifestacao(conexao)
    
    elif opcao == 6:
        exibir_quantidade_manifestacoes(conexao)

    elif opcao == 7:
        print("Saindo...")
        print("Programa encerrado.") #sai do loop e encerra o programa
        break
    else:
        print("Opção inválida. Digite novamente.") #imprime mensagem de erro se a opção for inválida
    
    input("\nPressione Enter para continuar...") #aguarda o usuário pressionar Enter para continuar

encerrarConexao(conexao) #encerra a conexão com o banco de dados