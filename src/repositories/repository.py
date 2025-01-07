""" Camada intermediária entre a aplicação e a fonte de dados """
from ..mock import tarefas
def addTarefa(tarefa):
    """ Função para adicionar tarefa à fonte de dados """
    tarefas.append(tarefa)
def removerTarefa(tarefa):
    """ Função para remover tarefa da fonte de dados """
    tarefas.remove(tarefa)
def encontrarPorId(id):
    """ Função para encontrar uma tarefa pelo id """
    return next((tarefa for tarefa in tarefas if tarefa["id"] == id),None)
def tarefasPendentes():
    """ Função que retornará tarefas pendentes """
    return list(filter(lambda x:x["concluido"]==False,tarefas))
def tarefasConcluidas():
    """ Função que retornará tarefas concluídas """
    return list(filter(lambda x:x["concluido"]==True,tarefas))
def todasTarefas():
    """ Função que retornará todas as tarefas"""
    return tarefas
def concluirTarefa(tarefa):
    """ Função que atualizará a tarefa para concluída """
    tarefa["concluido"] = True