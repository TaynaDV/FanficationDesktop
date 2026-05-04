import pyodbc


def get_connection():
    connection = pyodbc.connect(
        r"DRIVER={SQL Server};"
        r"SERVER=KorraDoraPRIME\SQLEXPRESS;"
        r"DATABASE=Fanfication;"
        r"Trusted_Connection=yes;"
    )
    return connection