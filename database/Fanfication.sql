CREATE DATABASE Fanfication

USE Fanfication

CREATE TABLE Usuario(
id_usuario INT IDENTITY PRIMARY KEY,
username VARCHAR (30) UNIQUE NOT NULL,
email VARCHAR (100) UNIQUE NOT NULL,
senha VARCHAR (255) NOT NULL,
data_nasc DATE NOT NULL,
data_criacao DATETIME NOT NULL DEFAULT GETDATE()
);

CREATE TABLE historias(
id_livro INT IDENTITY PRIMARY KEY,
id_autor INT NOT NULL,
titulo VARCHAR (150) NOT NULL,
sinopse VARCHAR (500) NOT NULL,
data_his DATETIME DEFAULT GETDATE(),
status_his VARCHAR (50) CHECK (status_his IN ('Em andamento', 'Concluido', 'Pausado', 'Rascunho')) NOT NULL,
genero VARCHAR (50) CHECK (genero in ('Romance','Fantasia','Ficção Científica','Terror','Suspense','Fanfic','Conto','Poesia','Aventura')) NOT NULL,
FOREIGN KEY (id_autor) REFERENCES Usuario (id_usuario)
);

CREATE TABLE capitulos(
id_capitulo INT IDENTITY PRIMARY KEY, 
id_livro INT NOT NULL,
titulo VARCHAR (100) NOT NULL,
conteudo VARCHAR (MAX) NOT NULL,
ordem_cap INT NOT NULL,
data_cap DATETIME DEFAULT GETDATE(),
status_cap VARCHAR (50) CHECK (status_cap IN ('Rascunho', 'Publicado')),
CONSTRAINT uq_livro_ordem UNIQUE (id_livro, ordem_cap),
FOREIGN KEY (id_livro) REFERENCES historias (id_livro),
);

CREATE TABLE comentarios(
id_comentario INT IDENTITY PRIMARY KEY,
id_capitulo INT NOT NULL,
id_usuario INT NOT NULL,
num_paragrafo INT,
data_coment DATETIME NOT NULL DEFAULT GETDATE(),
comment VARCHAR (250) NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
FOREIGN KEY (id_capitulo) REFERENCES capitulos (id_capitulo)
);

CREATE TABLE avaliacao(
id_avaliacao INT IDENTITY PRIMARY KEY,
id_capitulo INT NOT NULL,
id_usuario INT NOT NULL,
voto_cap BIT NOT NULL,
CONSTRAINT uq_capitulo_usuario UNIQUE (id_capitulo, id_usuario),
FOREIGN KEY (id_capitulo) REFERENCES capitulos (id_capitulo),
FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
);

CREATE TABLE lista(
id_lista INT IDENTITY PRIMARY KEY,
id_usuario INT NOT NULL,
nomelista VARCHAR (50) NOT NULL,
CONSTRAINT uq_usuario_nomelista UNIQUE (id_usuario, nomelista),
FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
);

CREATE TABLE listahistoria(
id_listahistoria INT IDENTITY PRIMARY KEY,
id_lista INT NOT NULL,
id_livro INT NOT NULL,
CONSTRAINT uq_livro_lista UNIQUE (id_livro, id_lista),
FOREIGN KEY (id_lista) REFERENCES lista(id_lista),
FOREIGN KEY(id_livro) REFERENCES historias (id_livro)
);

CREATE TABLE biblioteca(
id_biblioteca INT IDENTITY PRIMARY KEY,
id_usuario INT NOT NULL,
id_livro INT NOT NULL,
id_capitulo INT NOT NULL,
num_paragrafo INT NOT NULL DEFAULT 1,
CONSTRAINT uq_usuario_livro UNIQUE (id_usuario, id_livro),
FOREIGN KEY (id_livro) REFERENCES historias (id_livro),
FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
FOREIGN KEY (id_capitulo) REFERENCES capitulos (id_capitulo)
);

------------------------------ PROCEDURES ------------------------------

CREATE PROCEDURE prc_cadastrar_usuario 
    @username VARCHAR(30),
    @email VARCHAR(100),
    @senha VARCHAR(255),
    @data_nasc DATE
AS 
BEGIN
    INSERT INTO Usuario (username, email, senha, data_nasc)
    VALUES (@username, @email, @senha, @data_nasc)
END
GO

CREATE PROCEDURE prc_publicar_historia
    @id_autor INT,
    @titulo VARCHAR(150),
    @sinopse VARCHAR(500),
    @status_his VARCHAR(50),
    @genero VARCHAR(50)
AS
BEGIN
    IF @status_his NOT IN ('Em andamento', 'Concluido', 'Pausado', 'Rascunho')
    BEGIN
        RAISERROR('Status inválido', 16, 1)
        RETURN
    END

    INSERT INTO historias(id_autor, titulo, sinopse, status_his, genero)
    VALUES (@id_autor, @titulo, @sinopse, @status_his, @genero)
END
GO

CREATE PROCEDURE prc_criar_capitulo
    @id_livro INT,
    @titulo VARCHAR(100),
    @conteudo VARCHAR(MAX),
    @ordem_cap INT,
    @status_cap VARCHAR(50)
AS
BEGIN
    INSERT INTO capitulos(id_livro, titulo, conteudo, ordem_cap, status_cap)
    VALUES (@id_livro, @titulo, @conteudo, @ordem_cap, @status_cap)
END
GO

CREATE PROCEDURE prc_votar_capitulo
    @id_capitulo INT,
    @id_usuario INT
AS
BEGIN
    INSERT INTO avaliacao(id_capitulo, id_usuario, voto_cap)
    VALUES (@id_capitulo, @id_usuario, 1)
