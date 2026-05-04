from database.connection import get_connection

def comentar_paragrafo(id_capitulo, id_usuario, num_paragrafo, comment):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_comentar_paragrafo ?, ?, ?, ?",
                   (id_capitulo, id_usuario, num_paragrafo, comment))
    conn.commit()
    conn.close()

def buscar_comentarios(id_capitulo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_buscar_comentarios ?", (id_capitulo,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado