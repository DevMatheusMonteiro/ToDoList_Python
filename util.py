import mock

def entrarDescricao():
    while True:
        descricao = input("Entre com a descrição da tarefa: ")
        if(descricao == None or descricao.strip() == ""):
            print("Erro: descrição da tarefa nula ou vazia.")
        else:
            return descricao
def entrarNumero(texto):
    while True:
        try:
            numero = int(input(texto))
            return numero
        except:
            print("Erro: número inválido.")
def definirValorCodigo():
    if len(mock.tarefas) == 0:
        return 1
    return mock.tarefas[len(mock.tarefas)-1]["codigo"]+1