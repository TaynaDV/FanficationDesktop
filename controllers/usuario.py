from database.connection import get_connection

def cadastrar_usuario(username, email, senha, data_nasc):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_cadastrar_usuario ?, ?, ?, ?",
                   (username, email, senha, data_nasc))
    conn.commit()
    conn.close()

def buscar_usuario(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_buscar_usuario ?", (id_usuario,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def verificar_username(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_verificar_username ?", (username,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

def verificar_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_verificar_email ?", (email,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

def fazer_login(email, senha):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_fazer_login ?, ?", (email, senha))
    resultado = cursor.fetchone()
    conn.close()
    return resultado