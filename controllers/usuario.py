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

def atualizar_perfil(id_usuario, bio, foto_perfil):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_atualizar_perfil ?, ?, ?",
                   (id_usuario, bio, foto_perfil))
    conn.commit()
    conn.close()

def seguir_usuario(id_seguidor, id_seguido):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_seguir_usuario ?, ?",
                   (id_seguidor, id_seguido))
    conn.commit()
    conn.close()

def deixar_seguir(id_seguidor, id_seguido):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_deixar_seguir ?, ?",
                   (id_seguidor, id_seguido))
    conn.commit()
    conn.close()

def buscar_perfil(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_buscar_perfil ?", (id_usuario,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def buscar_seguidores(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_buscar_seguidores ?", (id_usuario,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def buscar_seguindo(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC prc_buscar_seguindo ?", (id_usuario,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado