-- Insertar datos en Dim_producto (mínimo 5 registros)
INSERT INTO Dim_producto (nombre, categoria, precio)
VALUES 
('Laptop Pro', 'Computación', 1200.00),
('Smartphone X', 'Telefonía', 800.00),
('Monitor LG 27"', 'Accesorios', 300.00),
('Teclado Mecánico RGB', 'Accesorios', 80.00),
('Ratón Inalámbrico', 'Accesorios', 50.00);

-- Insertar datos en Dim_tiempo (mínimo 5 registros)
INSERT INTO Dim_tiempo (tiempo_key, fecha, anio, mes, trimestre)
VALUES 
(20240115, '2024-01-15', 2024, 'Enero', 1),
(20240220, '2024-02-20', 2024, 'Febrero', 1),
(20240310, '2024-03-10', 2024, 'Marzo', 1),
(20240405, '2024-04-05', 2024, 'Abril', 2),
(20240512, '2024-05-12', 2024, 'Mayo', 2);

-- Insertar datos en Dim_cliente (mínimo 5 registros)
INSERT INTO Dim_cliente (nombrecompleto, genero, ciudad, segmento)
VALUES 
('Juan Pérez', 'Masculino', 'Madrid', 'premium'),
('María Gómez', 'Femenino', 'Barcelona', 'regular'),
('Carlos Ruiz', 'Masculino', 'Valencia', 'nuevo'),
('Ana López', 'Femenino', 'Sevilla', 'premium'),
('Luis Fernández', 'Masculino', 'Bilbao', 'regular');

-- Insertar datos en Hecho_Ventas (mínimo 10 registros, cruzando dimensiones)
INSERT INTO Hecho_Ventas (producto_key, tiempo_key, cliente_key, cantidad, totalventa)
VALUES 
(1, 20240115, 1, 1, 1200.00),
(2, 20240115, 2, 2, 1600.00),
(3, 20240220, 3, 1, 300.00),
(4, 20240220, 4, 3, 240.00),
(5, 20240310, 5, 2, 100.00),
(1, 20240310, 1, 1, 1200.00),
(2, 20240405, 2, 1, 800.00),
(3, 20240405, 3, 2, 600.00),
(4, 20240512, 4, 1, 80.00),
(5, 20240512, 5, 5, 250.00);
