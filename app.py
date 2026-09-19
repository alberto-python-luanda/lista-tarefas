tarefas = []

while True:
    print("\n--- MINHA LISTA DE TAREFAS ---")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Sair")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        if len(tarefas) == 0:
            print("Nenhuma tarefa ainda!")
        else:
            for i, t in enumerate(tarefas):
                print(f"{i+1}. {t}")
    
    elif opcao == "2":
        nova = input("Digite a tarefa: ")
        tarefas.append(nova)
        print(f"Tarefa '{nova}' adicionada!")
    
    elif opcao == "3":
        print("Até logo!")
        break
