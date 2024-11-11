def addTarefa(lista, tarefa):
    while True:
        if(tarefa == None | tarefa.strip() == ""):
            print("Erro: tarefa nula ou vazio.")
        else:
            lista.append(tarefa)
def concluirTarefa(lista):
    



tarefas = [{codigo: 1, nome: "Lavar o banheiro", concluida: True}]