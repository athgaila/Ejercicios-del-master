#1-. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados.

# Definimos la función contar_frecuencias
def contar_frecuencias(cadena):
    frecuencias = {}
    for letra in cadena:
        if letra.isalpha():  # Verifica si el carácter es una letra
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias

#Ejemplo
cadena = "castiga, exhausto, el poste tosco y recto, e insiste, infausto, que ha visto a los espectros"
print(contar_frecuencias(cadena))
{'c': 4,
 'a': 6,
 's': 11,
 't': 9,
 'i': 5,
 'g': 1,
 'e': 9,
 'x': 1,
 'h': 2,
 'u': 3,
 'o': 9,
 'l': 2,
 'p': 2,
 'y': 1,
 'r': 2,
 'n': 2,
 'f': 1,
 'q': 1,
 'v': 1}



#2-. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
# Creamos la función map incluyendo una lambda para duplicar la lista de números
nueva_lista = list(map(lambda x: x * 2, lista_numeros))
print(nueva_lista)

#Ejemplo
lista_numeros = [1, 2, 3, 4, 5]
print(nueva_lista)
[2, 4, 6, 8, 10]    



#3-. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
#La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

#definimos la función filtrar_palabras
def filtrar_palabras(lista_palabras, palabra_objetivo):
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]
#Ejemplo
lista_palabras = ["albania", "rusia", "francia", "españa", "italia"]
palabra_objetivo = "ia"
print(filtrar_palabras(lista_palabras, palabra_objetivo))
['albania', 'rusia', 'francia', 'italia']



#4-. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
#definimos la función diferencia_valores:
def diferencia_valores(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))
#Ejemplo
lista1 = [9, 8, 7, 6] 
lista2 = [1, 2, 3, 4]
print(diferencia_valores(lista1, lista2))
[8, 6, 4, 2]          



#5-. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
#La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
#Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

#definimos la función calcular_media_estado
def calcular_media_estado(lista_notas, nota_aprobado=5):
# Calculamos la media sumando todos los números y dividiendo entre la cantidad de elementos
    media = sum(lista_notas) / len(lista_notas)
# Determinamos el estado según la media y la nota de aprobado
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)          
#Ejemplo
lista_notas = [3.3, 6.7, 5, 2.8, 8]
print(calcular_media_estado(lista_notas))
(5.16, 'aprobado')



#6-.Escribe una función que calcule el factorial de un número de manera recursiva.
#def factorial(numero_factor):
def factorial(numero_factor):
    # Caso base: el factorial de 0 o 1 es 1
    if numero_factor == 0 or numero_factor == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return numero_factor * factorial(numero_factor - 1)
#Ejemplo
print(factorial(5))     
120



#7-. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def tuplas_a_strings(lista_tuplas):
    return list(map(str, lista_tuplas))
#Ejemplo
lista_tuplas = [(1, 2), (3, 4), (5, 6)]
print(tuplas_a_strings(lista_tuplas))
['(1, 2)', '(3, 4)', '(5, 6)']



#8-. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
#o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

def division_numeros_usuario():
    try:
        valor_usuario1 = int(input("Introduce un número entero distinto de 0: "))
        valor_usuario2 = int(input("Introduce otro número entero distinto de 0: "))

        if valor_usuario1 == 0 or valor_usuario2 == 0:
            print("Error: los números no pueden ser 0.")
            return

        resultado = valor_usuario1 / valor_usuario2
        print(f"El resultado de dividir {valor_usuario1} entre {valor_usuario2} es {resultado}")

    except ValueError:
        print("Error: debes introducir solo números enteros y estos deben ser diferentes que 0.")

print (division_numeros_usuario())  



#9-.Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
#La lista de mascotas a excluir es ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter() 

lista_mascotas_prohibidas = ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"]
def filtrar_mascotas(lista_mascotas):
    return list(filter(lambda mascota: mascota not in lista_mascotas_prohibidas, lista_mascotas))
#Ejemplo
Lista_mascotas = ["Perro", "Gato", "Tortuga", "Oso", "Hurón", "Loro", "Tigre"]
print(filtrar_mascotas(Lista_mascotas))
['Perro', 'Gato', 'Tortuga', 'Hurón', 'Loro']   



#10-. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente
class Lista_vacia(ZeroDivisionError):
    """Excepción personalizada para listas vacías"""
    pass
