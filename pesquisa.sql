CREATE DATABASE escola;
USE escola;

CREATE TABLE alunos(
	matricula VARCHAR (100) NOT NULL,
    nome VARCHAR (100) NOT NULL,
	idade INT NOT NULL,
    curso VARCHAR (100),
    nota float
);

SELECT * FROM alunos;
DESCRIBE alunos;