
"""import mysql.connector # Futura conexão com um banco de dados local

conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="database_name"
)
"""

#Banco de dados de exemplo e teste
restaurants = [{"name": "Pé de Fava", "category": "Mineira", "active": True},
               {"name": "Mezzomo Colonial", "category": "Pizzaria", "active": True},
               {"name": "Zé da Pizza", "category": "Pizzaria", "active": False}
              ]