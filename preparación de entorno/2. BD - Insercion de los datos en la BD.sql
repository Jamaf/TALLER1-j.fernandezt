INSERT INTO public."Guarderias"("ID", "Nombre", "Direccion", "Telefono")VALUES (1,'Winterfell','Castle Ward in County Down','601 4567890')

INSERT INTO public."Cuidadores"("ID", "Nombre", "Telefono", "ID_Guarderia")VALUES (1,'Jon Snow','601 5678901',1);
INSERT INTO public."Cuidadores"("ID", "Nombre", "Telefono", "ID_Guarderia")VALUES (2,'Daenerys Targaryen','601 6789012',1);

INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (1,'Rufo','Labrador retriever',7,22,1,2);
INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (2,'Bingo','Pug',2,6,1,2);
INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (3,'Lazzie','Collie',5,27,1,2);
INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (4,'Zeus','Rottweiler',NULL,45.8,1,2);
INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (5,'Nala','Golden R.',NULL,8.5,1,2);
INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (6,'Atila','Alabai',NULL,58.9,1,2);
INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (7,'Dobby','Doberman',6,NULL,1,2);
INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (8,'Peter','Pit bull',7,NULL,1,2);
INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (9,'Ghost','Direwolf',NULL,NULL,1,1);
INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (10,'Summer','Direwolf',NULL,NULL,1,1);
INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (11,'Shaggydog','Direwolf',NULL,NULL,1,1);
INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (12,'Nymeria','Direwolf',NULL,NULL,1,1);
INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (13,'Lady','Direwolf',NULL,NULL,1,1);
INSERT INTO public."Perros"("ID", "Nombre", "Raza", "Edad", "Peso", "ID_Guarderia", "ID_Cuidador")VALUES (14,'Grey Wind','Direwolf',NULL,NULL,1,1);

INSERT INTO public."Roles"("ID", "Nombre") VALUES (1,'Cliente');
INSERT INTO public."Roles"("ID", "Nombre") VALUES (2,'Administrador');
INSERT INTO public."Roles"("ID", "Nombre") VALUES (3,'Empleado');
INSERT INTO public."Roles"("ID", "Nombre") VALUES (4,'Cualquiera');

INSERT INTO public."Usuarios"("ID", username, password, "ID_Rol") VALUES (1, 'pperez', '12345', 1);
INSERT INTO public."Usuarios"("ID", username, password, "ID_Rol") VALUES (2, 'cocho', '12345', 1);
INSERT INTO public."Usuarios"("ID", username, password, "ID_Rol") VALUES (3, 'jfernandez', '12345', 2);