def avg(lista):
    try:
        sumatorio = sum(lista)
        divisor = len(lista)
        if(divisor == 0):
            raise Lista_vacia
        resultado = sumatorio / divisor
        return resultado
    except Lista_vacia:
        return print("Error: La lista está vacía. No se puede calcular el promedio.")
#Ejemplo
lista = []      
print(avg(lista))



#11-. Escribe un programa que pida al usuario que introduzca su edad. 
#Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120 años")
        print(f"Tu edad es {edad} años.")
    except ValueError as e:
        print(f"Error: {e}. Por favor, introduce un número válido.")

pedir_edad()



#12-. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitudes(palabras):
    palabras = palabras.split()
    return list(map(len, palabras))  
#Ejemplo
palabras = "Castiga, exhausto, el poste tosco y recto, e insiste, infausto, que ha visto a los espectros"
print(longitudes(palabras))
[8, 8, 2, 5, 5, 1, 5, 8, 3, 2, 5, 1, 3, 9]


#13-. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. 
#Las letras no pueden estar repetidas. Usa la función map()

def mayus_minus(conjunto_caracteres):
    return list(map(lambda c: (c.upper(), c.lower()), conjunto_caracteres))
#Ejemplo
conjunto_caracteres = {'r', 'e', 'l', 'o', 'j'}
print(mayus_minus(conjunto_caracteres))
[('R', 'r'), ('E', 'e'), ('L', 'l'), ('O', 'o'), ('J', 'j')]    



#14-. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
def palabras_con_letra(palabras, letra):
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), palabras))
#Ejemplo
lista_palabras = ["Perro", "Gato", "Pájaro", "Pez", "Gallina"]
print(palabras_con_letra(lista_palabras, 'P'))  
['Perro', 'Pájaro', 'Pez']



#15-. Crea una función lambda que sume 3 a cada número de una lista dada.
sumar_tres = lambda lista: [x + 3 for x in lista]
#Ejemplo
numeros = [7, 15, 2, 25, 9]
print(sumar_tres(numeros))  
[10, 18, 5, 28, 12]     



#16-. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
def palabras_mas_largas(texto, n):
    # Dividimos el texto en palabras (separadas por espacios)
    palabras = texto.split()
    
    # Usamos filter para quedarnos solo con las palabras más largas que n
    resultado = filter(lambda palabra: len(palabra) > n, palabras)
    
    # Convertimos el resultado (un objeto filter) en una lista
    return list(resultado) 
# Ejemplo
texto = "serán ceniza , mas tendrán sentido ; polvo serán , mas polvo enamorado"
n = 6 
print (palabras_mas_largas(texto, n))   
['tendrán', 'sentido', 'enamorado']



#17-. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. 
# Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()
def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)
#Ejemplo
digitos = [5, 7, 2]
print(lista_a_numero(digitos))  # Salida: 572



#18-. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
estudiantes = [
    {"nombre": "Cristina", "edad": 40, "calificacion": 83},
    {"nombre": "Mario", "edad": 41, "calificacion": 96},
    {"nombre": "Alberto", "edad": 34, "calificacion": 72},
    {"nombre": "Olga", "edad": 59, "calificacion": 63}
    ]
estudiantes_top = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))
# ejemplo
print("Estudiantes con calificación mayor o igual a 90:")
for estudiante in estudiantes_top:
    print(f"- {estudiante['nombre']} ---> ({estudiante['calificacion']})")
#Estudiantes con calificación mayor o igual a 90:
#Mario ---> (96)



#19-.Crea una función lambda que filtre los números impares de una lista dada.
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))
#Ejemplo
numeros = [1, 1, 2, 3, 5, 8, 13, 21]
print(filtrar_impares(numeros))  
[1, 1, 3, 5, 13, 21]



#20-. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
lista = [10, "Messi", 23, "Beckham", 7, "Raúl"]
solo_numeros = list(filter(lambda x: isinstance(x, int), lista))
print(solo_numeros)
[10, 23, 7]



#21-. Crea una función que calcule el cubo de un número dado mediante una función lambda
cubo_de_x = lambda numero: numero **3
#Ejemplo
numero = 5
print(cubo_de_x(numero))
125



