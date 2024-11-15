from util import definirValorCodigo,entrarDescricao,entrarNumero
import repository
def encontrarPorCodigo():
    codigo = entrarNumero("Entre com o código da tarefa: ")
    tarefa = repository.encontrarPorCodigo(codigo)
    if(len(tarefa) == 0):
        return None
    return tarefa[0]
def addTarefa():
    codigo = definirValorCodigo()
    descricao = entrarDescricao()
    tarefa = {"codigo": codigo, "descricao": descricao, "concluido": False}
    repository.addTarefa(tarefa)
def removerTarefa():
    tarefa = encontrarPorCodigo()
    if(tarefa == None):
        return print("Erro: tarefa não encontrada!")
    repository.removerTarefa(tarefa)
def concluirTarefa():
    tarefa = encontrarPorCodigo()
    if(tarefa == None):
        return print("Erro: tarefa não encontrada!")
    repository.concluirTarefa(tarefa)
def consultarTarefas():
    while True:
        escolha = entrarNumero("1 - Listar todas as tarefas\n" +
                               "2 - Listar tarefas concluídas\n" +
                               "3 - Listar tarefas pendentes\n" +
                               "Escolha: ")
        if escolha == 1:
            for tarefa in repository.todasTarefas():
                print(tarefa)
            break
        elif escolha == 2:
            for tarefa in repository.tarefasConcluidas():
                print(tarefa)
            break
        elif escolha == 3:
            for tarefa in repository.tarefasPendentes():
                print(tarefa)
            break
        else:
            print("Escolha inválida!")