import pyodbc


def get_connection():
    connection = pyodbc.connect(
        r"DRIVER={SQL Server};"
        r"SERVER=TBS0676765W11-1;"
        r"DATABASE=Fanfication;"
        r"Trusted_Connection=yes;"
    )
    return connection