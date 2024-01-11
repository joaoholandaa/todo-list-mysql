import mysql.connector

# Conectar-se ao servidor MySQL
meubd = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "admin"
)

# Criando banco de dados
cursor = meubd.cursor()
cursor.execute("CREATE DATABASE tarefas")