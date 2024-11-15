from util import entrarNumero
import service
def menu():
    while True:
        escolha = entrarNumero("1 - Adicionar Tarefa\n" + 
                                "2 - Listar Tarefas\n" +
                                "3 - Marcar Tarefa como Concluída\n" +
                                "4 - Remover Tarefa\n" + 
                                "0 - Encerrar\n" +
                                "Escolha: ")
        if escolha == 1:
            service.addTarefa()
        elif escolha == 2:
            service.consultarTarefas()
        elif escolha == 3:
            service.concluirTarefa()
        elif escolha == 4:
            service.removerTarefa()
        elif escolha == 0:
            print("Encerrado!")
            break
        else:
            print("Escolha inválida!")
menu()