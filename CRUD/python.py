import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Senha2020@',
    database='bdyoutube',
)

cursor = conexao.cursor()
# cursor.execute('"Criar tabela"')

#CRUD
# Create
#CADASTRO DE PRODUTOS
while True:
    alternativas = int(input("""
| Digite 1 para cadastrar produto |
| 2 para ler os produtos no BDD |
| 3 para atualizar o produto no BDD |
| 4 para deletar o produto no BDD | 
| 5 Para reiniciar o banco de dados |
| 6 Para Sair do Programa | 
"""))




    if alternativas == 1:
        
        nome_produto = str(input('Digite o nome do produto: ')).lower()
        valor = float(input('Digite o valor do produto: R$  '))

        comando = f'INSERT into vendas  (nome_produto, valor) values ("{nome_produto}", {valor})'
        cursor.execute(comando)
        conexao.commit() #Editar o banco de dados
    #resultado = cursor.fetchall() #ler o banco de dados

    #Read
    if alternativas == 2:
        comando = 'Select * from vendas'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print('Resultado:', resultado)
    # Update

    if alternativas == 3:
        alternativaUpdtate = int(input("""Oque você quer mudar? 
| 1- Quer mudar o valor do item em vendas |
| 2- Quer Mudar o nome do produto 
"""))

        if alternativaUpdtate == 1:
            metodo = int(input("""
|1- Digite Qual o metodo que você quer mudar
|1- Pelo ID da venda |
|2- Pelo nome do produto |
"""))
            if metodo == 1:
                Idvendas = int(input("Digite o ID da onde você quer trocar o valor: "))
                valor = int(input("Digite o quanto você quer colocar: "))
                comando = f'UPDATE vendas set valor = {valor} where idVendas = {Idvendas}'
                cursor.execute(comando)
                conexao.commit()
            if metodo == 2:
                nome_produto = str(input("Digite o nome do produto que você deseja mudar o valor: ")).lower()
                if not nome_produto:
                    print("Nome digitado errado!")
                    continue
                valor = int(input("Digite o quanto você quer colocar: "))
                comando = f'UPDATE vendas set valor = {valor} where nome_produto = "{nome_produto}"'
                cursor.execute(comando)
                conexao.commit()
            else:
                print("Digite um valor válido!")
                continue

        if alternativaUpdtate == 2:
            alternativaupdate = int(input("""
|1- Digite Qual o metodo que você quer mudar
|1- Pelo ID da venda |
|2- Pelo Valor  |
"""))
            if alternativaupdate == 1:
                Idvendas = int(input("Digite O ID da onde você quer trocar o nome: "))
                nome_produto = str(input("Digite o nome do produto para o qual você quer alterar: "))
                comando = f'Update vendas set nome_produto = "{nome_produto}" where idVendas = {Idvendas}'
                cursor.execute(comando)
                conexao.commit()

            if alternativaupdate == 2:
                valor = int(input("Digite o valor da onde você quer mudar o nome:  "))
                nome_produto = str(input("Digite o nome do produto para o qual você quer alterar: "))
                comando = f'Update vendas set nome_produto = "{nome_produto}" where valor = {valor}'
                cursor.execute(comando)
                conexao.commit()
            else:
                print("Digite um valor válido!")
                continue

    


    # Delete
    #DELETAR PRODUTOS
    if alternativas == 4:
        metodo = int(input("""
| Como deseja deletar?
| 1 - Pelo ID da venda
| 2 - Pelo nome do produto
| 3 - Pelo valor do produto
"""))
        if metodo == 1:
            id_venda = int(input("Digite o ID da venda que deseja deletar: "))
            comando = f'DELETE FROM vendas WHERE idVendas = {id_venda}'
            cursor.execute(comando)
            conexao.commit()
            print("Venda deletada pelo ID com sucesso!")
        if metodo == 2:
            nome_produto = input("Digite o nome do produto que deseja deletar: ").lower()
            comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
            cursor.execute(comando)
            conexao.commit()
            print("Produto deletado pelo nome com sucesso!")
        if metodo == 3:
            valor = float(input("Digite o valor do produto que deseja deletar: "))
            comando = f'DELETE FROM vendas WHERE valor = {valor}'
            cursor.execute(comando)
            conexao.commit()
            print("Produto deletado pelo valor com sucesso!")
        else:
            print("Opção inválida!")

    #COMANDO CRIADO PELO GITHUBCOPILOT
    # Reiniciar o banco de dados
    if alternativas == 5:
        confirmar = input("Tem certeza que deseja apagar tudo e reiniciar os IDs? (S/N): ").upper()
        if confirmar[0] == 'S':
            cursor.execute('DELETE FROM vendas')
            cursor.execute('ALTER TABLE vendas AUTO_INCREMENT = 1')
            conexao.commit()
            print("Tabela reiniciada com sucesso!")


    elif alternativas == 6:
        print("Saindo do programa...")
        break;


        print("=" * 20)
cursor.close()
conexao.close()