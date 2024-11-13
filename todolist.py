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
def definirValorCodigo(lista):
    if len(lista) == 0:
        return 1
    return lista[len(lista)-1]["codigo"]+1
def addTarefa(lista):
    codigo = definirValorCodigo(lista)
    descricao = entrarDescricao()
    tarefa = {"codigo": codigo, "descricao": descricao, "concluido": False}
    lista.append(tarefa)
def removerTarefa(lista):
    tarefa = encontrarPorCodigo(lista)
    if(tarefa == None):
        return print("Erro: tarefa não encontrada!")
    lista.remove(tarefa)
def encontrarPorCodigo(lista):
    codigo = entrarNumero("Entre com o código da tarefa: ")
    elemento = list(filter(lambda x: x["codigo"] == codigo,lista))
    if(len(elemento) == 0):
        return None
    return elemento[0]
def concluirTarefa(lista):
    tarefa = encontrarPorCodigo(lista)
    if(tarefa == None):
        return print("Erro: tarefa não encontrada!")
    tarefa["concluido"] = True
def filtrarTarefasPendentes(lista):
    return list(filter(lambda x:x["concluido"]==False,lista))
def filtrarTarefasConcluidas(lista):
    return list(filter(lambda x:x["concluido"]==True,lista))
def listarTarefas(lista):
    for tarefa in lista:
        print(tarefa)
def menuListar(lista):
    while True:
        escolha = entrarNumero("1 - Listar todas as tarefas\n2 - Listar tarefas concluídas\n3 - Listar tarefas pendentes\nEscolha: ")
        if escolha == 1:
            for tarefa in lista:
                print(tarefa)
            break
        elif escolha == 2:
            for tarefa in filtrarTarefasConcluidas(lista):
                print(tarefa)
            break
        elif escolha == 3:
            for tarefa in filtrarTarefasPendentes(lista):
                print(tarefa)
            break
        else:
            print("Escolha inválida!")
def menu(lista):
    while True:
        escolha = entrarNumero("1 - Adicionar Tarefa\n2 - Listar Tarefas\n3 - Marcar Tarefa como Concluída\n4 - Remover Tarefa\n0 - Encerrar\nEscolha: ")
        if escolha == 1:
            addTarefa(lista)
        elif escolha == 2:
            menuListar(lista)
        elif escolha == 3:
            concluirTarefa(lista)
        elif escolha == 4:
            removerTarefa(lista)
        elif escolha == 0:
            print("Encerrado!")
            break
        else:
            print("Escolha inválida!")

tarefas = [
    {"codigo": 1, "descricao": "Estudar Python", "concluido": False},
    {"codigo": 2, "descricao": "Ler um capítulo de livro", "concluido": True},
    {"codigo": 3, "descricao": "Praticar exercícios de lógica", "concluido": False},
    {"codigo": 4, "descricao": "Revisar conceitos de POO", "concluido": False},
    {"codigo": 5, "descricao": "Assistir vídeo sobre APIs", "concluido": True},
    {"codigo": 6, "descricao": "Resolver problemas no LeetCode", "concluido": False},
    {"codigo": 7, "descricao": "Aprender sobre listas em Python", "concluido": True},
    {"codigo": 8, "descricao": "Escrever resumo de aula", "concluido": False},
    {"codigo": 9, "descricao": "Estudar Flask", "concluido": False},
    {"codigo": 10, "descricao": "Ler sobre SQL", "concluido": True},
    {"codigo": 11, "descricao": "Praticar uso de dicionários", "concluido": False},
    {"codigo": 12, "descricao": "Testar funções em Python", "concluido": True},
    {"codigo": 13, "descricao": "Implementar algoritmo de ordenação", "concluido": False},
    {"codigo": 14, "descricao": "Estudar Django", "concluido": False},
    {"codigo": 15, "descricao": "Fazer resumo sobre MVC", "concluido": True},
    {"codigo": 16, "descricao": "Praticar com listas e tuplas", "concluido": False},
    {"codigo": 17, "descricao": "Aprender sobre módulos e pacotes", "concluido": True},
    {"codigo": 18, "descricao": "Escrever função recursiva", "concluido": False},
    {"codigo": 19, "descricao": "Assistir tutorial sobre SQLAlchemy", "concluido": False},
    {"codigo": 20, "descricao": "Estudar variáveis globais e locais", "concluido": True},
    {"codigo": 21, "descricao": "Revisar manipulação de strings", "concluido": False},
    {"codigo": 22, "descricao": "Ler artigo sobre Big Data", "concluido": True},
    {"codigo": 23, "descricao": "Estudar testes unitários", "concluido": False},
    {"codigo": 24, "descricao": "Fazer projeto pessoal em Python", "concluido": False},
    {"codigo": 25, "descricao": "Explorar bibliotecas externas", "concluido": True},
    {"codigo": 26, "descricao": "Escrever documentação de código", "concluido": False},
    {"codigo": 27, "descricao": "Fazer curso sobre Pandas", "concluido": True},
    {"codigo": 28, "descricao": "Implementar CRUD em SQL", "concluido": False},
    {"codigo": 29, "descricao": "Estudar programação funcional", "concluido": True},
    {"codigo": 30, "descricao": "Praticar lógica com listas encadeadas", "concluido": False}
]

menu(tarefas)