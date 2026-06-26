-- Insertamos datos en las dimensiones (Pelicula, Sucursal y Tiempo)
INSERT INTO Dim_Pelicula VALUES ( 1, 'The Batman', 'Accion', 'R' );

INSERT INTO
    Dim_Sucursal
VALUES (
        1,
        'Cinepolis Central',
        'Punta Arenas',
        'Chile'
    );

INSERT INTO Dim_Tiempo VALUES ( 1, '2025-05-15', 15, 5, 2025, 2 );

-- Se vendieron 2 entradas para Batman en ese cine y fecha
INSERT INTO Hechos_Ventas VALUES (1001, 1, 1, 1, 2, 7500.00);