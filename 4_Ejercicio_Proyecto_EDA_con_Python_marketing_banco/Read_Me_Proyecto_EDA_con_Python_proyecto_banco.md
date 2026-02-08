Lo primero sería juntar en una sola hoja todos los datos, unidos por el ID. Para ello, vamos a usar Power Query. 
Elijo el archivo que incluye tres hojas (2012, 2013 y 2014). En cada hoja creo una columna llamada “Year”. 
Datos → Obtener datos → Desde archivo → Desde libro  → Marco las tres hojas  → Transformar datos 
Veo las tres consultas en Power Query  → selecciono la primera  → Inicio → Anexar consultas → Anexar consultas como una nueva → Selecciono “Tres o más tablas” → añado las tres hojas y acepto → obtengo una hoja con las filas de los tres años.
Para cargar el archivo bank_additional → Datos → Obtener datos → Desde archivo → Desde libro → selecciono el archivo → Transformar datos 
Selecciono la tabla en que se están las filas de todos los años → Inicio → Combinar consultas → elijo la tabla de bank_additional → Marco la columna ID en ambas → Tipo de unión: izquierda → aceptar
Pulso el icono de expandir → selecciono las columnas que quiero conservar del Excel de bank additional (todas menos el número de fila) y desmarco “Usar nombre de columna como prefijo” → Cerrar y cargar
Con esto he unificado en una única tabla los dos archivos unidos por ID, pero hay filas sin ID y con datos. Elimino esas filas, porque el ID es necesario para identificar al cliente, y me queda un total de 43.000.
Paso el filtro para saber si hay duplicados, veo que no los hay. 
Elimino la columna de Contact, ya que sabíamos (y comprobamos) que siempre es telefónico. 
Doy nombres más comprensibles a las columnas: sustituyo “Default” por “Payment Default”, “y” por “Service/producto contracted”, “poutcome” por “Previous marketing campaign outcome”, “pdays” por “Days from last call”, “previous” por “Previous contacts”, “campaign” por “Current campaign calls”, “Euribor3m” por “Euribir3months”. Renombro la columna “date” y la llamo “Interaction date” 
Hago una nueva consulta en Power Query para corregir las edades quitando el 0 final (en dividir columna – por número de caracteres – una vez, lo más a la derecha posible, con un dígito). Elimino la columna de los ceros que se ha creado adicionalmente. En Power query selecciono las columnas de “Payment default”, de “Loan” y de “Housing” y las transformo en texto, para luego sustituir los “10” por “YES” y los “0” por “NO” (con Reemplazar valores). Pongo en mayúsculas “yes” y “no” en la columna “Service”/producto” contracted”.
He tenido que investigar qué era la columna “Dt_Customer” (que he cambiado por Start date), porque con la explicación del documento de que “representa la fecha en que el cliente se convirtió en cliente de la empresa” solo entendía que era una fecha. He averiguado que está en formato de números de serie de Excel. En el documento selecciono la columna – formato de celdas – fecha y elijo que muestre el formato día – mes – año. No obstante, es una información que no me aporta mucho, así que la dejo al final. Por cierto, creo que hay un error y que la explicación está cruzada en el documento, a tenor de la información de cada celda: la columna “Dt_Customer” probablemente sea el día en que se ha producido la interacción y la columna Date probablemente sea la fecha en que el cliente se convirtió en cliente de la empresa. Así, a la columna “DT customer” la llamo “Contacted” y a la columna “Date” la llamo “Start date”. 
Reordeno las columnas para tener agrupados los datos por temas relacionados. Creo una columna llamada Latitude OK y otra llamada Lomgitude OK en que las formateo multiplicándolas por 1000 para que puedan leerse. El orden quedaría:
1-. Año de estudio
2-. Fecha de comienzo en el banco
3-. Datos personales: Edad, Trabajo, Nivel de Educación, Estado Civil, Ingresos, Niños en casa, Adolescentes en casa
4-. Datos personales económicos: Historial de impagos, Hipoteca, Préstamos
5-. Datos relacionados con la campaña: Número de visitas a la web en el mes, Si contrata o no un producto o servicio, Llamadas de la campaña actual, Duración de las llamadas, Días desde la última llamada, Contactos anteriores, Día de la interacción, Resultado de campañas anteriores
6-. Datos macroeconómicos: Ratio de varianza de empleo, IPC, Índice de Confianza del Consumidor, Euribor a 3 meses
7-. Número de empleados
8-. Coordenadas: Latitud y Longitud (primero las que no están formateadas y luego las que sí)
9-. ID

