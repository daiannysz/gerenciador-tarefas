def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def listar_tarefas(tarefas):
    if tarefas:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa encontrada.")

def main():
    tarefas = []
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_tarefa(tarefas)
        elif escolha == '2':
            listar_tarefas(tarefas)
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
3

