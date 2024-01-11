# Importando mysql
import mysql.connector

# Conectar ao servidor mysql
meubd = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "admin",
  database = "tarefas"
)

# Criando cursor
cursor = meubd.cursor()

#Função para adcionar tarefa ao bando de dados
def adcionar_tarefas(i):
  sql = "INSERT INTO tarefas (descricao, concluido) VALUES (%s, %s)"
  valores = (i, False)
  cursor.execute(sql, valores)
  meubd.commit()
