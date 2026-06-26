-- Tabla de Hechos 
CREATE TABLE Hecho_Ventas (
    VentaId INT PRIMARY KEY IDENTITY(1,1),
    producto_key INT REFERENCES Dim_producto(Producto_Key),
    tiempo_key INT REFERENCES Dim_tiempo(tiempo_key),
    cliente_key INT REFERENCES Dim_cliente(Cliente_key),
    cantidad INT,
    totalventa DECIMAL(18,2)
);