Voy a medir:
-	Perfil de clientes: Qué segmento compra más (basándome en edad, estado civil, educación, empleo e ingresos) para identificar al público objetivo
-	Análisis de la campaña de marketing: me basaré en el número de llamadas, los productos o servicios que se han contratado, si hay o no contratos previos y el resultado de campañas previas de marketing. El objetivo es averiguar la tasa de éxito por número de llamadas, si más llamadas reducen o aumenta la probabilidad de contratar y si el resultado interior influye.  
-	Análisis de riesgo: el objetivo es averiguar el riesgo de impago, centrándome en las columnas de Loan, Housing, Housing, Job y Payment default.
-	Análisis de comportamiento Web: la relación que hay entre las visitas a la web y la contratación, comparando las columnas NumWebVisitsMonth y Service/product contracted. La pregunta clave es: ¿más visitas implican más probabilidad de contratar?
Básicamente haré un estudio en el que intentaré predecir la contratación con las siguientes variables:
o	Demográficas: Age, Job, Education…
o	Económicas (impacto macroeconómico): Income, Housing, Loan…
o	Comportamiento: NumWebVisitsMonth, Previous contacts, Current Campaign calls…
o	Contexto macroeconómico: Cons.price.idx, Cons.conf.idx, Euribor3months…
No obstante, mientras avanzaba me hice preguntas concretas y aproveché el estudio para responderlas.



INFORME

1-. Objetivo del análisis
Identificar qué variables influyen en la contratación del servicio/producto, usando:
•	Exploración de datos
•	Limpieza
•	Codificación de variables
•	Correlaciones
•	Segmentación de clientes
La variable objetivo es:
Service/producto contracted
(YES = contratado / NO = no contratado)





2-. Descripción del dataset analizado
•	Filas: 43.000 clientes
•	Columnas: 30 variables
•	Tipos de variables:
o	Demográficas (edad, educación, trabajo)
o	Financieras (deuda, impago, préstamos)
o	Económicas (inflación, euribor, índices macro)
o	Estado de contratación
Distribución real de contratación
Estado	   Clientes	   %
NO	   38.156	   88,73%
YES	   4.844	   11,27%
Conclusión: la contratación es minoritaria, por lo que el análisis se centra en detectar nichos de alta conversión.

3-. Pasos ejecutados en el notebook
Paso 1 — Carga de datos
Se importa la hoja “Análisis” desde Excel usando Pandas.
Resultado:
- Dataset cargado correctamente
- Tamaño validado (43.000 registros)

Paso 2 — Exploración inicial
Se revisan:
•	Tipos de columnas
•	Valores únicos
•	Distribuciones
•	Estadísticos básicos

Paso 3 — Análisis de valores nulos
Se contabilizan los valores faltantes.
Columnas con mayor número de nulos
Variable	    Nulos
Euribor3months	    9.256
Payment default	    8.981
Age	    5.120
Education	    1.807
Housing	    1.026
Loan	    1.026

Paso 4 — Eliminación de duplicados
Resultado:
✔ 0 duplicados

Paso 5 — Preparación de variables
Se ejecutan las siguientes transformaciones:
•	Codificación de variables categóricas (get_dummies)
•	Conversión a variables numéricas
•	Preparación para correlaciones y segmentación







Vamos ahora a analizar los datos del dataset que hemos preparado en Python.
1-. Tamaño real del fenómeno: contratar es la excepción
De 43.000 clientes analizados:
Estado	   Clientes	   %
NO contratan	   38.156	   88,73%
SÍ contratan	   4.844	   11,27%
Solo 1 de cada 9 clientes termina contratando
El negocio depende críticamente de identificar quiénes son esos 11%
Lectura estratégica:
No es un producto masivo. Funciona mejor como producto de nicho para perfiles concretos.

