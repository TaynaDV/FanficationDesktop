from database.connection import get_connection

conn = get_connection()
print("Conexão ok!")
conn.close()

from ui.app import App

app = App()
app.mainloop()