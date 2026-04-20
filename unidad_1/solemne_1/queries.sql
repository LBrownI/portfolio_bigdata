-- =======================================================================
-- 1. CREAR BASE DE DATOS Y TABLAS
-- =======================================================================
-- Dimensión Estudiante
CREATE TABLE Dim_Estudiante (
ID_Estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
Nombre VARCHAR(200),
Fecha_Nacimiento DATE,
Genero VARCHAR(50),
Sede VARCHAR(100),
Tipo_Ingreso VARCHAR(50), -- Nuevo, Transferencia, Reingreso
Jornada VARCHAR(50) -- Diurna, Vespertina
);
-- Dimensión Curso (Asignatura)
CREATE TABLE Dim_Curso (
ID_Curso INTEGER PRIMARY KEY AUTOINCREMENT,
Nombre_Materia VARCHAR(100),
Creditos INT,
Departamento VARCHAR(100),
Facultad VARCHAR(100)
);
-- Dimensión Programa Académico (Carrera)
CREATE TABLE Dim_Programa (
ID_Programa INTEGER PRIMARY KEY AUTOINCREMENT,
Nombre_Carrera VARCHAR(100),
Nivel VARCHAR(50), -- Pregrado, Postgrado
Duracion_Semestres INT
);
-- Dimensión Tiempo
CREATE TABLE Dim_Tiempo (
ID_Tiempo INTEGER PRIMARY KEY,
Fecha_Completa DATE,
Anio INT,
Semestre INT, -- 1 o 2
Trimestre INT -- 1, 2, 3 o 4
);
-- Tabla de Hechos: Inscripciones
CREATE TABLE Hechos_Inscripciones (
ID_Inscripcion INTEGER PRIMARY KEY AUTOINCREMENT,
ID_Estudiante INT,
ID_Curso INT,
ID_Programa INT,
ID_Tiempo INT,
Nota_Final DECIMAL(2,1), 
Asistencia_Porcentaje DECIMAL(5,2), 
Intentos_Curso INT, -- 1 (primera vez), 2 (reprobó antes)
-- Definición de las llaves foráneas
FOREIGN KEY (ID_Estudiante) REFERENCES Dim_Estudiante(ID_Estudiante),
FOREIGN KEY (ID_Curso) REFERENCES Dim_Curso(ID_Curso),
FOREIGN KEY (ID_Programa) REFERENCES Dim_Programa(ID_Programa),
FOREIGN KEY (ID_Tiempo) REFERENCES Dim_Tiempo(ID_Tiempo)
);
-- =======================================================================
-- 2. POBLAR TABLA DIMENSION PROGRAMA (Mínimo 10 registros)
-- =======================================================================
INSERT INTO Dim_Programa (ID_Programa, Nombre_Carrera, Nivel, Duracion_Semestres) VALUES 
(1, 'Ingeniería Civil Informática', 'Pregrado', 10),
(2, 'Ingeniería Civil Industrial', 'Pregrado', 10),
(3, 'Ingeniería Comercial', 'Pregrado', 10),
(4, 'Arquitectura', 'Pregrado', 10),
(5, 'Psicología', 'Pregrado', 10),
(6, 'Enfermería', 'Pregrado', 10),
(7, 'Derecho', 'Pregrado', 10),
(8, 'Medicina Veterinaria', 'Pregrado', 10),
(9, 'Kinesiología', 'Pregrado', 10),
(10, 'Magíster en Ciencias de la Computación', 'Postgrado', 4),
(11, 'Medicina', 'Pregrado', 14),
(12, 'Pedagogía en Inglés', 'Pregrado', 10);
-- =======================================================================
-- 3. POBLAR DIMENSIÓN TIEMPO (Mínimo 10 registros)
-- =======================================================================
INSERT INTO Dim_Tiempo (ID_Tiempo, Fecha_Completa, Anio, Semestre, Trimestre) VALUES 
(20201, '2020-03-01', 2020, 1, 1),
(20202, '2020-08-01', 2020, 2, 3),
(20211, '2021-03-01', 2021, 1, 1),
(20212, '2021-08-01', 2021, 2, 3),
(20221, '2022-03-01', 2022, 1, 1),
(20222, '2022-08-01', 2022, 2, 3),
(20231, '2023-03-01', 2023, 1, 1),
(20232, '2023-08-01', 2023, 2, 3),
(20241, '2024-03-01', 2024, 1, 1),
(20242, '2024-08-01', 2024, 2, 3),
(20251, '2025-03-01', 2025, 1, 1),
(20252, '2025-08-01', 2025, 2, 3),
(20261, '2026-03-01', 2026, 1, 1),
(20262, '2026-08-01', 2026, 2, 3);
-- =======================================================================
-- 4. POBLAR DIMENSIÓN CURSO (Mínimo 10 registros)
-- =======================================================================
INSERT INTO Dim_Curso (ID_Curso, Nombre_Materia, Creditos, Departamento, Facultad) VALUES 
(1, 'Introducción al Cálculo', 5, 'Ciencias Básicas', 'Ingeniería'),
(2, 'Introducción a la Informática', 4, 'Ciencias de la Computación', 'Ingeniería'),
(3, 'Cálculo Multivariable', 5, 'Ciencias Básicas', 'Ingeniería'),
(4, 'Programación Orientada a Objetos', 6, 'Ciencias de la Computación', 'Ingeniería'),
(5, 'Estructura de Datos y Algoritmos', 6, 'Ciencias de la Computación', 'Ingeniería'),
(6, 'Base de Datos', 5, 'Sistemas de Información', 'Ingeniería'),
(7, 'Redes de Computadores', 5, 'Infraestructura TI', 'Ingeniería'),
(8, 'Aplicaciones y Tecnologías de la Web', 6, 'Proyectos TI', 'Ingeniería'),
(9, 'Inteligencia Artificial', 6, 'Ciencias de la Computación', 'Ingeniería'),
(10, 'Gestión de Proyectos', 5, 'Sistemas de Información', 'Ingeniería'),
(11, 'Álgebra Lineal', 5, 'Ciencias Básicas', 'Ingenieria'),
(12, 'Ecuaciones Diferenciales', 5, 'Ciencias Básicas', 'Ingenieria'),
(13, 'Ingeniería de Software', 6, 'Proyectos TI', 'Ingenieria'),
(14, 'Sistemas Operativos', 5, 'Infraestructura TI', 'Ingenieria'),
(15, 'Anatomía Humana', 8, 'Ciencias Morfológicas', 'Medicina y Ciencia'),
(16, 'Fisiología Clínica', 7, 'Ciencias Biomédicas', 'Medicina y Ciencia'),
(17, 'Fonética y Fonología Inglesa', 5, 'Idiomas', 'Educación'),
(18, 'Didáctica del Inglés', 6, 'Educación', 'Educación'),
(19, 'Derecho Civil I', 6, 'Derecho Privado', 'Derecho'),
(20, 'Derecho Penal General', 6, 'Derecho Público', 'Derecho');
-- =======================================================================
-- 5. POBLAR DIMENSIÓN ESTUDIANTE (Mínimo 10 registros)
-- =======================================================================
INSERT INTO Dim_Estudiante (ID_Estudiante, Nombre, Fecha_Nacimiento, Genero, Sede, Tipo_Ingreso, Jornada) VALUES 
(1, 'Dante Quezada', '2001-05-14', 'Masculino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(2, 'Lucas Brown Ibieta', '2000-11-22', 'Masculino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(3, 'Karina Barrientos', '2001-01-30', 'Femenino', 'De la Patagonia', 'Transferencia', 'Diurna'),
(4, 'Alonso Cardenas', '2002-04-10', 'Masculino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(5, 'Javiera Sobarzo', '2002-08-15', 'Femenino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(6, 'Diego Alvarez', '2001-12-05', 'Masculino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(7, 'Catalina Mendoza', '2003-02-18', 'Femenino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(8, 'Fernando Oyarzun', '2003-07-25', 'Masculino', 'De la Patagonia', 'Reingreso', 'Vespertina'),
(9, 'Emilia Osorio', '2003-09-11', 'Femenino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(10, 'Martin Cerda', '2004-01-08', 'Masculino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(11, 'Ursula Marcich', '2004-06-20', 'Femenino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(12, 'Nicolas Lazaro', '2003-10-30', 'Masculino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(13, 'Alonso Henriquez', '2005-03-12', 'Masculino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(14, 'Camila Osorio', '2005-05-05', 'Femenino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(15, 'Antonia Fernandez', '2005-11-18', 'Femenino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(16, 'Ignacio Rehbein', '2000-10-14', 'Masculino', 'Concepción', 'Nuevo', 'Diurna'),
(17, 'Alan Silva', '2001-03-22', 'Masculino', 'Valdivia', 'Transferencia', 'Vespertina'),
(18, 'Angelo Vargas', '2002-05-11', 'Masculino', 'Bellavista', 'Nuevo', 'Diurna'),
(19, 'Bastian Contreras', '2002-09-05', 'Masculino', 'Concepción', 'Reingreso', 'Diurna'),
(20, 'Diego Vargas', '2001-11-20', 'Masculino', 'Valdivia', 'Nuevo', 'Diurna'),
(21, 'Maximiliano Bayer', '2003-01-15', 'Masculino', 'Bellavista', 'Nuevo', 'Diurna'),
(22, 'Tomas Barria', '2003-04-30', 'Masculino', 'Concepción', 'Nuevo', 'Vespertina'),
(23, 'Buni Fuentes', '2003-08-12', 'Femenino', 'Valdivia', 'Transferencia', 'Diurna'),
(24, 'Julian Saldivia', '2004-02-28', 'Masculino', 'Bellavista', 'Nuevo', 'Diurna'),
(25, 'Jose Boscan', '2004-07-16', 'Masculino', 'Concepción', 'Nuevo', 'Diurna'),
(26, 'Esteban Mustaki', '2003-12-05', 'Masculino', 'Valdivia', 'Nuevo', 'Diurna'),
(27, 'Bruno Rodriguez', '2005-01-20', 'Masculino', 'Bellavista', 'Nuevo', 'Diurna'),
(28, 'Cristobal Chavez', '2005-04-08', 'Masculino', 'Concepción', 'Nuevo', 'Diurna'),
(29, 'Hunter Uthmano', '2005-09-14', 'Masculino', 'Valdivia', 'Nuevo', 'Diurna'),
(30, 'Tomas Bojanic', '2005-10-02', 'Masculino', 'Bellavista', 'Reingreso', 'Vespertina'),
(31, 'Vincent Bustamante', '2001-08-14', 'Masculino', 'De la Patagonia', 'Nuevo', 'Diurna'),
(32, 'Claudio Diaz', '2000-05-22', 'Masculino', 'Concepción', 'Nuevo', 'Diurna'),
(33, 'Israel Gonzalez', '2002-11-03', 'Masculino', 'Valdivia', 'Transferencia', 'Diurna'),
(34, 'Julian Herrera', '2002-01-19', 'Masculino', 'Bellavista', 'Nuevo', 'Diurna'),
(35, 'Manuel Figueroa', '2003-06-08', 'Masculino', 'De la Patagonia', 'Nuevo', 'Vespertina'),
(36, 'Matias Moraga', '2002-12-15', 'Masculino', 'Concepción', 'Reingreso', 'Diurna'),
(37, 'Benjamin Ojeda', '2001-09-25', 'Masculino', 'Valdivia', 'Nuevo', 'Diurna'),
(38, 'Diego Schafer', '2003-03-10', 'Masculino', 'Bellavista', 'Nuevo', 'Diurna'),
(39, 'Ignacio Ovalle', '2002-07-30', 'Masculino', 'De la Patagonia', 'Transferencia', 'Vespertina');
-- =======================================================================
-- 6. POBLAR TABLA DE HECHOS (Inscripciones Cruzadas Lógicamente - Mínimo 15)
-- =======================================================================
INSERT INTO Hechos_Inscripciones (ID_Estudiante, ID_Curso, ID_Programa, ID_Tiempo, Nota_Final, Asistencia_Porcentaje, Intentos_Curso) VALUES 
(13, 1, 1, 20261, 5.5, 90.00, 1),
(13, 2, 1, 20261, 6.0, 95.50, 1),
(14, 1, 1, 20261, 6.2, 100.00, 1),

(14, 2, 1, 20261, 5.8, 88.00, 1),
(15, 1, 1, 20261, 3.8, 65.00, 1),
(10, 3, 1, 20251, 4.5, 80.00, 1),
(10, 4, 1, 20251, 5.5, 85.00, 1),
(11, 3, 1, 20251, 6.8, 98.00, 1),
(11, 4, 1, 20251, 6.5, 100.00, 1),
(12, 4, 1, 20251, 4.0, 75.00, 2),
(7, 5, 1, 20241, 5.2, 88.00, 1),
(7, 6, 1, 20241, 6.1, 92.00, 1),
(8, 5, 1, 20241, 4.8, 78.50, 1),
(9, 6, 1, 20241, 5.9, 90.00, 1),
(4, 7, 1, 20231, 6.0, 95.00, 1),
(4, 8, 1, 20231, 5.8, 92.00, 1),
(5, 7, 1, 20231, 6.5, 100.00, 1),
(6, 8, 1, 20231, 5.1, 85.00, 1),
(1, 9, 1, 20221, 6.7, 98.00, 1),
(1, 10, 1, 20221, 6.2, 95.00, 1), 
(2, 9, 1, 20221, 5.5, 88.00, 1),
(3, 10, 1, 20221, 6.8, 100.00, 1),
(1, 7, 1, 20221, 6.0, 92.00, 1),
(5, 6, 1, 20231, 6.3, 96.00, 1),
(27, 1, 1, 20261, 5.8, 95.00, 1),
(27, 11, 1, 20261, 6.1, 98.00, 1),
(28, 1, 1, 20261, 4.2, 75.50, 1),
(29, 11, 1, 20261, 5.5, 88.00, 1),
(30, 1, 1, 20261, 3.9, 60.00, 2), 
(24, 3, 1, 20251, 4.8, 82.00, 1),
(24, 12, 1, 20251, 5.0, 85.00, 1),
(25, 12, 1, 20251, 6.4, 95.00, 1),
(26, 3, 1, 20251, 5.2, 90.00, 1),
(21, 6, 1, 20241, 6.5, 100.00, 1),
(21, 13, 1, 20241, 6.0, 92.00, 1),
(22, 6, 1, 20241, 4.5, 78.00, 1),
(23, 13, 1, 20241, 5.9, 88.50, 1),
(18, 8, 1, 20231, 6.2, 94.00, 1),
(18, 14, 1, 20231, 5.8, 89.00, 1),
(19, 14, 1, 20231, 4.9, 80.00, 2),
(20, 8, 1, 20231, 6.0, 90.00, 1),
(20, 8, 1, 20231, 6.7, 98.00, 1),
(16, 9, 1, 20221, 6.8, 100.00, 1),
(16, 10, 1, 20221, 6.5, 95.00, 1),
(17, 9, 1, 20221, 5.4, 85.00, 1),
(17, 10, 1, 20221, 5.9, 90.00, 1),
(31, 15, 11, 20241, 5.8, 95.00, 1),
(31, 16, 11, 20241, 6.2, 98.00, 1),
(32, 15, 11, 20241, 4.5, 85.00, 2),
(33, 16, 11, 20241, 6.5, 100.00, 1),
(34, 17, 12, 20251, 6.0, 92.00, 1),
(34, 18, 12, 20251, 5.5, 88.00, 1),
(35, 17, 12, 20251, 4.9, 75.00, 1),
(36, 18, 12, 20251, 6.8, 100.00, 1),
(37, 19, 7, 20261, 5.2, 80.00, 1),
(37, 20, 7, 20261, 6.1, 90.00, 1),
(38, 19, 7, 20261, 4.0, 70.00, 2),
(39, 20, 7, 20261, 5.9, 85.00, 1);
-- =======================================================================
-- QUERY A: Total, de alumnos inscritos por Facultad en el año 2025
-- =======================================================================
SELECT 
C.Facultad, 
COUNT(DISTINCT H.ID_Estudiante) AS Total_Alumnos_2025
FROM Hechos_Inscripciones H
JOIN Dim_Curso C ON H.ID_Curso = C.ID_Curso
JOIN Dim_Tiempo T ON H.ID_Tiempo = T.ID_Tiempo
WHERE T.Anio = 2025
GROUP BY C.Facultad;
-- =======================================================================
-- QUERY B: Promedio de notas finales por Carrera.
-- =======================================================================
SELECT 
P.Nombre_Carrera, 
ROUND(AVG(H.Nota_Final), 2) AS Promedio_Notas
FROM Hechos_Inscripciones H
JOIN Dim_Programa P ON H.ID_Programa = P.ID_Programa
GROUP BY P.Nombre_Carrera
ORDER BY Promedio_Notas DESC;
-- =========================================================================================
-- QUERY C: Top 5 de asignaturas con mayor tasa de reprobación (Asumiendo nota_final < 4.0)
-- =========================================================================================

SELECT 
C.Nombre_Materia,
SUM(H.Nota_Final < 4.0) AS Alumnos_Reprobados,
COUNT(H.ID_Inscripcion) AS Total_Inscritos,
ROUND(AVG(H.Nota_Final < 4.0) * 100.0, 2) AS Tasa_Reprobacion
FROM Hechos_Inscripciones H
JOIN Dim_Curso C ON H.ID_Curso = C.ID_Curso
GROUP BY C.Nombre_Materia
ORDER BY Tasa_Reprobacion DESC
LIMIT 5;
-- =======================================================================
-- QUERY D: Cantidad de alumnos nuevos (primer ingreso) por semestre.
-- =======================================================================
SELECT 
T.Anio, 
T.Semestre, 
COUNT(DISTINCT H.ID_Estudiante) AS Cantidad_Alumnos_Nuevos
FROM Hechos_Inscripciones H
JOIN Dim_Estudiante E ON H.ID_Estudiante = E.ID_Estudiante
JOIN Dim_Tiempo T ON H.ID_Tiempo = T.ID_Tiempo
WHERE E.Tipo_Ingreso = 'Nuevo'
GROUP BY T.Anio, T.Semestre
ORDER BY T.Anio ASC, T.Semestre ASC;
-- =======================================================================
-- QUERY E: Distribución de alumnos por género y programa
-- =======================================================================
SELECT 
P.Nombre_Carrera, 
E.Genero, 
COUNT(DISTINCT H.ID_Estudiante) AS Cantidad_Alumnos
FROM Hechos_Inscripciones H
JOIN Dim_Programa P ON H.ID_Programa = P.ID_Programa
JOIN Dim_Estudiante E ON H.ID_Estudiante = E.ID_Estudiante
GROUP BY P.Nombre_Carrera, E.Genero
ORDER BY P.Nombre_Carrera, E.Genero;
-- ===========================================================================================
-- QUERY F: Comparativa de promedio de notas entre alumnos de jornada diurna vs. vespertina.
-- ===========================================================================================
SELECT 
E.Jornada, 
ROUND(AVG(H.Nota_Final), 2) AS Promedio_Notas
FROM Hechos_Inscripciones H
JOIN Dim_Estudiante E ON H.ID_Estudiante = E.ID_Estudiante
GROUP BY E.Jornada;
-- =======================================================================
-- QUERY G: PERSONA con mejor promedio de notas (Por curso/materia).
-- =======================================================================
SELECT 
C.Nombre_Materia, 
E.Nombre AS Mejor_Estudiante, 
MAX(H.Nota_Final) AS Nota_Final
FROM Hechos_Inscripciones H
JOIN Dim_Curso C ON H.ID_Curso = C.ID_Curso
JOIN Dim_Estudiante E ON H.ID_Estudiante = E.ID_Estudiante
GROUP BY C.ID_Curso;
-- ===========================================================================================
-- QUERY H: Lista de alumnos que pertenecen al "Cuadro de Honor" (nota final >6.5) por sede.
-- ===========================================================================================
SELECT 
E.Sede, 
E.Nombre AS Alumno, 
C.Nombre_Materia, 
H.Nota_Final
FROM Hechos_Inscripciones H
JOIN Dim_Estudiante E ON H.ID_Estudiante = E.ID_Estudiante
JOIN Dim_Curso C ON H.ID_Curso = C.ID_Curso
WHERE H.Nota_Final > 6.5
ORDER BY E.Sede ASC, H.Nota_Final DESC;