2-. Calidad de los datos — Lo bueno y lo mejorable
Duplicados
•	0 filas duplicadas
Dataset limpio a nivel estructural
•	Valores nulos relevantes
Variable	   Nulos	   % sobre total
Euribor3months	   9.256	   ~21,5%
Payment default	   8.981	   ~20,9%
Age	   5.120	   ~11,9%
Education	   1.807	   ~4,2%
Dato curioso: 1 de cada 5 clientes no tiene información completa sobre riesgo financiero o euribor, lo que puede sesgar análisis crediticios.

3-. Edad — Existe una “edad óptima” para contratar
Tendencia observada en el notebook
•	Baja contratación en menores de 25
•	Pico de contratación entre 30 y 55 años
•	Descenso progresivo a partir de 60+
La contratación se concentra en la edad laboral madura, cuando hay ingresos estables + decisiones financieras activas.

4-. Empleo — El trabajo importa más que la edad
Los segmentos con mayor propensión a contratar:
Tipo de empleo	   Tendencia
Profesionales cualificados	   Alta contratación
Técnicos	   Alta
Empleados estables	   Alta
Trabajos precarios / temporales	   Baja
Desempleados	   Muy baja
La estabilidad laboral pesa más que la edad en la decisión de contratar.

5-. Impagos — El predictor negativo más potente
La variable Payment default aparece en el notebook como una de las más influyentes.
Resultado real:
•	Clientes sin historial de impago → mucho más propensos a contratar
•	Clientes con historial de impago → caída drástica de conversión
El riesgo crediticio no solo reduce la aprobación, también reduce el interés del cliente en contratar.

6-. Deuda y préstamos — Menos deuda = más contratación
Patrón detectado:
•	Clientes sin préstamos activos → mayor conversión
•	Clientes con préstamos e hipotecas → menor conversión

Interpretación:
El cliente que ya está endeudado evita asumir nuevos compromisos.

7-. Educación — A mayor educación, mayor contratación
Tendencia clara en tus celdas:
Nivel educativo	Propensión
Universitario	Alta
Formación profesional	Media
Educación básica	Baja
El producto parece atraer a clientes con mayor capacidad de comprensión financiera.

8-. Variables macroeconómicas — El contexto sí influye
El notebook relaciona contratación con:
•	Euribor
•	Índices de precios
•	Confianza económica
Patrón:
Cuando el contexto económico es más favorable, la contratación aumenta.
Los clientes contratan cuando sienten estabilidad en el entorno, no solo en su situación personal.

9-. Correlaciones — Qué variables empujan realmente la contratación
Las variables con mayor relación positiva incluyen:
Factores que AUMENTAN contratación
-	Historial limpio (sin impagos)
-	Estabilidad laboral
-	Edad 30–55
-	Mayor educación
-	Bajo endeudamiento
Factores que REDUCEN contratación
-	Impagos
-	Alta deuda
-	Inestabilidad laboral
-	Edades extremas
El producto se vende mejor a perfiles financieramente sanos.

10-. Segmentos reales detectados (con lectura de negocio)
Segmentos de ALTO potencial
Segmento	   Por qué funciona
Profesionales estables sin deuda	   Máxima conversión
Empleados con buen historial financiero	   Alta
Técnicos cualificados	   Alta

Segmentos de BAJO potencial
Segmento	   Motivo
Clientes con impagos	   Riesgo + baja conversión
Jóvenes con baja estabilidad	   Baja capacidad financiera
Altamente endeudados	   Evitan nuevos compromisos

Dato interesante:
El mejor segmento es pequeño, pero muy rentable.

Hallazgos curiosos del análisis
-	Contratan más quienes no están endeudados, aunque ganen menos
-	El empleo pesa más que el nivel de ingresos
-	El riesgo financiero reduce intención, no solo aprobación
-	La contratación es más psicológica (seguridad) que puramente económica
-	El dataset muestra que el producto es aspiracional para clase media estable

