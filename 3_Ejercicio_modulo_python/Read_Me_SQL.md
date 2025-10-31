En general me parece que la herramienta Jupyter Notebook de Visual Studio ayuda mucho, ya que según iba escribiendo código tras incluir el enunciado me ha dado en más de una ocasión funciones completas correctas. Para poder pensar he tenido que borrar y, cuando he decidido dejar lo que me sugería el programa me he esforzado por entender el motivo de su uso.
He intentado seguir buenas prácticas y describir en lo que he visto necesario, además de hacer un código coherente en que la separación entre palabras venga con guión bajo (_). Por supuesto, no he usado palabras reservadas cuando no debía hacerlo.
Creía que los ejercicios iban a ser mucho más fáciles, me parecen de un nivel avanzado para lo visto.


1-. El propio Jupyter me ha sugerido la función .isalpha() para identificar solo las letras, por lo que la he usado y la he incorporado a mis conocimientos.

2-. Tenía la opción de usar o no una función lambda y he preferido hacerlo para optimizar el código.

3-. Uso un bucle for y un condicional, y en el ejemplo uso la terminación "ia" para que me busque los países de la lista que la contengan.

4-. He decidido incluir una función lambda en la función map.

5-. He decidido hacer mezclas entre integers y floats para calcular la suma de las notas

6-. Cuando me he puesto a meter el código he visto que había una forma más fácil de llegar al resultado (me la ha sugerido el programa), pero he decidido incluir la fórmula tal y como yo la he pensado. He tenido que recalcular, porque en un principio no había puesto que el range empezara en 1, por lo que, al empezar en 0, el resultado final era 0. Una vez he hecho la corrección, ya ha funcionado correctamente. 



7-. Como me piden pasar una lista de tuplas a strings me ha parecido rizar el rizo si lo que convierto a strings son integers, así que he aplicado la función map sobre ese tipo de números.



8-. Me ha llevado un tiempo cuadrar bien la función manejando las excepciones. Cuando se devuelve un resultado es porque la división ha sido exitosa. He querido acotar indicando que solo podían meterse integers para ser más restrictiva.



9-. No había visto hasta ahora el "not in" y me ha parecido muy útil, el propio Python me ha sugerido incluirlo en la función y he decidido aplicarlo.



10-. Incluyo la excepción que creo como clase. Me resulta complicado crear las excepciones dentro del código, saber dónde tienen que ir, pero con ayuda del programa lo consigo. Utilizo el raise para lanzar la excepción, lo incorporo a mis conocimientos.



11-. Trabajo con un VaueError para que me devuelva un mensajes en caso de que las edades estén fuera del rango o no sean integers.



12-. Usamos el método split para dividir la frase en palabras y poder hacer un len de cada palabra.



13-. Había opción de usar un set, pero de esta manera la función queda con el código más limpio.



14-. Primero uso el método lower para que todas las letras sean minúsculas y no haya posibles confusiones y luego el método que aprendo gracias al código de startswith´



15-. Uso la función lanbda, como se me pide, pero también una list comprehension con un bucle for que itere los elementos de la lista.



16-. Ese ha sido mi texto, pero para que funcionara sin unir la puntuación a las palabras he tenido que dejar un espacio entre ambos.



17-. Este ejercicio parecía muy sencillo, pero después de darle varias vueltas no sabía cómo hacerlo y me ha tenido que ayudar ChatGPT. Entiendo que se corre el código hacia la derecha una vez multiplicamos el primer dígito x 10 y sumamos el segundo. Esto se convierte en un acumulado y por lo tanto en un nuevo primer dígito de nuevo, y, cuando se suma el último dígito, deja ya de multiplicarse porque no quedan más.



18-. Esta no me ha resultado muy difícil una vez he gestionado la lambda.



19-. Era simple, es uno de los ejemplos que hemos tratado en las clases.



20-. Parecía sencillo, pero me lo ha simplificado más Python cuando me ha enseñado la función isinstance para saber si es de determinado tipo el elemento y solo dejar pasar los que dan como resultado True.



21-. He usado una lambda con un solo argumento.



22-. Uso una lambda con dos argumentos y la función reduce.



23-. No tengo mucho problema con la función reduce



24-. Crea una función que cuente el número de caracteres en una cadena de texto dada.



25-. Me ha resultado un poco compleja, quizás porque llevaba tiempo sin hacer el len.



26-. En este caso, chatGPT me ha tenido que ayudar, porque no había contemplado poner indexación al hacer el cálculo.



27-. Cálculo de promedio usando un len , una suma y una división entre sumatorio y len. No he puesto dos veces / porque no me interesaba redondear.



28-. He tenido que usar chatGPT porque no estoy acostumbrada a usar los set.



29-. Era difícil, y he tenido que pelearme con chatGPT porque me devolvía 5 caracteres sin ocultar, no 4. 



30-. Sabía que iba a tener que usar un sorted y un booleano, pero no cómo he tenido que pedir ayuda a chatGPT.



31-. Este ha sido muy complicado, incluso me daba error usando chatgpt, porque me aceptaba la lista de nombres, pero se bloqueaba cuando ponía uno, bien sea de la lista o de fuera de ella.



32-. Uso de diccionarios, no ha sido difícil. Lo que más me cuesta es pensar cuándo tengo que escribir toda una información, como en este caso.



33-. ES el único ejercicio en el que he tenido que hacer un zip y he tenido que pedir ayuda para vercómo formularlo, a priori pensaba que era más sencillo de lo que ha sido.



34-. Me ha gustado mucho hacer este ejercicio, crear los atributos y los métodos. ChatGPT me ha sugerido una opción para cuando no haya ramas a eliminar en una posición específica, que salga un error, y me ha parecido bien implementarlo en el código.



35-. No existe el ejercicio, pasa directamente al 36



36-.Ejercicio interesante, he tenido que reformular varias veces para que entendiera que todo era parte del mismo supuesto y me diera errores cuando era necesario y la cantidad correcta del saldo de Alicia.



37-. Las dos primeras casuísticas me han resultado fáciles, pero la de eliminar palabra ha sido difícil, he tenido que pedir ayuda a chatGPT, al igual que para procesar texto, había mucho que meter ahí, creo que tengo que aprender a hacerme esquemas cuando hay tanta información y tantas casuísticas.



38-. Este me ha gustado mucho hacerlo y me ha parecido que es muy práctico.



39-. Ejercicio divertido con una aplicación práctica, no he tenido dificultades.



40-. Aquí he tenido que recurrir a ChatGPT para importar maths y usarla para pi, además, no sabía cómo incluir las fórmulas para las figuras.



41-. Me ha encantado este ejercicio. He querido dar mi toque y poner que no se pueda hacer el descuento del cupón si el PVP es inferior a él, y que solo permita poner Y o N para meter el cupón, de lo contrario se asume que no hay cupón y se ofrece que, si lo hay, se reinicie el programa para aplicalrlo.



Autora: Cristina Cuadrado
