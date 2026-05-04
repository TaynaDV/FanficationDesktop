from database.connection import get_connection

conn = get_connection()
print("Conexão ok!")
conn.close()

from ui.cadastro import TelaCadastro

app = TelaCadastro()
app.mainloop() 