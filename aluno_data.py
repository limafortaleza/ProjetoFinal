'''construção do objeto de acesso a dados
instalar o pymysql
instalar o objeto de conexão'''
#2►B coisa a ser criada é a conexão com o banco.

import pymysql.cursors
from aluno import Aluno


class AlunoData:  # estebelece a conexão com o bando de dados.
    def __init__(self):
        self.conexao = pymysql.connect(host='localhost',
                                       user='root',
                                       password='',
                                       database='escola',
                                       cursorclass=pymysql.cursors.DictCursor)  # para as pesquisa virem em formato de dicionarios.
        self.cursor = self.conexao.cursor()  # para executar os comandos das querys.

    def insert(self,
               aluno: Aluno):  # instancia aluno da classe Aluno, para iserir na tabela tem que criar o objeto a ser inserido.
        try:
            sql = "INSERT INTO alunos VALUES (%s, %s,%s, %s,%s)"
            self.cursor.execute(sql, (aluno.matricula, aluno.nome, aluno.idade, aluno.curso, aluno.nota))
            self.conexao.commit()  # salva as alterações.
        except Exception as error:
            print(f'Erro ao inserir ! Erro:{error}')

    def select(self):  # lista todos os alunos.
        try:
            sql = "SELECT *FROM alunos"
            self.cursor.execute(sql)
            alunos = self.cursor.fetchall()  # fatia os alunos e coloca-os dentro de um dicionário (como linha)
            return alunos
        except Exception as error:
            print(f'Erro ao listar! Erro: {error}')

    def update(self, aluno: Aluno):  # atualiza tabela.
        try:
            sql = "UPDATE alunos SET nome= %s, idade =%s, curso=%s, nota=%s WHERE matricula =%s"
            self.cursor.execute(sql, (aluno.nome, aluno.idade, aluno.curso, aluno.nota, aluno.matricula))
            self.conexao.commit()  # salva as alterações
        except Exception as error:
            print(f'Erro ao atualizar! Erro {error}')

    def delete(self, matricula: str):
        try:
            sql = "DELETE FROM alunos WHERE matricula = %s"
            self.cursor.execute(sql, matricula)
            self.conexao.commit()
        except Exception as error:
            print(f'Erro ao deletar! Erro {error}')


if __name__ == '__main__':
    ad = AlunoData()  # criação do objeto de acesso a dados.

    # bloco para inserir o aluno
    # aluno=Aluno ('Jorge', 18, 'CSS', 9.3) #criar o objeto aluno dentro da tabela
    # ad.insert(aluno)

    # bloco de edição do aluno
    # aluno = Aluno('Ana', 41, 'HTML', 10)
    # aluno.matricula = '9ee0a7ae-8a61-11ee-94b8-0ae0afa10843'
    # ad.update(aluno)

    # bloco de deletar
    # ad.delete('cb3f385b-8a5e-11ee-8e03-0ae0afa10843')
    # print(ad.select())
    # ad.update('Maria', 21,'Python',9.2,'dd8730db-8a55-11ee-bff4-0ae0afa10843')
