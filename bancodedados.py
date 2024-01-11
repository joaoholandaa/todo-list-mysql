import mysql.connector

# Conectar-se ao servidor MySQL
meubd = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "admin",
  database = "tarefas"
)

cursor = meubd.cursor()

# Criar banco de dados
#cursor.execute("CREATE DATABASE tarefas")

# Criar tabela 
cursor.execute("CREATE TABLE IF NOT EXISTS tarefas(id INT AUTO_INCREMENT PRIMARY KEY, descricao VARCHAR (255), concluido BOOLEAN)")