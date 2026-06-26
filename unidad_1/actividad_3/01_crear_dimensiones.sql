CREATE DATABASE Tienda_DW;
GO
USE Tienda_DW;

-- 1. Dimensión Producto
CREATE TABLE Dim_producto (
    Producto_Key INT PRIMARY KEY IDENTITY(1,1),
    nombre NVARCHAR(100),
    categoria NVARCHAR(50),
    precio DECIMAL(10,2)
);

-- 2. Dimensión Tiempo (Vital en todo DW)
CREATE TABLE Dim_tiempo (
    tiempo_key INT PRIMARY KEY, -- Formato YYYYMMDD
    fecha DATE,
    anio INT,
    mes NVARCHAR(20),
    trimestre INT
);

-- 3. Dimensión Cliente 
CREATE TABLE Dim_cliente (
    Cliente_key INT PRIMARY KEY IDENTITY(1,1),
    nombrecompleto NVARCHAR(100),
    genero NVARCHAR(20),
    ciudad NVARCHAR(50),
    segmento NVARCHAR(20) -- por ejemplo: 'premium', 'regular', 'nuevo' 
);
