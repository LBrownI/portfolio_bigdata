CREATE DATABASE Tienda_DW;
GO
USE Tienda_DW;

-- 1. Dimensión Producto
CREATE TABLE DimProducto (
    ProductoKey INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100),
    Categoria NVARCHAR(50),
    PrecioUnitario DECIMAL(10,2)
);

-- 2. Dimensión Tiempo (Vital en todo DW)
CREATE TABLE DimTiempo (
    TiempoKey INT PRIMARY KEY, -- Formato YYYYMMDD
    Fecha DATE,
    Anio INT,
    Mes NVARCHAR(20),
    Trimestre INT
);
