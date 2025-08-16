#RYAN LUKA SANTOS OLIVEIRA
#DANIEL ALISSON LOURENÇO DA SILVA
#KLISMA MATEUS CORDEIRO BARROS
#MATHEUS SANTOS DANTAS CAVALCANTI
#Projeto Ouvidoria

from operacoesbd import * #importa todas as funções do arquivo operacoesbd.py
from funcoes_sql import * #importa todas as funções do arquivo funcoes_sql.py
import os

conexao = criarConexao('localhost', 'root', '123456', 'ouvidoria')

while True:
    os.system('cls' if os.name == 'nt' else 'clear') #limpa a tela do terminal
    print("""
1. Listagem das Manifestações
2. Listagem de Manifestações por Tipo
3. Criar uma nova Manifestação
4. Exibir quantidade de Manifestações
5. Pesquisar uma Manifestação por código
6. Excluir uma Manifestação por código
7. Sair do sistema
""")
    try:
        opcao = int(input("Escolha uma opção: "))

        os.system('cls' if os.name == 'nt' else 'clear') #limpa a tela do terminal
        
        if opcao == 1:
            listar_manifestacoes(conexao)

        elif opcao == 2:
            listar_manifestacoes_por_tipo(conexao)
            
        elif opcao == 3:
            criar_manifestacao(conexao)
            
        elif opcao == 4:
            exibir_quantidade_manifestacoes(conexao)
        
        elif opcao == 5:
            pesquisar_manifestacao(conexao)
        
        elif opcao == 6:
            excluir_manifestacao(conexao)

        elif opcao == 7:
            print("Saindo...")
            print("Programa encerrado.") #sai do loop e encerra o programa
            break
        
        else:
            print("Opção inválida. Digite novamente.") #imprime mensagem de erro se a opção for inválida
        
        input("\nPressione Enter para continuar...") #aguarda o usuário pressionar Enter para continuar

    except ValueError:
        print("\nEntrada inválida. Digite um número válido.\n")
        input("\nPressione Enter para continuar...") #aguarda o usuário pressionar Enter para continuar

encerrarConexao(conexao) #encerra a conexão com o banco de dados