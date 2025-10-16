
-- 2-. Muestra los nombres de todas las películas con una clasificación por edades de‘Rʼ */
SELECT title
FROM film
WHERE rating = 'R'';

-- 3-. Encuentra los nombres de los actores que tengan un “actor_idˮ entre 30 y 40.*/
SELECT actor_id , concat(first_name, ' ', last_name)
FROM actor
WHERE actor_id BETWEEN 30 and 40;

-- 4-. Obtén las películas cuyo idioma coincide con el idioma original.*/
SELECT f.film_id,
       f.title,
       l.name AS language_name
FROM film f
JOIN language l
  ON f.language_id = l.language_id
WHERE f.language_id = f.original_language_id;
-- No puede averiguarse, porque el idioma original siempre es NULL, no se vuelcan resultados por las características de los datos.

-- 5-. Ordena las películas por duración de forma ascendente.
SELECT title , length 
FROM film
ORDER BY length ASC;

-- 6-. Encuentra el nombre y apellido de los actores que tengan ‘Allenʼ en su apellido.
SELECT first_name , last_name
FROM actor
WHERE last_name LIKE '%ALLEN%';

-- 7-. Encuentra la cantidad total de películas en cada clasificación de la tabla “filmˮ y muestra la clasificación junto con el recuento.
SELECT rating AS clasificación, COUNT(*) AS totalpelículas
FROM film
GROUP BY rating
ORDER BY totalpelículas DESC;

-- 8-. Encuentra el título de todas las películas que son ‘PG-13ʼ o tienen una duración mayor a 3 horas en la tabla film.
SELECT title, rating, length 
FROM film
WHERE rating = 'PG-13' OR length >180;

-- 9-. Encuentra la variabilidad de lo que costaría reemplazar las películas.
SELECT ROUND (VARIANCE (replacement_cost))
FROM film;

-- 10-. Encuentra la mayor y menor duración de una película de nuestra BBDD.
SELECT title, length
FROM film
WHERE length = (SELECT MIN(length) FROM film)
   OR length = (SELECT MAX(length) FROM film)
ORDER BY length DESC ;

-- 11-. Encuentra lo que costó el antepenúltimo alquiler ordenado por día.
SELECT amount, payment_date
FROM payment
ORDER BY payment_date ASC 
LIMIT 1 OFFSET 2;

-- 12-. Encuentra el título de las películas en la tabla “filmˮ que no sean ni ‘NC- 17ʼ ni ‘Gʼ en cuanto a su clasificación.
SELECT f.title, f.rating
FROM film f
WHERE rating NOT IN ('NC-17', 'G');

-- 13-. Encuentra el promedio de duración de las películas para cada clasificación de la tabla film y muestra la clasificación junto con el promedio de duración.
SELECT rating, AVG(length)
FROM film
GROUP BY rating;

-- 14-. Encuentra el título de todas las películas que tengan una duración mayor a 180 minutos.
SELECT title , length
FROM film
WHERE length > 180;

-- 15-. ¿Cuánto dinero ha generado en total la empresa?
SELECT SUM(amount) 
FROM payment;

-- 16-. Muestra los 10 clientes con mayor valor de id.
SELECT *
FROM customer
ORDER BY customer_id desc
LIMIT 10;

-- 17-. Encuentra el nombre y apellido de los actores que aparecen en la película con título ‘Egg Igbyʼ.
SELECT a.first_name, a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE f.title = 'EGG IGBY';
-- Es necesario poner el título en mayúsculas para que aparezca:

-- 18-. Selecciona todos los nombres de las películas únicos.
SELECT DISTINCT title 
FROM film;

-- 19-. Encuentra el título de las películas que son comedias y tienen una duración mayor a 180 minutos en la tabla “filmˮ.
SELECT f.title
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Comedy'
  AND f.length > 180;

-- 20-. Encuentra las categorías de películas que tienen un promedio de duración superior a 110 minutos y muestra el nombre de la categoría junto con el promedio de duración.
SELECT c.name AS category_name,
       AVG(f.length) AS avg_duration
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY c.name
HAVING AVG(f.length) > 110
ORDER BY avg_duration ASC;

-- 21-. ¿Cuál es la media de duración del alquiler de las películas?
SELECT AVG(f.rental_duration)
FROM film f ;

-- 22-. Crea una columna con el nombre y apellidos de todos los actores y actrices.
SELECT CONCAT(first_name , ' ', last_name )
FROM actor;

