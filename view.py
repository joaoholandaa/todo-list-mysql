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

# Função para adcionar tarefa ao banco de dados
def adcionar_tarefas(i):
  sql = "INSERT INTO tarefas (descricao, concluido) VALUES (%s, %s)"
  valores = (i, False)
  cursor.execute(sql, valores)
  meubd.commit()

# Função para obter todas as tarefas do banco de dados
def obter_tarefas():
  sql = "SELECT * FROM tarefas"
  cursor.execute(sql)
  return cursor.fetchall()

# Função para marcar uma tarefa como concluída
def marcar_completo(id_tarefa):
  sql = "UPDATE tarefas SET concluido = True WHERE id = %s"
  valores = (id_tarefa,)
  cursor.execute(sql, valores)
  meubd.commit()