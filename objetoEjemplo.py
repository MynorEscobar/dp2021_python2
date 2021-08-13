#hacer referencia a un archivo en python
from ClaseEjemplo import ClaseEjemplo

#instanciar la clase o crear un objeto
ejemplo = ClaseEjemplo()

#llamar al metodo para asignar un dato al valor1
ejemplo.setValor1(float(input("ingrese un valor ")))
ejemplo.setValor2(float(input("ingrese otro valor")))

#llamando al metodo que retorna el contenido valor1
print (ejemplo.calcularSuma())
print (ejemplo.calcularMulti())
print (ejemplo.calcularPromedio())
print (ejemplo.verificarMayorMenor())
print (ejemplo.verificarMayorMenor2())
ejemplo.verificarMayorMenor3()


