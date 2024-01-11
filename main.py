# Importando o script view.py
from view import *

# Função para interagir com o usuário
def main():
  # Criando Menu
  while True:
    print("\n1. Adicionar tarefa\n2. Visualizar tarefas\n3. Marcar tarefa como concluída\n4. Excluir tarefa\n5. Sair")
    escolha = input('Digite a escolha (1-5): ')
    if escolha == '1':
      descricao = input("Digite a descrição da tarefa: ")
      adcionar_tarefas(descricao)
      print("Tarefa adicionada com sucesso!")

    elif escolha == "2":
      tarefas = obter_tarefas()
      if len(tarefas) == 0:
        print("Nenhuma tarefa encontrada.")
      else:
        for tarefa in tarefas:
          print(f"{tarefa[0]}. {tarefa[1]} - {'Concluída' if tarefa[2] else 'Incompleta'}")
    
    elif escolha == "3":
      id_tarefa = input("Digite o ID da tarefa: ")
      marcar_completo(id_tarefa)
      print("Tarefa marcada como concluída")

    elif escolha == "4":
      id_tarefa = input("Digite o ID da tarefa: ")
      deletar_tarefas(id_tarefa)
      print("Tarefa excluída")
    
    elif escolha == "5":
      break

    else:
      print("Escolha inválida")

if __name__ == "__main__":
  main()