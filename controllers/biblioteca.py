from database.connection import get_connection

def adicionar_biblioteca(id_usuario, id_livro, id_capitulo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_adicionar_biblioteca ?, ?, ?",
                   (id_usuario, id_livro, id_capitulo))
    conn.commit()
    conn.close()

def atualizar_progresso(id_usuario, id_livro, id_capitulo, num_paragrafo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_atualizar_progresso ?, ?, ?, ?",
                   (id_usuario, id_livro, id_capitulo, num_paragrafo))
    conn.commit()
    conn.close()

def buscar_biblioteca(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_buscar_biblioteca ?", (id_usuario,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado