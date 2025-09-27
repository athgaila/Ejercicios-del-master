En el ejercicio propuesto he conseguido una base de datos de las reservas ofrecidas en agosto por un proveedor de servicios turísticos de Santiago de Compostela. 
Para analizar el caso he seguido los siguientes pasos:

-	Análisis y comprensión de las columnas:
A: Número de reserva: es un identificador único, que corresponde a un cliente y a una actividad concreta.
B: Origen: si se ha reservado de manera orgánica (el cliente a través de la web), si se debe a Marketing, si se ha hecho a través de un Afiliado, de una Agencia de Viajes…
C: Reserva: Fecha exacta en que entró la reserva en el sistema, incluida hora.
D: Día de disfrute: día en que se ofrece el servicio.
E: Hora de disfrute: hora en que se ofrece el servicio.
F: Servicio contratado: nombre del servicio reservado.
G: PAX: Número de personas asistentes.
H: Precio: precio abonado por la reserva.
I: Cliente: nombre y apellido/s del cliente que ha usado para reservar.
J: Teléfono: número de teléfono de contacto del cliente que ha dejado al reservar.
K: Estado: indica si la reserva fue Opinada, se quedó sin recibir una opinión o si no se asistió a la actividad.

-	Limpieza y depuración:
Mi siguiente paso ha sido crear otra hoja y copiar la inicial. He decidido crear una columna en que se muestre solo la fecha de reserva, sin hora, formateando con la función =FECHA(AÑO(E2);MES(E2);DIA(E2)) para poder calcular luego la diferencia entre la fecha de reserva y la de realización. También he ocultado la columna de las horas de realización porque no la considero relevante, ya que solo me interesa saber los días de antelación. 
Creo columna para que tengan el mismo formato y se vean mejor la fecha de reserva y la fecha de realización, y oculto la fecha de realización con el formato inválido. Oculto la columna en que venían la fecha y hora en que entró la reserva también.
Creo una nueva columna para calcular la diferencia entre los días que hay entre la reserva y la realización y aplico la fórmula =F2-D2
Reviso si hay duplicados en la columna de teléfono y clientes, ya que es un identificador único, para eliminarlos. Veo con el formato condicional que se me iluminan varias celdas, así que voy a eliminarlos. 
Creo una hoja nueva llamada Cálculos, y uso la siguiente función para ver los resultados únicos de reserva que me proporciona (3054 en mi Hoja_ Origen): =CONTAR(Hoja_Origen!A:A). 
Sigo la ruta Datos – Quitar duplicados por Teléfono, ya que puede que haya algún cliente con el mismo nombre que otro. Se queda en 3028 filas. 
Una vez hecho esto, pienso que, una vez hemos quitado los duplicados, realmente las columnas de cliente y de teléfono no son útiles para el análisis, así que las oculto. Renombro las columnas de Pax por Número de Pax y la de Precio por Importe abonado.
Compruebo que no hay valores faltantes además. 
Me parece interesante ver si hay una diferencia importante entre las reservas por días de la semana y por días de realización, así que para verlo creo dos columnas con la función =TEXTO(D2;"dddd") y =TEXTO(F2;"dddd")

En un primer vistazo vemos que hay determinados servicios que se repiten mucho, al igual que la antelación, que suele ser muy baja, y el importe abonado, que suele ser 0 (es el importe que se paga por reservar un free tour). Por esta razón, me parece interesante averiguar qué antelación máxima hay, cuál es la máxima cuántas reservas a 0€ hay y qué precio máximo se ha abonado y a qué actividad pertenece. Además, es interesante saber cuánto se reserva cada tour y con qué antelación.
Por supuesto, también veremos las que se opinan, no se opinan y los No Shows, y el origen de las reservas.

La Tabla_Hoja_Depurada la convertí en tabla, por cierto.

Creo otra hoja para hacer unas cuentas para el dashboard y una de filtros, aunque es cierto que finalmente casi todas las hago en la hoja de Tablas_dinamicas_y_graficos, que también creo. En esta última creo tablas dinámicas, gráficos en varios formatos y miro información que me interesa ver a través de tablas. También creé los filtros que aplico en el dash.