-- 23-. Números de alquiler por día, ordenados por cantidad de alquiler de forma descendente.
SELECT 
    DATE(rental_date) AS dia,
    COUNT(*) AS cantidad_alquileres
FROM 
    rental
GROUP BY 
    DATE(rental_date)
ORDER BY 
    cantidad_alquileres desc;

-- 24-. Encuentra las películas con una duración superior al promedio.
SELECT title, length
FROM film
WHERE length > (SELECT AVG(length) FROM film);

-- 25-. Averigua el número de alquileres registrados por mes.
SELECT 
    DATE_TRUNC('month', rental_date) AS mes,
    COUNT(*) AS numero_alquileres
FROM 
    rental
GROUP BY 
    DATE_TRUNC('month', rental_date)
ORDER BY 
    mes;

-- 26-. Encuentra el promedio, la desviación estándar y varianza del total pagado.
SELECT AVG(p.amount), STDDEV(p.amount ), VARIANCE(p.amount ) 
FROM payment p ;

-- 27-. ¿Qué películas se alquilan por encima del precio medio?
SELECT title, rental_rate
FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);

-- 28-. Muestra el id de los actores que hayan participado en más de 40 películas.
SELECT actor_id
FROM film_actor fa 
GROUP BY actor_id
HAVING COUNT(film_id) > 40;

-- 29-. Obtener todas las películas y, si están disponibles en el inventario, mostrar la cantidad disponible.
SELECT 
    f.film_id,
    f.title,
    COUNT(i.inventory_id) AS total_copias,
    COUNT(i.inventory_id) - COUNT(r.rental_id) AS disponibles
FROM film f
LEFT JOIN inventory i 
    ON f.film_id = i.film_id
LEFT JOIN rental r 
    ON i.inventory_id = r.inventory_id
    AND r.return_date IS NULL  -- solo cuenta las copias que están actualmente alquiladas
GROUP BY f.film_id, f.title
ORDER BY f.title;

-- 30-. Obtener los actores y el número de películas en las que ha actuado.
SELECT 
    a.first_name,
    a.last_name,
    COUNT(fa.film_id) AS numero_de_peliculas
FROM 
    actor a
JOIN 
    film_actor fa ON a.actor_id = fa.actor_id
GROUP BY 
    a.actor_id, a.first_name, a.last_name
ORDER BY 
    numero_de_peliculas DESC;

-- 31-. Obtener todas las películas y mostrar los actores que han actuado en ellas, incluso si algunas películas no tienen actores asociados.
SELECT 
    f.film_id,
    f.title AS pelicula,
    a.actor_id,
    CONCAT(a.first_name, ' ', a.last_name) AS actor
FROM 
    film f
LEFT JOIN 
    film_actor fa ON f.film_id = fa.film_id
LEFT JOIN 
    actor a ON fa.actor_id = a.actor_id
ORDER BY 
    f.film_id, a.actor_id;

-- 32-. Obtener todos los actores y mostrar las películas en las que han actuado, incluso si algunos actores no han actuado en ninguna película.
SELECT 
    a.actor_id,
    a.first_name,
    a.last_name,
    f.film_id,
    f.title AS film_title
FROM 
    actor a
LEFT JOIN 
    film_actor fa ON a.actor_id = fa.actor_id
LEFT JOIN 
    film f ON fa.film_id = f.film_id
ORDER BY 
    a.last_name,
    a.first_name,
    f.title;

-- 33-. Obtener todas las películas que tenemos y todos los registros de alquiler.
SELECT 
    f.film_id,
    f.title AS film_title,
    r.rental_id,
    r.rental_date,
    r.return_date,
    r.customer_id
FROM 
    film f
LEFT JOIN 
    inventory i ON f.film_id = i.film_id
LEFT JOIN 
    rental r ON i.inventory_id = r.inventory_id
ORDER BY 
    f.film_id, r.rental_date;

-- 34-. Encuentra los 5 clientes que más dinero se hayan gastado con nosotros.
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(p.amount) AS total_gastado
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_gastado DESC
LIMIT 5;

-- 35-. Selecciona todos los actores cuyo primer nombre es 'Johnny'.
SELECT first_name , last_name 
FROM actor
WHERE first_name = 'JOHNNY';
-- Hay que poner el nombre en mayúscula para que se pueda hacer la búsqueda.

-- 36-. Renombra la columna “first_nameˮ como Nombre y “last_nameˮ como Apellido.
SELECT first_name as "Nombre", last_name as "Apellido"
FROM actor;

