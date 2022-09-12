class Calculator:

    def addition(self,a, b):
        return a + b
    
    def subtraction(self,a, b):
        return a - b

    def multipication(self,a, b):
        return a * b

    def division(self,a, b):
        return a / b


if __name__ == '__main__':
    #criação do objeto
    calc = Calculator()

    #comportamento observado
    result = calc.addition(2,2)

    #comportamento esperado
    esperado = 4

    #teste
    if result == esperado:
        print("Passou!") #teste passa
    else:
        print("Falhou") #teste falha