#22-. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce() .
numeros = [5, 21, 6, 18]
producto_final = reduce (lambda x,y : x * y, numeros)
print (producto_final)
11340



#23-. Concatena una lista de palabras. Usa la función reduce() .
lista_palabras = ["polvo " "serán " ", " "mas " "polvo " "enamorado"]
concatenacion_palabras = reduce (lambda x, y: x + " " + y, lista_palabras)
print (concatenacion_palabras)
#polvo serán , mas polvo enamorado



#24-. Calcula la diferencia total en los valores de una lista. Usa la función reduce()
numeros = [23, 16]
resta_numeros = reduce(lambda x,y : x-y, numeros)
print (resta_numeros)
7



#25-. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(texto):
    cantidad_caracteres = len(texto)
    return cantidad_caracteres
frase = "serán ceniza, mas tendrán sentido"
print(contar_caracteres(frase))
33



#26-. Crea una función lambda que calcule el resto de la división entre dos números dados.
resto_division = lambda x, y: x % y
# Ejemplo
lista_numeros = [21, 5]
resultado = resto_division(lista_numeros[0], lista_numeros[1])
print(resultado)
1



#27-. Crea una función que calcule el promedio de una lista de números.
def calcular_promedio(lista_numeros):
    suma = sum(lista_numeros)     
    promedio = suma / len(lista_numeros)  
    return promedio
#Ejemplo
lista_numeros = [25, 10, 12, 32, 1, 8, 16]
resultado = calcular_promedio(lista_numeros)
print("El promedio es:", resultado)
#El promedio es: 14.857142857142858



#28-. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    vistos = set()  # Usamos un conjunto para almacenar los elementos vistos
    for num in lista:
        if num in vistos:
            return num  # Devolvemos el primer duplicado encontrado
        vistos.add(num)
    return None  # Si no hay duplicados, devolvemos None
#Ejemplo
lista = [2, 4, 3, 5, 7, 11, 13, 7, 3, 13]
print(primer_duplicado(lista))
7



#29-. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
def enmascarar(valor):
    valor_str = str(valor)
    num_enmascarar = max(len(valor_str) - 4, 0)
    
    enmascarado = '#' * num_enmascarar + valor_str[-4:]
    
    return enmascarado
#Ejemplo
print (enmascarar ("16061985"))
####1985



#30-. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    # Convertimos las palabras a minúsculas para ignorar mayúsculas/minúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    # Comprobamos si al ordenar sus letras son iguales
    return sorted(palabra1) == sorted(palabra2)

#Ejemplo
palabra1 = "Amor"
palabra2 = "Rosa"
print(son_anagramas(palabra1, palabra2))
False



#31-. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
#esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def buscar_nombre():
    try:
        # Solicitar lista de nombres al usuario
        nombres = input("Ingresa una lista de nombres separados por comas: ")
        lista_nombres = [nombre.strip() for nombre in nombres.split(",")]

        # Solicitar el nombre a buscar
        nombre_buscar = input("Ingresa el nombre que deseas buscar: ").strip()

        # Verificar si el nombre está en la lista
        if nombre_buscar in lista_nombres:
            print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
        else:
            raise ValueError(f"El nombre '{nombre_buscar}' no se encuentra en la lista.")
    
    except ValueError as e:
        print(e)




#32-. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
diccionario_empleados = {
    "Carmen Moreno": "Directora General",
    "Aurora Moreno": "Directora de RRHH",
    "Mario Noriega": "Director de Programación",
    "Alberto Cuadrado": "Director de Finanzas"
}
def buscar_puesto(nombre_completo, empleados):
    puesto = empleados.get(nombre_completo)
    if puesto:
        return puesto
    else:
        return "La persona no trabaja aquí."
#Ejemplo
print (buscar_puesto("Cristina Cuadrado", diccionario_empleados))  
#La persona no trabaja aquí.



#33-. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
suma_listas = lambda lista1, lista2: [x + y for x, y in zip(lista1, lista2)]    
#Ejemplo
lista1 = [1, 1, 2, 3]
lista2 = [5, 8, 13, 21]
print(suma_listas(lista1, lista2))  
[6, 9, 15, 24]