-- 37-. Encuentra el ID del actor más bajo y más alto en la tabla actor.
SELECT MIN(actor_id) , MAX(actor_id)
FROM actor;

-- 38-. Cuenta cuántos actores hay en la tabla “actorˮ.
SELECT count(actor_id )
FROM actor;

-- 39-. Selecciona todos los actores y ordénalos por apellido en orden ascendente.
SELECT first_name , last_name
FROM actor
ORDER BY last_name ASC;

-- 40-. Selecciona las primeras 5 películas de la tabla “filmˮ.
SELECT *
FROM film
LIMIT 5;

-- 41-. Agrupa los actores por su nombre y cuenta cuántos actores tienen el mismo nombre. ¿Cuál es el nombre más repetido?
SELECT 
    first_name ,
    COUNT(*) AS cantidad
FROM 
    actor
GROUP BY 
    first_name 
ORDER BY 
    cantidad DESC;
-- Los nombres más repetidos son KENNETH, PENELOPE Y JULIA (4 veces cada uno).

-- 42-. Encuentra todos los alquileres y los nombres de los clientes que los realizaron.
SELECT 
    r.rental_date, 
    c.first_name, 
	c.last_name
FROM 
    rental r
JOIN 
    customer c
ON 
    r.customer_id = c.customer_id;

-- 43-. Muestra todos los clientes y sus alquileres si existen, incluyendo aquellos que no tienen alquileres.
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    r.rental_id,
    r.rental_date,
    r.return_date
FROM customer c
LEFT JOIN rental r 
    ON c.customer_id = r.customer_id
ORDER BY c.customer_id, r.rental_date;

-- 44-. Realiza un CROSS JOIN entre las tablas film y category. ¿Aporta valor esta consulta? ¿Por qué? Deja después de la consulta la contestación.
SELECT *
FROM film
CROSS JOIN category;
-- No aporta valor la consulta, porque simplemente repite en orden las categorías que hay y cuando acaba vuelve a empezar, emparejando con cada película, lo cual no tiene sentido.

-- 45-. Encuentra los actores que han participado en películas de la categoría 'Action'.
SELECT DISTINCT a.actor_id,
       a.first_name,
       a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Action'
ORDER BY a.last_name, a.first_name;

-- 46-. Encuentra todos los actores que no han participado en películas.
SELECT a.actor_id, a.first_name, a.last_name
FROM actor a
LEFT JOIN film_actor fa ON a.actor_id = fa.actor_id
WHERE fa.film_id IS NULL;
-- No refleja resultados, luego todos los actores han participado en películas.

-- 47-. Selecciona el nombre de los actores y la cantidad de películas en las que han participado.
SELECT 
    CONCAT(a.first_name, ' ', a.last_name) AS actor_name,
    COUNT(fa.film_id) AS total_peliculas
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
GROUP BY a.actor_id, a.first_name, a.last_name
ORDER BY total_peliculas DESC;

-- 48-. Crea una vista llamada “actor_num_peliculasˮ que muestre los nombres de los actores y el número de películas en las que han participado.
CREATE VIEW actor_numero_peliculas AS
SELECT 
    a.actor_id,
    a.first_name || ' ' || a.last_name AS nombre_actor,
    COUNT(fa.film_id) AS numero_peliculas
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
GROUP BY a.actor_id, a.first_name, a.last_name
ORDER BY numero_peliculas DESC;

-- 49-. Calcula el número total de alquileres realizados por cada cliente.
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(r.rental_id) AS total_alquileres
FROM 
    customer c
LEFT JOIN 
    rental r ON c.customer_id = r.customer_id
GROUP BY 
    c.customer_id, c.first_name, c.last_name
ORDER BY 
    total_alquileres DESC;

-- 50-. Calcula la duración total de las películas en la categoría 'Action'.
SELECT SUM(f.length) AS duracion_total
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Action';

-- 51-. Crea una tabla temporal llamada “cliente_rentas_temporalˮ para almacenar el total de alquileres por cliente.
CREATE TEMPORARY TABLE cliente_rentas_temporal AS
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(r.rental_id) AS total_rentas
FROM customer c
LEFT JOIN rental r 
    ON c.customer_id = r.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name;

-- 52-. Crea una tabla temporal llamada “peliculas_alquiladasˮ que almacene las películas que han sido alquiladas al menos 10 veces.
CREATE TEMPORARY TABLE peliculas_alquiladas AS
SELECT f.film_id,
       f.title,
       COUNT(r.rental_id) AS veces_alquilada
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r   ON i.inventory_id = r.inventory_id
GROUP BY f.film_id, f.title
HAVING COUNT(r.rental_id) >= 10;

