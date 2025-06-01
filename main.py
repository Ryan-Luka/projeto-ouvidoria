#RYAN LUKA SANTOS OLIVEIRA
#DANIEL ALISSON LOURENÇO DA SILVA
#KLISMA MATEUS CORDEIRO BARROS
#MATHEUS SANTOS DANTAS CAVALCANTI

from funcoes import * #importa todas as funções do arquivo funcoes.py
#manifestacoes = []

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
        listar_manifestacoes() #chama a função listar_manifestacoes do arquivo funcoes.py
    elif opcao == 2:
        listar_manifestacoes_por_tipo() #chama a função listar_manifestacoes_por_tipo do arquivo funcoes.py 
    elif opcao == 3:
        #criar_manifestacao() #chama a função criar_manifestacao do arquivo funcoes.py
        criar_manifestacao_por_tipo()
    elif opcao == 4:
        pesquisar_manifestacao() #chama a função buscar_manifestacao do arquivo funcoes.py
    elif opcao == 5:
        excluir_manifestacao() #chama a função excluir_manifestacao do arquivo funcoes.py
    elif opcao == 6:
        quantidade_manifestacoes() #chama a função quantidade_manifestacoes do arquivo funcoes.py
    elif opcao == 7:
        print("Saindo...")
        print("Programa encerrado.") #sai do loop e encerra o programa
        break
    else:
        print("Opção inválida. Digite novamente.") #imprime mensagem de erro se a opção for inválida
    
    input("\nPressione Enter para continuar...") #aguarda o usuário pressionar Enter para continuar