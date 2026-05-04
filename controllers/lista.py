from database.connection import get_connection

def criar_lista(id_usuario, nomelista):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_criar_lista ?, ?",
                   (id_usuario, nomelista))
    conn.commit()
    conn.close()

def adicionar_lista(id_lista, id_livro):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_adicionar_lista ?, ?",
                   (id_lista, id_livro))
    conn.commit()
    conn.close()

def buscar_listas(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_buscar_listas ?", (id_usuario,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado