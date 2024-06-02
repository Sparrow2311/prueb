class ConjuntoNumeros:
    valor = None
    def __init__(self):
        self.numeros = list(range(1, 101))
        self.extraido = None
    
    def extract(self, numero):
        print('self: {}'.format(self))
        print('numero: {}'.format(numero))
        if not isinstance(numero, int):
            raise ValueError("El número debe ser un entero.")
        if numero < 1 or numero > 100:
            raise ValueError("El número debe estar entre 1 y 100.")
        if numero not in self.numeros:
            raise ValueError("El número ya fue extraído o no está en el rango.")
        
        self.numeros.remove(numero)
        self.extraido = numero
    
    def calcular_numero_extraido(self):
        #print('Numero self: {}'.format(self.numeros))
        suma_esperada = 100 * (100 + 1) // 2
        #print('suma esperada: {}'.format(suma_esperada))
        suma_actual = sum(self.numeros)
        #print('suma actual: {}'.format(suma_actual))
        return suma_esperada - suma_actual

# Aplicación principal
if __name__ == "__main__":
    import sys
    valor = input('Ingrese valor entero  a eliminar: ')
    
    
    try:
        numero_a_extraer = int(valor)
    except ValueError:
        print("El argumento debe ser un número entero.")
        sys.exit(1)
    
    conjunto = ConjuntoNumeros()
    
    try:
        conjunto.extract(numero_a_extraer)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    numero_calculado = conjunto.calcular_numero_extraido()
    print(f"El número extraído fue: {numero_calculado}")