#34-. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
#Código a seguir:
#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#6. Implementar el método
#info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
#Caso de uso:
# 1. Crear un árbol.
#2. Hacer crecer el tronco del árbol una unidad.
#3. Añadir una nueva rama al árbol.
#4. Hacer crecer todas las ramas del árbol una unidad.
#5. Añadir dos nuevas ramas al árbol.
#6. Retirar la rama situada en la posición 2.
#7. Obtener información sobre el árbol.

class Arbol:
    def __init__(self):
        #Inicializa un árbol con un tronco de longitud 1 y una lista vacía de ramas.
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        #Aumenta la longitud del tronco en una unidad.
        self.tronco += 1

    def nueva_rama(self):
        #Agrega una nueva rama de longitud 1.
        self.ramas.append(1)

    def crecer_ramas(self):
        #Aumenta en una unidad la longitud de todas las ramas existentes.
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        #Elimina la rama en una posición específica (comenzando desde 1). Si la posición no existe, muestra un mensaje de error.
        if 1 <= posicion <= len(self.ramas):
            self.ramas.pop(posicion - 1)
        else:
            print(f"No existe una rama en la posición {posicion}.")

    def info_arbol(self):
        #Devuelve información sobre el árbol.
        info = {
            "Longitud del tronco": self.tronco,
            "Número de ramas": len(self.ramas),
            "Longitudes de las ramas": self.ramas
        }
        return info
if __name__ == "__main__":
    arbol = Arbol()              # 1. Crear un árbol
    arbol.crecer_tronco()        # 2. Hacer crecer el tronco una unidad
    arbol.nueva_rama()           # 3. Añadir una nueva rama
    arbol.crecer_ramas()         # 4. Hacer crecer todas las ramas una unidad
    arbol.nueva_rama()           # 5. Añadir dos nuevas ramas
    arbol.nueva_rama()
    arbol.quitar_rama(2)         # 6. Retirar la rama situada en la posición 2
    print(arbol.info_arbol())    # 7. Obtener información del árbol
{'Longitud del tronco': 2, 'Número de ramas': 2, 'Longitudes de las ramas': [2, 1]}



#36-. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
# Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
#Código a seguir:
#1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
#2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
#3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
#4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
#Caso de uso:
#1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente. 
#2. Agregar 20 unidades de saldo de "Bob".
#3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
#4. Retirar 50 unidades de saldo a "Alicia".
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad} unidades. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        if not self.cuenta_corriente or not otro_usuario.cuenta_corriente:
            raise ValueError("Ambos usuarios deben tener cuenta corriente para transferir dinero.")
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad
        print(f"{self.nombre} ha transferido {cantidad} unidades a {otro_usuario.nombre}.")
        print(f"Saldo actual de {self.nombre}: {self.saldo}")
        print(f"Saldo actual de {otro_usuario.nombre}: {otro_usuario.saldo}")

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad} unidades. Saldo actual: {self.saldo}")

    #Ejerrcicios:
if __name__ == "__main__":
    # 1. Crear usuarios
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    # 2. Agregar 20 unidades a Bob
    bob.agregar_dinero(20)
    #Bob ha agregado 20 unidades. Saldo actual: 70

    # 3. Transferir 80 unidades de Bob a Alicia
    bob.transferir_dinero(alicia, 80)
    ValueError: Bob no tiene suficiente saldo para transferir 80.

    # 4. Retirar 50 unidades de Alicia
    alicia.retirar_dinero(50)
    #Alicia ha retirado 50 unidades. Saldo actual: 50



#37-. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.
#Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
#Caso de uso: Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(frase):
    #Cuenta cuántas veces aparece cada palabra en la farse.
    palabras = texto.split()
    contador = {}
    for palabra in frase:
        palabra_lower = palabra.lower()
        contador[palabra_lower] = contador.get(palabra_lower, 0) + 1
    return contador
#Ejemplo:
frase = "es hielo abrasador, es fuego helado, es herida que duele y no se siente"
print(contar_palabras(frase))
{'es': 3, 'hielo': 1, 'abrasador,': 1, 'fuego': 1, 'helado,': 1, 'herida': 1, 'que': 1, 'duele': 1, 'y': 1, 'no': 1, 'se': 1, 'siente': 1}


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    #Reemplaza una palabra por otra en el texto.
    return texto.replace(palabra_original, palabra_nueva)
