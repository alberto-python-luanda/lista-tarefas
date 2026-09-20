
"""
Lista de Tarefas PRO - Luanda 🇦🇴
Por Alberto Filipe - Feito 100% no celular
Projeto 2 rumo ao Audi Q5!
Com sistema de conclusão e validação!
"""

tarefas = []

def adicionar_tarefa():
    nome = input("Digite a tarefa: ").strip()
    if nome:
        tarefas.append({"nome": nome, "feita": False})
        print(f"✅ '{nome}' adicionada!")
    else:
        print("❌ Não pode tarefa vazia!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("📭 Nenhuma tarefa ainda!")
        return
    print("\n--- MINHA LISTA DE TAREFAS ---")
    for i, t in enumerate(tarefas):
        status = "✅ FEITA" if t["feita"] else "⏳ Pendente"
        print(f"{i+1}. {status} - {t['nome']}")

def concluir_tarefa():
    listar_tarefas()
    if not tarefas:
        return
    try:
        num = int(input("Qual número concluir? ")) - 1
        if 0 <= num < len(tarefas):
            tarefas[num]["feita"] = True
            print(f"🎉 '{tarefas[num]['nome']}' concluída!")
        else:
            print("❌ Número inválido!")
    except ValueError:
        print("❌ Digite apenas números!")

# Programa principal
while True:
    print("\n--- MENU LUANDA ---")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        listar_tarefas()
    elif opcao == "2":
        adicionar_tarefa()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        print("Até logo, Alberto! 🚀 Rumo ao Q5!")
        break
    else:
        print("❌ Opção inválida!")