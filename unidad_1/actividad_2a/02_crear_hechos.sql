-- 3. Tabla de Hechos 
CREATE TABLE HechoVentas (
    VentaID INT PRIMARY KEY IDENTITY(1,1),
    ProductoKey INT REFERENCES DimProducto(ProductoKey),
    TiempoKey INT REFERENCES DimTiempo(TiempoKey),
    Cantidad INT,
    TotalVenta DECIMAL(18,2)
);