Explicación del Dasboard y confirmación de hipótesis:
El Dashboard analiza las reservas que se han ofrecido en agosto de 2025 en Santiago de Compostela por un proveedor de servicios de turismo que ha tenido a bien facilitarme los datos. 
Está compuesto de 4 Big numbers:
-	Número de pax que han realizado la actividad: 8.365 pax
-	Número de reservas recibidas: 3.028 reservas
-	Antelación media de reservas: 21 días
-	Importe de las ventas: 46.281,6€

En cuanto a los gráficos, he incluido dos circulares:
1-. De los estados, en que se puede ver los que están opinados (30%), en Opinión solicitada (63%) y como No Show (no se presentaron en un free tour, un 7% del total de las reservas de servicios). En verdad supone el 9,2% de los free tours, como podemos ver en la pestaña Cuentas.
2-. El porcentaje de pax que se han reservado desde los diferentes medios. Destaca que no llega al 1% lo reservado a través de partnership y tienda, y que se queda en el 1% lo vendido por alojamientos y al 2% lo vendido por agencias de viajes. Con poco más (6%) se quedan Retención y Afiliados (8%). En la otra cara de la moneda, el marketing ha conseguido el 48% y el tráfico orgánico web el 35%. 

También he incluido uno de líneas para que se viera cómo se han ido recibiendo reservas a lo largo del mes. Sobresalen 2 datos: 126, a mediados de agosto, y 69 a finales.
He añadido  un gráfico de barras para ver las reservas que se reciben por actividad, que está unido a los dos filtros de la izquierda (estado de la reserva y origen de la reserva). 

Llama mucho la atención que lo que más se reserva con diferencia es el Free tour por Santiago, seguido de lejos por la Visita guiada por la catedral y por el Free tour de misterios y leyendas de Santiago. El resto de reservas son irrelevantes, no llegando ningún servicio a 60 ese mes. 

<img width="614" height="385" alt="image" src="https://github.com/user-attachments/assets/c17f64eb-02a7-4c86-aed4-cf05330d035c" />

Así, tras este análisis, llegamos a la conclusión de que hay que seguir invirtiendo en el Free tour por Santiago, la Visita guiada por la catedral y el Free tour de Misterios y leyendas. Sinceramente, eliminaría varios de los servicios que casi no se reservan, destinando más recursos a los que sí (por ejemplo, daría una oportunidad al Tour de Santiago de Compostela al Completo con entradas y a algo en italiano, porque es el idioma que más reservas tiene o más recauda tras el español). El free tour por Santiago parece que se vende solo y con mucha igualdad cualquier día de la semana, pero quitaría la disponibilidad del free tour de misterios y leyendas en los días en que menos se reserva (lunes y miércoles, porque no renta y así esas reservas se repartirían en el resto de los días.

<img width="886" height="274" alt="image" src="https://github.com/user-attachments/assets/bcf46d12-01d2-4760-a08b-c21baa6b84f6" />

Los 5 tours más reservados hacen el 99% de las reservas y el 98% de los pax (sin tener en cuenta los pax No Show (que no asistieron), porque no nos han pasado ese dato).

<img width="620" height="263" alt="image" src="https://github.com/user-attachments/assets/2b352986-9e7a-4d6d-83ce-60deff5c247a" />

Preocupa que haya casi dos tercios en estado No Opinado (63%), por lo que habría que incidir en pedir que se opinen las reservas.
Por otra parte, en cuanto al origen, gana por mucho el marketing (48%), que supone un coste, por lo que habría que potenciar las reservas orgánicas revisando la web creando palabras clave que hagan que los clientes a través de las búsquedas por internet lleguen de manera natural a la web para reservar.
Por último, quiero añadir que de las actividades de pago resalta sobre todo la visita guiada por la catedral. Los 5 tours más reservados hacen el 97% de la recaudación:

<img width="610" height="267" alt="image" src="https://github.com/user-attachments/assets/a00a4317-9fcd-4d9d-98a2-4177fcc7e11a" />


Autora: Cristina Cuadrado
