from database.connection import get_connection

def publicar_historia(id_autor, titulo, sinopse, status_his, genero):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_publicar_historia ?, ?, ?, ?, ?",
                   (id_autor, titulo, sinopse, status_his, genero))
    conn.commit()
    conn.close()

def buscar_historia(id_livro):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_buscar_historia ?", (id_livro,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def buscar_historias_genero(genero):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_buscar_historias_genero ?", (genero,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def contar_votos_historia(id_livro):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_contar_votos_historia ?", (id_livro,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def buscar_historias_usuario(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_buscar_historias_usuario ?", (id_usuario,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado