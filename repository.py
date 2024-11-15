from mock import tarefas
def addTarefa(tarefa):
    tarefas.append(tarefa)
def removerTarefa(tarefa):
    tarefas.remove(tarefa)
def encontrarPorCodigo(codigo):
    return list(filter(lambda tarefa: tarefa["codigo"] == codigo,tarefas))
def tarefasPendentes():
    return list(filter(lambda x:x["concluido"]==False,tarefas))
def tarefasConcluidas():
    return list(filter(lambda x:x["concluido"]==True,tarefas))
def todasTarefas():
    return tarefas
def concluirTarefa(tarefa):
    tarefa["concluido"] = True