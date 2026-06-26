-- Pregunta A. ¿Cuánto dinero ganamos por categoría de producto en el primer trimestre?
SELECT 
    p.Categoria,
    SUM(h.TotalVenta) AS IngresosTotales,
    SUM(h.Cantidad) AS UnidadesVendidas
FROM HechoVentas h
JOIN DimProducto p ON h.ProductoKey = p.ProductoKey
JOIN DimTiempo t ON h.TiempoKey = t.TiempoKey
WHERE t.Trimestre = 1
GROUP BY p.Categoria;

-- Pregunta B. Ranking de Ventas por Categoría
SELECT 
    p.Categoria, 
    SUM(h.TotalVenta) AS GranTotal,
    COUNT(h.VentaID) AS NumeroDeTransacciones
FROM HechoVentas h
JOIN DimProducto p ON h.ProductoKey = p.ProductoKey
GROUP BY p.Categoria
ORDER BY GranTotal DESC;

-- Pregunta C. Ventas por Mes (Para ver tendencias)
SELECT 
    t.Anio,
    t.Mes, 
    SUM(h.TotalVenta) AS VentaMensual
FROM HechoVentas h
JOIN DimTiempo t ON h.TiempoKey = t.TiempoKey
GROUP BY t.Anio, t.Mes;

-- Pregunta D. Saber qué productos son los "estrellas" y cuáles no se están moviendo, sin mostrar IDs complicados, solo nombres.
SELECT 
    p.Nombre AS Producto,
    p.Categoria,
    SUM(h.Cantidad) AS UnidadesVendidas,
    SUM(h.TotalVenta) AS IngresosTotales,
    AVG(p.PrecioUnitario) AS PrecioPromedio
FROM HechoVentas h
JOIN DimProducto p ON h.ProductoKey = p.ProductoKey
GROUP BY p.Nombre, p.Categoria
ORDER BY UnidadesVendidas DESC;

-- Pregunta E. Ventas por periodo, es decir, las ventas por año, trimestre y mes.
SELECT 
    t.Anio,
    t.Trimestre,
    t.Mes,
    SUM(h.TotalVenta) AS TotalVendido,
    COUNT(h.VentaID) AS TotalTransacciones
FROM HechoVentas h
JOIN DimTiempo t ON h.TiempoKey = t.TiempoKey
GROUP BY t.Anio, t.Trimestre, t.Mes;
