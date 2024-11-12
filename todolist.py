def addTarefa(lista, tarefa):
    while True:
        if(tarefa == None | tarefa.strip() == ""):
            print("Erro: tarefa nula ou vazia.")
        else:
            lista.append(tarefa)
def encontrarPorCodigo(lista,codigo):
    return list(filter(lambda x: x["codigo"] == codigo,lista))[0]
def concluirTarefa(lista, codigo):
    tarefa = encontrarPorCodigo(lista,codigo)
    tarefa["concluido"] = True
tarefas = [{"codigo": 1, "descrição": "Estudar python", "concluido": False}]
concluirTarefa(tarefas,1)
print(tarefas)