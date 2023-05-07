class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not bool(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return not bool(self.items)


def validacao_expressao(expressao):
    stack = Stack()
    opening_brackets = '([{'
    closing_brackets = ')]}'
    for char in expressao:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            if closing_brackets.index(char) != opening_brackets.index(stack.pop()):
                return False
    return stack.is_empty()


def add_operation(queue):
    print('---------- OPERAÇÕES ----------')
    print('Adição (+)')
    print('Subtração (-)')
    print('Multiplicação (*)')
    print('Divisão (/)')
    operacao = input("Qual operação você deseja adicionar à fila?  ")
    valores = input("Digite os VALORES separados por vírgulas: ").split(',')
    queue.enqueue((operacao, valores))
    print("Operação adicionada com sucesso!")


def execute_next_operation(queue):
    if queue.is_empty():
        print("A fila de operações está vazia.")
    else:
        operacao, valores = queue.dequeue()
        result = eval(operacao.join(valores))
        print(f"Operação: {operacao}")
        print(f"Valores: {valores}")
        print(f"Resultado: {result}")


def executar_operacoes(queue):
    if queue.is_empty():
        print("A fila de operações está vazia.")
    else:
        while not queue.is_empty():
            execute_next_operation(queue)


def main():
    operation_queue = Queue()
    while True:
        print("---------- MENU PRINCIPAL ----------")
        print("1 - Operações")
        print("2 - Expressão")
        print("0 - Finalizar Programa")
        opcao_menu_principal = input("Escolha uma opção: ")
        if opcao_menu_principal == '1':
            while True:
                print("---------- MENU DE OPERAÇÕES ----------")
                print("1 - Adicionar Operação na Fila")
                print("2 - Executar Próxima Operação da Fila")
                print("3 - Executar Todas as Operações da Fila")
                print("0 - Voltar para o menu principal")
                opcao_menu_operacoes = input("Escolha uma opção: ")
                if opcao_menu_operacoes == '1':
                    add_operation(operation_queue)
                elif opcao_menu_operacoes == '2':
                    execute_next_operation(operation_queue)
                elif opcao_menu_operacoes == '3':
                    executar_operacoes(operation_queue)
                elif opcao_menu_operacoes == '0':
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif opcao_menu_principal == '2':
            expressao = input("Digite uma expressão matemática: ")
            if validacao_expressao(expressao):
                print("Expressão válida.")
            else:
                print("Expressão inválida.")
        elif opcao_menu_principal == '0':
            print("Finalizando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == '__main__':
    main()