#Ejemplo:
texto = "es hielo abrasador, es fuego helado, es herida que duele y no se siente"
palabra_original = "es"
palabra_nueva = "parece"
print(reemplazar_palabras(texto, palabra_original, palabra_nueva))
# parece hielo abrasador, parece fuego helado, parece herida que duele y no se siente


def eliminar_palabra(texto, palabra_a_eliminar):
    #Elimina una palabra del texto.
    palabras = texto.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra != palabra_a_eliminar]
    return ' '.join(palabras_filtradas)
print (eliminar_palabra("es hielo abrasador, es fuego helado, es herida que duele y no se siente", "es"))
# hielo abrasador, fuego helado, herida que duele y no se siente


def procesar_texto(texto, opcion, *args):
    #Procesa un texto según la opción:
    # 'contar' -> cuenta las palabras
    # 'reemplazar' -> reemplaza una palabra por otra
    # 'eliminar' -> elimina una palabra del texto
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para 'reemplazar' se requieren dos argumentos: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Para 'eliminar' se requiere un argumento: palabra_a_eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa: 'contar', 'reemplazar' o 'eliminar'.")
    


#38-. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def momento_del_dia():
    hora = int(input("Introduce la hora (0-23): "))
    # Validamos que la hora esté en el rango correcto
    if hora < 0 or hora > 23:
        print("Hora no válida. Debe estar entre 0 y 23.")
    else:
        if 6 <= hora <= 12:
            print("Es por la mañana.")
        elif 12 < hora < 20:
            print("Es por la tarde.")
        else:
            print("Es de noche.")
momento_del_dia()



#39-.  Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
#Las reglas de calificación son:
# 0 - 69 insuficiente
# 70 - 79 bien
# 80 - 89 muy bien
# 90 - 100 excelente

def calificacion():
    calif = int(input("Escribe tu puntuación de 0 a 100 - no se aceptan decimales"))
    if calif < 0 or calif > 100:
        return "La puntuación está fuera del rango, ingresa una puntuación correcta"
    if calif >= 0 and calif <= 69:
        return "insuficiente"
    if calif >= 70 and calif <= 79:
        return "bien"
    if calif >= 80 and calif <= 89:
        return "muy bien"
    if calif >= 90 and calif <= 100:
        return "excelente"
calificacion()



#40-. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo")
#y datos (una tupla con los datos necesarios para calcular el área de la figura).
def calcular_area_triángulo
import math  # para usar pi en el cálculo del círculo

def calcular_area(figura, datos):
    figura = figura.lower()  # evitar problemas con mayúsculas/minúsculas

    if figura == "triangulo":
        base, altura = datos
        area = (base * altura) / 2

    elif figura == "rectangulo":
        base, altura = datos
        area = base * altura

    elif figura == "circulo":
        radio, = datos
        area = math.pi * (radio ** 2)

    else:
        raise ValueError("Figura no reconocida. Usa 'triangulo', 'rectangulo' o 'circulo'.")

    return area

#Ejemplo
print(calcular_area("triangulo", (5, 10)))  # Salida: 25.0



#41-. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el 
#monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor 
# a cero). Por ejemplo, descuento de 15€. 
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python

# Programa: Cálculo del precio final con descuento

# 1. Solicita el precio original del artículo
pvp = float(input("Ingresa el PVP del artículo (€): "))

# 2. Pregunta si el usuario tiene un cupón de descuento
tiene_cupon = input("¿Tienes un cupón de descuento? Indica Y para sí y N para No: ")

# 3. Si el usuario tiene cupón, solicita el valor y calcula el descuento
if tiene_cupon.upper() == "Y":
    descuento = float(input("Ingresa el valor del cupón de descuento (€): "))

    # 4. Verifica si el valor del cupón es válido
    if descuento > pvp:
        print("El valor del cupón no es válido (no puede ser mayor que el PVP).")
        precio_final = pvp
    else:
        precio_final = pvp - descuento
        print(f"Descuento aplicado: {descuento}€")

# Si el usuario no tiene cupón
elif tiene_cupon.upper() == "N":
    precio_final = pvp
    print("No se aplicó ningún descuento.")

# Si el usuario introduce otra cosa
else:
    print("Opción no válida. Se asumirá que no tienes cupón y se aplicará el precio original. Si esto es un error, por favor reinicia el programa.")
    precio_final = pvp

# 5. Muestra el precio final
print(f"El precio final de tu compra es: {precio_final:.2f}€")