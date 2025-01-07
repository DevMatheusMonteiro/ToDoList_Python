""" Arquivo que possui funções utilitárias """
import mock
from datetime import datetime
def entrarDescricao():
    """
    Função para receber descrição da tarefa, validá-la e retorná-la.
    """
    while True:
        descricao = input("Entre com a descrição da tarefa: ")
        if(descricao == None or descricao.strip() == ""):
            print("Erro: descrição da tarefa nula ou vazia.")
        else:
            return descricao
def entrarNumero(texto):
    """
    Função para receber um valor numérico, validá-lo e retorná-lo.

    Parâmetros:
    - texto (string)
    """
    while True:
        try:
            numero = int(input(texto))
            return numero
        except:
            print("Erro: número inválido.")
def definirValorId():
    """
    Função para incrementar id de acordo com o último id da lista.
    """
    if len(mock.tarefas) == 0:
        return 1
    return mock.tarefas[len(mock.tarefas)-1]["id"]+1
def dataParaString(data):
    """
    Função para converter a data para string no formato dd/mm/yyyy
    
    Parâmetros:
    - data (datetime)
    """
    return data.strftime("%d/%m/%Y")
def validarData():
    """
    Função para receber a data, validá-la e retorná-la.
    """
    while True:
        try:
            stringData = input("Entre com o prazo final no formato dd/mm/yyyy: ")
            data = datetime.strptime(stringData, "%d/%m/%Y")
            if data.date() < datetime.today().date():
                print("Erro: prazo final não pode ser menor que a data atual.")
            else:
                stringData = dataParaString(data)
                return stringData
        except:
            print("Erro: data inválida.")