-- 53-. Encuentra el título de las películas que han sido alquiladas por el cliente con el nombre ‘Tammy Sandersʼ y que aún no se han devuelto. Ordena los resultados alfabéticamente por título de película.
SELECT f.title
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'TAMMY'
  AND c.last_name = 'SANDERS'
  AND r.return_date IS NULL
ORDER BY f.title ASC;
-- Es necesario escribir TAMMY SANDERS, en mayúsculas, para que devuelva resultados.

-- 54-. Encuentra los nombres de los actores que han actuado en al menos una película que pertenece a la categoría ‘Sci-Fiʼ. Ordena los resultados alfabéticamente por apellido.
SELECT DISTINCT a.first_name, a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Sci-Fi'
ORDER BY a.last_name, a.first_name;

-- 55-. Encuentra el nombre y apellido de los actores que han actuado en películas que se alquilaron después de que la película ‘SPARTACUS CHEAPER” se alquilara por primera vez. Ordena los resultados alfabéticamente por apellido.
SELECT DISTINCT a.first_name, a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.rental_date > (
    SELECT MIN(r2.rental_date)
    FROM rental r2
    JOIN inventory i2 ON r2.inventory_id = i2.inventory_id
    JOIN film f2 ON i2.film_id = f2.film_id
    WHERE f2.title = 'SPARTACUS CHEAPER'
)
ORDER BY a.last_name, a.first_name;

-- 56-. Encuentra el nombre y apellido de los actores que no han actuado en ninguna película de la categoría ‘Musicʼ.
SELECT a.first_name, a.last_name
FROM actor a
WHERE a.actor_id NOT IN (
    SELECT fa.actor_id
    FROM film_actor fa
    JOIN film f ON fa.film_id = f.film_id
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Music'
)
ORDER BY a.last_name, a.first_name;

-- 57-. Encuentra el título de todas las películas que fueron alquiladas por más de 8 días.
SELECT title, rental_duration 
FROM film 
WHERE rental_duration > 8;
-- No muestra resultados, por lo que ninguna se alquiló por más de 8 días.

-- 58-. Encuentra el título de todas las películas que son de la misma categoría que ‘Animationʼ.
SELECT title
FROM film
WHERE film_id IN (
    SELECT fc.film_id
    FROM film_category fc
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Animation'
);

-- 59-. Encuentra los nombres de las películas que tienen la misma duración que la película con el título ‘Dancing Feverʼ. Ordena los resultados alfabéticamente por título de película.
SELECT title
FROM film
WHERE length = (
    SELECT length
    FROM film
    WHERE title = 'DANCING FEVER'
)
AND title <> 'DANCING FEVER'
ORDER BY title;

-- 60-. Encuentra los nombres de los clientes que han alquilado al menos 7 películas distintas. Ordena los resultados alfabéticamente por apellido.
SELECT c.first_name, c.last_name
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING COUNT(DISTINCT r.inventory_id) >= 7
ORDER BY c.last_name ASC;

-- 61-. Encuentra la cantidad total de películas alquiladas por categoría y muestra el nombre de la categoría junto con el recuento de alquileres.
SELECT 
    c.name AS categoria,
    COUNT(r.rental_id) AS total_alquileres
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY total_alquileres DESC;

-- 62-. Encuentra el número de películas por categoría estrenadas en 2006.
SELECT c.name AS categoria,
       COUNT(f.film_id) AS numero_peliculas
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
WHERE YEAR(f.release_year) = 2006
GROUP BY c.name
ORDER BY numero_peliculas DESC;

-- 63-. Obtén todas las combinaciones posibles de trabajadores con las tiendas que tenemos.
SELECT 
    s.staff_id,
    CONCAT(s.first_name, ' ', s.last_name) AS staff_name,
    st.store_id,
    st.manager_staff_id,
    st.address_id
FROM staff s
CROSS JOIN store st
ORDER BY s.staff_id, st.store_id;

-- 64-. Encuentra la cantidad total de películas alquiladas por cada cliente y muestra el ID del cliente, su nombre y apellido junto con la cantidad de películas alquiladas.
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(r.rental_id) AS total_rentals
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
GROUP BY 
    c.customer_id, 
    c.first_name, 
    c.last_name
ORDER BY total_rentals DESC;
