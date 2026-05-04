from database.connection import get_connection

conn = get_connection()
print("Conexão ok!")
conn.close()

from ui.login  import TelaLogin

app = TelaLogin()
app.mainloop() 