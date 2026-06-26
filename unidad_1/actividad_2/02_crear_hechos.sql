-- Habilitar el soporte de llaves foráneas en SQLite
PRAGMA foreign_keys = ON;

CREATE TABLE Hechos_Ventas (
    ID_Venta INT PRIMARY KEY,
    FK_Pelicula INT,
    FK_Sucursal INT,
    FK_Tiempo INT,
    Cantidad_Tickets INT,
    Monto_Total DECIMAL(10,2),

-- Definimos las relaciones con las dimensiones
FOREIGN KEY (FK_Pelicula) REFERENCES Dim_Pelicula(ID_Pelicula),
    FOREIGN KEY (FK_Sucursal) REFERENCES Dim_Sucursal(ID_Sucursal),
    FOREIGN KEY (FK_Tiempo) REFERENCES Dim_Tiempo(ID_Tiempo)
);