from database.connection import get_connection

def criar_capitulo(id_livro, titulo, conteudo, ordem_cap, status_cap):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_criar_capitulo ?, ?, ?, ?, ?",
                   (id_livro, titulo, conteudo, ordem_cap, status_cap))
    conn.commit()
    conn.close()

def buscar_capitulos(id_livro):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_buscar_capitulos ?", (id_livro,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado