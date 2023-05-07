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


def validate_expression(expression):
    stack = Stack()
    opening_brackets = '([{'
    closing_brackets = ')]}'
    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            if closing_brackets.index(char) != opening_brackets.index(stack.pop()):
                return False
    return stack.is_empty()


def add_operation(queue):
    operation = input("Qual operação você deseja adicionar à fila? (+, -, *, /): ")
    valores = input("Digite os valores separados por vírgulas: ").split(',')
    queue.enqueue((operation, valores))
    print("Operação adicionada com sucesso!")


def execute_next_operation(queue):
    if queue.is_empty():
        print("A fila de operações está vazia.")
    else:
        operation, valores = queue.dequeue()
        result = eval(operation.join(valores))
        print(f"Operação: {operation}")
        print(f"Valores: {valores}")
        print(f"Resultado: {result}")


def execute_all_operations(queue):
    if queue.is_empty():
        print("A fila de operações está vazia.")
    else:
        while not queue.is_empty():
            execute_next_operation(queue)


def main():
    operation_queue = Queue()
    while True:
        print("MENU PRINCIPAL")
        print("1 - Operações")
        print("2 - Expressão")
        print("0 - Finalizar Programa")
        opcao_primaria = input("Escolha uma opção: ")
        if opcao_primaria == '1':
            while True:
                print("MENU DE OPERAÇÕES")
                print("1 - Adicionar Operação na Fila")
                print("2 - Executar Próxima Operação da Fila")
                print("3 - Executar Todas as Operações da Fila")
                print("0 - Voltar para o menu principal")
                sub_choice = input("Escolha uma opção: ")
                if sub_choice == '1':
                    add_operation(operation_queue)
                elif sub_choice == '2':
                    execute_next_operation(operation_queue)
                elif sub_choice == '3':
                    execute_all_operations(operation_queue)
                elif sub_choice == '0':
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif opcao_primaria == '2':
            expressao = input("Digite uma expressão matemática: ")
            if validate_expression(expressao):
                print("Expressão válida.")
            else:
                print("Expressão inválida.")
        elif opcao_primaria == '0':
            print("Finalizando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()
