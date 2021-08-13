#clases = inicial mayuscula
#atributos y metodos = inicial minuscula
#metodos el nombre se aconseja que inicie con un verto
class ClaseEjemplo():
    #atributos
    valor1=0
    valor2=0
    #metodos
    #metodo para asignar datos al atributo valor1
    def setValor1(self, valor1):
        self.valor1 = valor1

    #metodo para obtener el contenido del atributo valor1
    def getValor1(self):
        return self.valor1

    def setValor2(self, valor2):
        self.valor2 = valor2

    def calcularSuma(self):
        return "la suma es: ", self.valor1 + self.valor2

    def calcularMulti(self):
        return "La multiplicacion es: ", self.valor1 * self.valor2

    def calcularPromedio(self):
        return ("el promedio es: ", (self.valor1 + self.valor2)/2)

    def verificarMayorMenor(self):
        respuesta=""
        if(self.valor1 > self.valor2):
            respuesta="el mayor es: ", self.valor1, " el menor es: ", self.valor2
        elif(self.valor2>self.valor1):
            respuesta="el mayor es: ", self.valor2, " el menor es: ", self.valor1
        else:
            respuesta="los numeros son inguales"

        return respuesta

    def verificarMayorMenor2(self):
        if(self.valor1 > self.valor2):
            return "el mayor es: ", self.valor1, " el menor es: ", self.valor2
        elif(self.valor2>self.valor1):
            return "el mayor es: ", self.valor2, " el menor es: ", self.valor1
        else:
            return "los numeros son inguales"

    def verificarMayorMenor3(self):
        if(self.valor1 > self.valor2):
            print("el mayor es: ", self.valor1, " el menor es: ", self.valor2)
        elif(self.valor2>self.valor1):
            print("el mayor es: ", self.valor2, " el menor es: ", self.valor1)
        else:
            print("los numeros son inguales")

        
