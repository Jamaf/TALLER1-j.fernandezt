--cuántos animales en la guardería responden al nombre de Lassie
SELECT 
	*
FROM public."Perros" AS Perro
WHERE Perro."Nombre" = 'Lassie'

--Actualizamos el nombre del primer cuidador a Mario
UPDATE public."Cuidadores"
SET "Nombre" = 'Mario'
WHERE "ID" = 1;

--vemos la información de Mario
SELECT *
FROM public."Cuidadores" AS Cuidadores
WHERE "Nombre" = 'Mario';

--Ver los registros que queremos a actualizar
SELECT 
	*
FROM public."Perros" AS Perro
WHERE Perro."Peso" <= 3;

--Cree una instrucción en SQL que asigne al empleado Mario 
--todos los perros que pesen menos de 3 kilogramos
--Se hace como un Script que pueda servir a futuro
DO $$
DECLARE
	id_mario INTEGER;
BEGIN
	SELECT "ID"
	FROM public."Cuidadores" AS Cuidadores
	INTO id_mario
	WHERE "Nombre" = 'Mario';

	UPDATE public."Perros" AS Perro
	SET
		"ID_Cuidador" = id_mario
	WHERE Perro."Peso" <= 3;
	
	RAISE NOTICE 'El ID de Mario es %', id_mario;
END;
$$;

--Ver los registros despues del ajuste
SELECT 
	*
FROM public."Perros" AS Perro
WHERE Perro."Peso" <= 3;

--Actualizamos el nombre de la Guarderia a 'la favorita'
UPDATE public."Guarderias"
SET "Nombre" = 'La favorita';

--Se desea conocer toda la información de la guardería,
--así como de sus Perros y Cuidadores asociados
SELECT 
	Guarderias."Nombre" AS nombre_guarderia
	,Guarderias."Direccion" AS direccion_guarderia
	,Guarderias."Telefono" AS telefono_guarderia
	,Cuidadores."Nombre" AS nombre_cuidador
	,Cuidadores."Telefono" AS telefono_cuidador
	,Perros."Nombre" AS nombre_perro
	,Perros."Raza" AS raza_perro
	,Perros."Edad" AS edad_perro
	,Perros."Peso" AS peso_perro
	,Guarderias."ID" AS id_guarderia
	,Cuidadores."ID" AS id_cuidador
	,Perros."ID" AS id_perro
FROM public."Guarderias" AS Guarderias
INNER JOIN public."Cuidadores" AS Cuidadores
	ON Guarderias."ID" = Cuidadores."ID_Guarderia"
INNER JOIN public."Perros" AS Perros
	ON Guarderias."ID" = Perros."ID_Guarderia"
	AND Cuidadores."ID" = Perros."ID_Cuidador"
WHERE
	Guarderias."Nombre" = 'La favorita'




