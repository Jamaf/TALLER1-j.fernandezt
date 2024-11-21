CREATE TABLE public."Guarderias"
(
    "ID" integer NOT NULL,
    "Nombre" character varying(50) NOT NULL,
    "Direccion" character varying(200),
    "Telefono" character varying(50),
    PRIMARY KEY ("ID")
);

ALTER TABLE IF EXISTS public."Guarderias"
    OWNER to postgres;
	


CREATE TABLE public."Cuidadores"
(
    "ID" integer NOT NULL,
    "Nombre" character varying(50) NOT NULL,
    "Telefono" character varying(50),
    "ID_Guarderia" integer,
    PRIMARY KEY ("ID"),
    CONSTRAINT "FK_Cuidadores_Guarderias" FOREIGN KEY ("ID_Guarderia")
        REFERENCES public."Guarderias" ("ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE IF EXISTS public."Cuidadores"
    OWNER to postgres;
	
	
CREATE TABLE public."Perros"
(
    "ID" integer NOT NULL,
    "Nombre" character varying(50) NOT NULL,
    "Raza" character varying(50),
    "Edad" integer,
    "Peso" numeric(5, 2),
    "ID_Guarderia" integer NOT NULL,
    "ID_Cuidador" integer NOT NULL,
    PRIMARY KEY ("ID"),
    CONSTRAINT "FK_Perro_Guarderia" FOREIGN KEY ("ID_Guarderia")
        REFERENCES public."Guarderias" ("ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "FK_Perro_Cuidador" FOREIGN KEY ("ID_Cuidador")
        REFERENCES public."Cuidadores" ("ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE IF EXISTS public."Perros"
    OWNER to postgres;	