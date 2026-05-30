import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="08072006",
    database="biblioteca"
)

cursor = conexao.cursor()
 
print("Conectado com sucesso")


print("===== BIBLIOTECA =====")
print("1 - Cadastrar livro")
print("2 - Ver livros")
print("3 - Deletar livro")
print ("4 - Editar livro")
print("5 - Cadastrar leitor")
print("6 - Ver leitores")
print ("7-Editar leitor")
print("8 - Cadastrar autor")
print("9 - Ver autores")
print ("10- Editar autor")
print("11 - Realizar empréstimo")
print("12 - Ver empréstimos")
print ("13 - Editar empréstimo")
print("0 - Sair")

opcao = input("Escolha uma opção: ")

#LIVROS

if opcao == "1":

    nome = input("Nome do livro: ")
    genero = input("Gênero do livro: ")
    data = input("Data de lançamento (AAAA-MM-DD): ")

    comando = f"""
    INSERT INTO tbl_livros
    (nome_livro, genero_livro, dt_lancamento_livro)

    VALUES
    ('{nome}', '{genero}', '{data}') """

    cursor.execute(comando)
    conexao.commit()

    print("Livro cadastrado com sucesso!")

# parte para ver os livros cadastrado
elif opcao == "2":

    comando = "SELECT * FROM tbl_livros"

    cursor.execute("SELECT * FROM tbl_livros")

    resultado = cursor.fetchall()

    print(" livros cadastrado")

    for livro in resultado:
        print(livro)

    # a parte do delete#

elif opcao == '3':

    id_livro = input("Digite o ID do livro: ")

    comando = f"""
    DELETE FROM tbl_livros
    WHERE id_livro = {id_livro}
    """

    cursor.execute(comando)
    conexao.commit()

    print("\nLivro deletado com sucesso!")

elif opcao == "4":   

    id_livro = input("Digite o ID do livro: ")

    novo_nome = input("Novo nome do livro: ")
    novo_genero = input("Novo gênero do livro: ")
    nova_data = input("Nova data de lançamento (AAAA-MM-DD): ")

    comando = f"""
    UPDATE tbl_livros
    SET
    nome_livro = '{novo_nome}',
    genero_livro = '{novo_genero}',
    dt_lancamento_livro = '{nova_data}'

    WHERE id_livro = {id_livro}
    """

    cursor.execute(comando)
    conexao.commit()

    print("\nLivro atualizado com sucesso!")

    #LEITORES

elif opcao == "5":

    nome = input("Nome do leitor: ")
    cpf = input("CPF do leitor: ")
    data = input("Data de nascimento (AAAA-MM-DD): ")

    comando = f"""
    INSERT INTO tbl_leitores
    (nome_leitor, cpf_leitor, dt_nasc_leitor)

    VALUES
    ('{nome}', '{cpf}', '{data}')
    """

    cursor.execute(comando)
    conexao.commit()

    print("\nLeitor cadastrado com sucesso!")

elif opcao == "6":

    comando = "SELECT * FROM tbl_leitores"

    cursor.execute(comando)

    resultado = cursor.fetchall()

    print("\n===== LEITORES =====")

    for leitor in resultado:
        print(leitor)

elif opcao == "7":

    id_leitor = input("Digite o ID do leitor: ")

    novo_nome = input("Novo nome do leitor: ")
    novo_cpf = input("Novo CPF: ")
    nova_data = input("Nova data de nascimento (AAAA-MM-DD): ")

    comando = f"""
    UPDATE tbl_leitores
    SET
    nome_leitor = '{novo_nome}',
    cpf_leitor = '{novo_cpf}',
    dt_nasc_leitor = '{nova_data}'

    WHERE id_leitor = {id_leitor}
    """

    cursor.execute(comando)
    conexao.commit()

    print("\nLeitor atualizado com sucesso!")

#AUTORES

elif opcao == "8":

    nome = input("Nome do autor: ")
    data = input("Data de nascimento (AAAA-MM-DD): ")

    comando = f"""
    INSERT INTO tbl_autores
    (nome_autor, dt_nasc_autor)

    VALUES
    ('{nome}', '{data}')
    """

    cursor.execute(comando)
    conexao.commit()

    print("\nAutor cadastrado com sucesso!")

elif opcao == "9":

    comando = "SELECT * FROM tbl_autores"

    cursor.execute(comando)

    resultado = cursor.fetchall()

    print("\n===== AUTORES =====")

    for autor in resultado:
        print(autor)

elif opcao == "10":

    id_autor = input("Digite o ID do autor: ")

    novo_nome = input("Novo nome do autor: ")
    nova_data = input("Nova data de nascimento (AAAA-MM-DD): ")

    comando = f"""
    UPDATE tbl_autores
    SET
    nome_autor = '{novo_nome}',
    dt_nasc_autor = '{nova_data}'

    WHERE id_autor = {id_autor}
    """

    cursor.execute(comando)
    conexao.commit()

    print("\nAutor atualizado com sucesso!")

#EMPRESTIMOS


elif opcao == "11":

    id_livro = input("ID do livro: ")
    id_leitor = input("ID do leitor: ")
    data = input("Data do empréstimo (AAAA-MM-DD): ")

    # fk_livro e fk_leitor são as chaves estrangeiras

    comando = f"""
    INSERT INTO emprestimo
    (dt_emprestimo, fk_livro, fk_leitor)

    VALUES
    ('{data}', '{id_livro}', '{id_leitor}')
    """

    cursor.execute(comando)
    conexao.commit()

    print("\nEmpréstimo realizado com sucesso!")

elif opcao == "12":

    comando = "SELECT * FROM emprestimo"

    cursor.execute(comando)

    resultado = cursor.fetchall()

    print("\n===== EMPRÉSTIMOS =====")

    for emprestimo in resultado:
        print(emprestimo)

elif opcao == "13":

    id_emprestimo = input("Digite o ID do empréstimo: ")

    novo_livro = input("Novo ID do livro: ")
    novo_leitor = input("Novo ID do leitor: ")
    nova_data = input("Nova data do empréstimo (AAAA-MM-DD): ")

    comando = f"""
    UPDATE emprestimo
    SET
    fk_livro = '{novo_livro}',
    fk_leitor = '{novo_leitor}',
    dt_emprestimo = '{nova_data}'

    WHERE id_emprestimo = {id_emprestimo}
    """

    cursor.execute(comando)
    conexao.commit()

    print("\nEmpréstimo atualizado com sucesso!")

#SAIR

elif opcao == "0":

    print("\nSistema encerrado!")

# OPÇÃO INVÁLIDA

else:

    print("\nOpção inválida!")

# FECHAR CONEXÃO

cursor.close()
conexao.close()