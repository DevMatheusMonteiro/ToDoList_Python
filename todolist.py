def addTarefa(lista, tarefa):
    while True:
        if(tarefa == None | tarefa.strip() == ""):
            print("Erro: tarefa nula ou vazio.")
        else:
            lista.append(tarefa)
def encontrarPorCodigo(lista,codigo):
    list(filter(lambda x: x["codigo"] == codigo,lista))[0]
def concluirTarefa(lista, codigo):
    tarefa = encontrarPorCodigo(lista,codigo)
    return tarefa
tarefas = [{"codigo": 1, "descrição": "Estudar python", "concluido": True}]
print(concluirTarefa(tarefas,1))