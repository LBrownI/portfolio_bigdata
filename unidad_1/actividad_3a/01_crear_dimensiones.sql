CREATE DATABASE Hospital_DWH;
GO
USE Hospital_DWH;

-- Dimensión Paciente
CREATE TABLE Dim_Paciente (
    Paciente_Key INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100),
    Edad INT,
    Genero NVARCHAR(20),
    Ciudad NVARCHAR(50),
    Tipo_Seguro NVARCHAR(50)
);

-- Dimensión Doctor
CREATE TABLE Dim_Doctor (
    Doctor_Key INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100),
    Especialidad NVARCHAR(50)
);

-- Dimensión Diagnostico
CREATE TABLE Dim_Diagnostico (
    Diagnostico_Key INT PRIMARY KEY IDENTITY(1,1),
    Codigo_Enfermedad NVARCHAR(20),
    Descripcion NVARCHAR(200),
    Gravedad BIT -- 1: si, 0: no
);

-- Dimensión Tiempo
CREATE TABLE Dim_Tiempo (
    Tiempo_Key INT PRIMARY KEY, -- Formato YYYYMMDD
    Fecha DATE,
    Mes NVARCHAR(20),
    Anio INT
);
