-- Llenar dimensiones:
INSERT INTO DimProducto (Nombre, Categoria, PrecioUnitario)
VALUES ('Laptop Pro', 'Computación', 1200.00),
       ('Smartphone X', 'Telefonía', 800.00),
       ('iPhone 15', 'Telefonía', 900.00),
       ('Samsung Galaxy S24', 'Telefonía', 850.00),
       ('MacBook Air M2', 'Computación', 1100.00),
       ('Dell XPS 13', 'Computación', 1000.00),
       ('Monitor LG 27"', 'Accesorios', 300.00),
       ('Teclado Mecánico RGB', 'Accesorios', 80.00);

INSERT INTO DimTiempo (TiempoKey, Fecha, Anio, Mes, Trimestre)
VALUES (20240313, '2024-03-13', 2024, 'Marzo', 1),
       (20260101, '2026-01-01', 2026, 'Enero', 1),
       (20260102, '2026-01-02', 2026, 'Enero', 1),
       (20260103, '2026-01-03', 2026, 'Enero', 1),
       (20260105, '2026-01-05', 2026, 'Enero', 1);

-- Llenar hechos:
INSERT INTO HechoVentas (ProductoKey, TiempoKey, Cantidad, TotalVenta)
VALUES 
(1, 20240313, 2, 2400.00), -- Vendimos 2 Laptops
(2, 20240313, 1, 800.00),  -- Vendimos 1 Smartphone
(3, 20260101, 1, 900.00),  -- Un iPhone el 1 de enero
(5, 20260101, 2, 2200.00), -- Dos MacBooks el 1 de enero
(7, 20260102, 5, 1500.00), -- Cinco monitores el 2 de enero
(4, 20260103, 1, 850.00),  -- Un Samsung el 3 de enero
(8, 20260105, 10, 800.00); -- Diez teclados el 5 de enero
