""" Camada que implementa as regras de negócio da aplicação """
from datetime import datetime
import util
import src.repositories.repository as repository
def encontrarPorId():
    """ Função que encontra tarefa por id e a retorna """
    id = util.entrarNumero("Entre com o id da tarefa: ")
    tarefa = repository.encontrarPorId(id)
    if not tarefa:
        return None
    return tarefa
def addTarefa():
    """ Função que adicionará uma nova tarefa """
    id = util.definirValorId()
    descricao = util.entrarDescricao()
    data_criacao = util.dataParaString(datetime.today())
    prazo_final = util.validarData()
    tarefa = {"id": id, "descricao": descricao, "concluido": False, "data_criacao": data_criacao, "prazo_final": prazo_final}
    repository.addTarefa(tarefa)
    print("Tarefa adicionada!")
def removerTarefa():
    """ Função que removerá uma tarefa """
    tarefa = encontrarPorId()
    if(tarefa == None):
        return print("Erro: tarefa não encontrada!")
    repository.removerTarefa(tarefa)
    print("Tarefa removida!")
def concluirTarefa():
    """ Função que concluirá uma tarefa """
    tarefa = encontrarPorId()
    if(tarefa == None):
        return print("Erro: tarefa não encontrada!")
    repository.concluirTarefa(tarefa)
    print("Tarefa concluída!")
def consultarTarefas():
    """ Função que permite consultar todas as tarefas, tarefas concluídas e tarefas pendentes """
    tarefas = []
    while True:
        escolha = util.entrarNumero("1 - Listar todas as tarefas\n" +
                                    "2 - Listar tarefas concluídas\n" +
                                    "3 - Listar tarefas pendentes\n" +
                                    "Escolha: ")
        if escolha == 1:
            tarefas = repository.todasTarefas()
            break
        elif escolha == 2:
            tarefas = repository.tarefasConcluidas()
            break
        elif escolha == 3:
            tarefas = repository.tarefasPendentes()
            break
        else:
            print("Escolha inválida!")
    if len(tarefas) == 0:
        return print("Nenhuma tarefa encontrada!")
    for tarefa in tarefas:
        print(tarefa)