Aprovechamos y nos hacemos algunas preguntas para responderlas con los datos:
1-. ¿Hay edades que no deberían existir entre los que contratan?
Sí, aparecen edades sospechosamente bajas.
En el grupo de contratantes:
•	Hay registros con edad < 18
•	Son pocos, pero no deberían existir
Esto apunta a:
•	Error de captura
•	Edad mal codificada
•	Valores por defecto
•	Datos sintéticos mezclados
Hay un problema de calidad de datos en la variable edad, pero es mínimo (5 personas) y la influencia en los resultados es mínima.

2-. ¿Contratan personas con nivel educativo muy bajo o analfabetos?
Sí, y es llamativo.
Aunque la contratación es mayor en niveles educativos altos, aparece este patrón curioso:
•	Personas con educación muy baja / básica
•	Siguen apareciendo en el grupo YES
•	En proporción, no son tantas, pero más de las esperables
Interpretación posible
•	El producto no requiere alta alfabetización financiera
•	Puede haber contratación impulsiva o asistida (agente comercial)
•	O sesgo en cómo se reporta la educación
La educación ayuda, pero NO es una barrera real para contratar.


3-. ¿Los ingresos más altos contratan MENOS de lo esperado?
Sí, y esto es uno de los hallazgos más interesantes.
Patrón observado
•	Rentas medias-altas → buena contratación
•	Rentas muy altas → contratación menor de lo esperado
Interpretación
Los clientes con ingresos muy altos:
•	Ya tienen productos financieros más complejos
•	No ven atractivo este producto
•	Lo perciben como poco relevante o poco premium
El producto no es aspiracional para el segmento de ingresos muy altos.
Funciona mejor en clase media y media-alta.

4-. ¿Contratan personas con impagos o alto riesgo?
Sí, pero MUCHO MENOS que el resto.
Aunque la tasa es baja, existen clientes con historial de impago que contratan
Posibles explicaciones
•	Contratan pero luego pueden cancelar / incumplir
•	Intentan mejorar su situación financiera
•	Hay lagunas en los filtros de aprobación
Insight clave:
Este grupo existe, pero probablemente es de alto riesgo y bajo valor.

5-. ¿Contratan personas con muchas deudas?
Menos de lo esperado.
Patrón curioso
•	Personas sin préstamos activos → sobrerrepresentadas
•	Personas muy endeudadas → infrarrepresentadas
El cliente endeudado evita nuevos compromisos.
La contratación está ligada a sensación de “capacidad” más que necesidad.

6-. ¿Contratan perfiles que “no encajan” con el perfil ideal?
Sí, aparecen outliers interesantes:
Casos raros detectables
•	Personas muy jóvenes que contratan
•	Personas con educación muy baja que contratan
•	Personas con ingresos muy altos que no contratan
•	Personas con historial financiero débil que aun así contratan
El modelo de cliente ideal explica la mayoría, pero no a todos.
Hay decisiones emocionales, impulsivas o no racionales.

7-. ¿El empleo muestra algo contraintuitivo?
Sí, no siempre contratan más los que ganan más
•	Contratan más los que:
o	Se sienten estables
o	Aunque no sean los mejor pagados
La estabilidad pesa más que el nivel absoluto de ingresos.

8-. ¿Qué perfil no contrata aunque “debería”?
Anomalía interesante
Los perfiles con:
•	Ingresos muy altos
•	Alta educación
•	Perfil financiero sólido
contratan menos de lo esperado
Posible lectura:
Este producto no es atractivo para el segmento premium
Puede percibirse como básico o poco diferencial


Conclusión estratégica clara
La contratación no es masiva. Funciona mejor como producto selectivo para perfiles estables, solventes y en edad laboral madura.
El crecimiento no vendrá de vender más a todos, sino de:
Detectar mejor al cliente correcto
Reducir coste de captación en segmentos débiles
Personalizar la oferta para perfiles premium

Ahora vamos a analizar el target
TARGET IDEAL — Basado en los clientes que sí contratan
El target no es el más rico ni el más joven.
Es el cliente de clase media–media alta, estable, sin riesgo financiero y en edad laboral madura.

1-. Perfil demográfico óptimo
Edad más rentable: 30–55 años
•	Menor conversión <25
•	Menor conversión >60
•	Pico claro en edad laboral estable

2-. Situación laboral ideal
Contratan más:
•	Empleados estables
•	Técnicos
•	Profesionales cualificados
Contratan menos:
•	Desempleados
•	Trabajos precarios
•	Jubilados
Target laboral: empleo estable / profesional

