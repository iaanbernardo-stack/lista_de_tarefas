def adicionar_tarefa (lista_de_tarefas, tarefa):
    """Adiciona nova tarefa a uma lista pre exisitente"""
    lista_de_tarefas.append(tarefa)
    print('\n')
    adicionada = "!Tarefa adicionada com sucesso!"
    print(f"{' ' * 15}{adicionada.upper()}")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    """Exibe lista de tarefa numerada"""
    lista = "> Lista de tarefas"
    print('\n')
    print(f"{' ' * 15}{lista.upper()}")
    print("-" *50)
    n = 1
    for tarefa in lista_de_tarefas:
            print(f"{n} - {tarefa}")
            n += 1
    print("-" * 50)

def deletar_tarefa(lista_de_tarefas, tarefa):
     """Deleta tarefa de uma lista pre-exisitente a partir do número dela"""
     lista_de_tarefas.pop((tarefa -1))
     print('\n')
     tarefa_excluida = "!Tarefa esxluída com sucesso!"
     print(f"{' ' * 15}{tarefa_excluida.upper()}")
     print (tarefa)
     return lista_de_tarefas

def exibir_menu():
     """Exibe menu com opções para a pessoas escolher"""
     escolha = "> Escolha uma opção"
     print("-" * 50)
     print(f"{' ' * 15}{escolha.upper()}\n\n" \
            "1 - Inserir nova tarefa\n" \
            "2 - Listar tarefas\n" \
            "3 - Deletar tarefa\n" \
            "4 - Sair"
        )
     print("-" * 50)

# Inicialização de variáveis
lista_de_tarefas = []
continuar = True

# Cabeçalho do programa
começo = "Vamos começar sua lista de tarefas?"
print(f"{' ' * 15}{começo.upper()}")
print('\n')

# Loop principal
while continuar:
    exibir_menu()
    opcao = input ("Insira o que deseja fazer: ")

    if opcao == "1": 
        tarefa = input('insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)  
    elif opcao == "3":
        # A validação verfica o valor é numerico, se é menor do que o limite da lista e se é menor ou igual a 0
        tarefa = input('Insira o número da tarefa que deseja deletar: ')
        print("\n")
        if not tarefa.isnumeric():
         invalido = "Número inválido! tente novamente."
         print(f"{invalido.upper()}")
        elif int(tarefa) > len(lista_de_tarefas):
         invalido = "Número inválido! tente novamente."
         print(f"{invalido.upper()}")
        elif int(tarefa) <= 0 :
         invalido = "Número inválido! tente novamente."
         print(f"{invalido.upper()}")
        else:
            deletar_tarefa(lista_de_tarefas, int(tarefa))
    elif opcao == "4":
        continuar = False
    else:
        print("\n")
        numero_valido = "insira um número válido."
        print(f"{numero_valido.upper()}")
    print('\n')
        