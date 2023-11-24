#criação da classe (modelo) para a criação dos objetos sejam eles quais forem
#1ª coisa a ser criada é a classe.
import uuid
class Aluno: #exportar para o arquivo aluno.
    def __init__(self, nome, idade, curso, nota):
        self.matricula = uuid.uuid1() # número da matrícula gerada automaticamente.
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota

    def __repr__(self): # comportamento para imprimir o objeto
        return f"Matricula: {self.matricula} \n" \
               f"Nome: {self.nome} \n" \
               f"Idade: {self.idade} \n" \
               f"Curso: {self.curso} \n" \
               f"Nota: {self.nota}"

if __name__ == "__main__":
    a1 = Aluno("Jonas", 19, "Python", 9.8)
    print(a1)