3-. Perfil financiero que mejor contrata según el riesgo crediticio
Sin historial de impagos
Baja deuda activa
Alto riesgo financiero = baja conversión

4-. Nivel de ingresos (punto óptimo)
•	Ingresos medios–altos → mejor conversión
•	Ingresos muy altos → menor interés
Target ingresos: clase media–media alta 
El producto no es premium suficiente para rentas top.

5-. Nivel educativo que mejor responde
Contratan más:
•	Educación media y superior
Contratan menos:
•	Educación básica

6-. Vivienda y deuda
Mejor conversión en clientes:
Sin préstamos activos
Sin hipotecas pesadas
Con sensación de control financiero

7-. Contexto psicológico detectado
Aunque no sea una variable directa, los datos sugieren:
El target típico es alguien que:
•	Se siente seguro económicamente
•	No está en estrés financiero
•	No es ultra rico
•	Toma decisiones racionales, no impulsivas
Es decir, contrata quien siente que puede, no quien necesita.

TARGET CORE
Edad: 30–55
Ingresos: medios–altos
Trabajo: empleado estable / técnico / profesional
Educación: media o superior
Riesgo financiero: bajo
Deuda: baja o inexistente
Historial de impago: NO
Situación vital: estabilidad económica
Segmento social: clase media acomodada

ANTI-TARGET (a quiénes no priorizar)
Menores de 25
Muy endeudados
Historial de impagos
Inestables laboralmente
Rentas ultra altas (bajo interés)
Perfiles en estrés financiero

Una vez definido el target, teniendo en cuenta los resultados de los factores de la campaña ¿a quién deben llamar los agentes en el futuro y cómo?
2–3 llamadas máximo por lead
Porque
•	Los que convierten no necesitan muchas llamadas
•	Si no convierten en 2–3 impactos, normalmente:
o	No encajan con el perfil
o	No tienen intención real
o	El coste extra ya no compensa
La conversión ocurre rápido o no ocurre.
Insistir demasiado no crea intención en este tipo de cliente.

Según los datos que refleja nuestro estudio:
Llamada 1 — Detección + Posicionamiento
Objetivo:
✔ Confirmar que es el perfil correcto
✔ No vender todavía
✔ Generar confianza
Lo que funciona con nuestro target:
•	Tono tranquilo
•	Profesional
•	Nada agresivo
“Le llamo porque su perfil encaja con un grupo de clientes que están contratando este servicio…”
Los que contratan responden mejor a sentirse “seleccionados” que “presionados”.

Llamada 2— Propuesta clara + valor
Objetivo:
✔ Explicar el beneficio
✔ Resolver dudas
✔ Dar control al cliente
Los clientes que convierten:
•	Valoran seguridad
•	Valoran no sentirse forzados
•	Quieren sentir que deciden ellos
“Se lo explico y usted decide sin compromiso.”
Cuanto más control siente el cliente, más probable es que contrate.

Llamada 3 — Cierre suave o descarte
Objetivo:
✔ Cerrar si hay interés
✔ O abandonar si no lo hay
Si en 3 contactos el cliente estable no muestra intención es casi seguro que NO es convertible
Persistir más no cambia su decisión

Cómo deben ser las llamadas (según el perfil que sí convierte)
Lo que no funciona
•	Presión
•	Urgencia artificial
•	Insistencia agresiva
•	Scripts rígidos

Lo que sí funciona
•	Tono calmado
•	Profesional
•	Consultivo
•	Orientado a asesoría
•	Ritmo lento
•	Lenguaje claro
El cliente que contrata es racional, no impulsivo.
La venta debe parecer asesoría, no marketing.

Duración ideal de llamada 
3–5 minutos
•	<2 min → superficial
•	6–7 min → genera fatiga
Los clientes que contratan quieren eficiencia, no charlas largas.

Cuándo ABANDONAR un lead 
No convierten cuando:
-	Perfil no encaja (deuda, inestabilidad, impagos)
-	No muestra interés tras 2–3 contactos
-	Pide posponer repetidamente
-	Rechaza sin curiosidad


