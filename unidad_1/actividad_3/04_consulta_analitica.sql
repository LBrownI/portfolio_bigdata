-- Ranking de Ventas por Categoría de producto
SELECT 
    p.categoria, 
    SUM(h.totalventa) AS VentasTotales
FROM Hecho_Ventas h
JOIN Dim_producto p ON h.producto_key = p.Producto_Key
GROUP BY p.categoria
ORDER BY VentasTotales DESC;

-- Ventas por Mes (Para ver tendencias)
SELECT 
    t.anio,
    t.mes, 
    SUM(h.totalventa) AS VentasMensuales
FROM Hecho_Ventas h
JOIN Dim_tiempo t ON h.tiempo_key = t.tiempo_key
GROUP BY t.anio, t.mes;

-- Ventas por periodo, es decir, las ventas por año y mes.
SELECT 
    t.anio,
    t.mes, 
    SUM(h.totalventa) AS VentasPorPeriodo
FROM Hecho_Ventas h
JOIN Dim_tiempo t ON h.tiempo_key = t.tiempo_key
GROUP BY t.anio, t.mes;

-- Ranking de ventas totales por ciudad y género.
SELECT 
    c.ciudad,
    c.genero,
    SUM(h.totalventa) AS VentasTotales
FROM Hecho_Ventas h
JOIN Dim_cliente c ON h.cliente_key = c.Cliente_key
GROUP BY c.ciudad, c.genero
ORDER BY VentasTotales DESC;

-- Quien es mi mejor cliente
SELECT TOP 1
    c.nombrecompleto,
    SUM(h.totalventa) AS TotalComprado
FROM Hecho_Ventas h
JOIN Dim_cliente c ON h.cliente_key = c.Cliente_key
GROUP BY c.nombrecompleto
ORDER BY TotalComprado DESC;
