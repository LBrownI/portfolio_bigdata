-- 1. Dimensión de Películas
CREATE TABLE Dim_Pelicula (
    ID_Pelicula INT PRIMARY KEY,
    Titulo VARCHAR(100),
    Genero VARCHAR(50),
    Clasificacion VARCHAR(10) -- Ejemplo: PG-13, R
);

-- 2. Dimensión de Sucursales (Cines)
CREATE TABLE Dim_Sucursal (
    ID_Sucursal INT PRIMARY KEY,
    Nombre_Cine VARCHAR(100),
    Ciudad VARCHAR(50),
    Pais VARCHAR(50)
);

-- 3. Dimensión de Tiempo
CREATE TABLE Dim_Tiempo (
    ID_Tiempo INT PRIMARY KEY,
    Fecha DATE,
    Dia INT,
    Mes INT,
    Anio INT,
    Trimestre INT
);