END
GO

CREATE PROCEDURE prc_comentar_paragrafo
    @id_capitulo INT,
    @id_usuario INT,
    @num_paragrafo INT,
    @comment VARCHAR(250)
AS
BEGIN
    INSERT INTO comentarios(id_capitulo, id_usuario, num_paragrafo, comment)
    VALUES (@id_capitulo, @id_usuario, @num_paragrafo, @comment)
END
GO

CREATE PROCEDURE prc_adicionar_biblioteca
    @id_usuario INT,
    @id_livro INT,
    @id_capitulo INT
AS
BEGIN
    INSERT INTO biblioteca(id_usuario, id_livro, id_capitulo, num_paragrafo)
    VALUES (@id_usuario, @id_livro, @id_capitulo, 1)
END
GO

CREATE PROCEDURE prc_atualizar_progresso
    @id_usuario INT,
    @id_livro INT,
    @id_capitulo INT,
    @num_paragrafo INT
AS
BEGIN
    UPDATE biblioteca
    SET id_capitulo = @id_capitulo,
        num_paragrafo = @num_paragrafo
    WHERE id_usuario = @id_usuario 
    AND id_livro = @id_livro
END
GO

CREATE PROCEDURE prc_criar_lista
    @id_usuario INT,
    @nomelista VARCHAR(50)
AS
BEGIN
    INSERT INTO lista(id_usuario, nomelista)
    VALUES (@id_usuario, @nomelista)
END
GO

CREATE PROCEDURE prc_adicionar_lista
    @id_lista INT,
    @id_livro INT
AS
BEGIN
    INSERT INTO listahistoria(id_lista, id_livro)
    VALUES (@id_lista, @id_livro)
END
GO

CREATE PROCEDURE prc_buscar_username
    @username VARCHAR(30)
AS
BEGIN
    SELECT id_usuario FROM Usuario
    WHERE username = @username
END
GO

CREATE PROCEDURE prc_verificar_username
    @username VARCHAR(30)
AS
BEGIN
    SELECT id_usuario FROM Usuario
    WHERE username = @username
END
GO

CREATE PROCEDURE prc_verificar_email
    @email VARCHAR(100)
AS
BEGIN
    SELECT id_usuario FROM Usuario
    WHERE email = @email
END
GO
------------------------------ SELECTS ------------------------------

CREATE PROCEDURE prc_buscar_historia
    @id_livro INT
AS
BEGIN
    SELECT * FROM historias
    WHERE id_livro = @id_livro
END
GO

CREATE PROCEDURE prc_buscar_capitulos
    @id_livro INT
AS
BEGIN
    SELECT * FROM capitulos
    WHERE id_livro = @id_livro
    ORDER BY ordem_cap
END
GO

CREATE PROCEDURE prc_buscar_comentarios
    @id_capitulo INT
AS
BEGIN
    SELECT * FROM comentarios
    WHERE id_capitulo = @id_capitulo
    ORDER BY data_coment
END
GO

CREATE PROCEDURE prc_buscar_historias_genero
    @genero VARCHAR(50)
AS
BEGIN
    SELECT * FROM historias
    WHERE genero = @genero
    ORDER BY data_his DESC
END
GO

CREATE PROCEDURE prc_buscar_biblioteca
    @id_usuario INT
AS
BEGIN
    SELECT * FROM biblioteca
    WHERE id_usuario = @id_usuario
END
GO

CREATE PROCEDURE prc_buscar_listas
    @id_usuario INT
AS
BEGIN
    SELECT * FROM lista
    WHERE id_usuario = @id_usuario
END
GO

CREATE PROCEDURE prc_contar_votos_historia
    @id_livro INT
AS
BEGIN
    SELECT COUNT(*) AS total_votos
    FROM avaliacao a
    INNER JOIN capitulos c ON a.id_capitulo = c.id_capitulo
    WHERE c.id_livro = @id_livro
END
GO 

CREATE PROCEDURE prc_verificar_username
    @username VARCHAR(30)
AS
BEGIN
    SELECT id_usuario FROM Usuario
    WHERE username = @username
END
GO

CREATE PROCEDURE prc_verificar_email
    @email VARCHAR(100)
AS
BEGIN
    SELECT id_usuario FROM Usuario
    WHERE email = @email
END
GO

CREATE PROCEDURE prc_fazer_login
    @email VARCHAR(100),
    @senha VARCHAR(255)
AS
BEGIN
    SELECT id_usuario, username, email FROM Usuario
    WHERE email = @email AND senha = @senha
END
GO

------------------------------ TRIGGERS ------------------------------

CREATE TRIGGER trg_deletar_capitulos
ON historias
AFTER DELETE
AS
BEGIN
    DELETE FROM capitulos
    WHERE id_livro IN (SELECT id_livro FROM DELETED)
END
GO

CREATE TRIGGER trg_deletar_usuario
ON Usuario
AFTER DELETE
AS
BEGIN
    DELETE FROM comentarios
    WHERE id_usuario IN (SELECT id_usuario FROM DELETED)

    DELETE FROM avaliacao
    WHERE id_usuario IN (SELECT id_usuario FROM DELETED)

    DELETE FROM biblioteca
    WHERE id_usuario IN (SELECT id_usuario FROM DELETED)

    DELETE FROM lista
    WHERE id_usuario IN (SELECT id_usuario FROM DELETED)

    DELETE FROM historias
    WHERE id_autor IN (SELECT id_usuario FROM DELETED)
END
GO
SELECT * FROM Usuario
