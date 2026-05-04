from database.connection import get_connection

def votar_capitulo(id_capitulo, id_usuario):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_votar_capitulo ?, ?",
                   (id_capitulo, id_usuario))
    conn.commit()
    conn.close()