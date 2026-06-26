-- Cual es la especialidad mas costosa y con más días de estancia
SELECT TOP 1
    d.Especialidad,
    SUM(h.Costo_Tratamiento) AS CostoTotal,
    SUM(h.Dias_Estancia) AS TotalDiasEstancia
FROM Hechos_Hospitalizaciones h
JOIN Dim_Doctor d ON h.Doctor_Key = d.Doctor_Key
GROUP BY d.Especialidad
ORDER BY CostoTotal DESC, TotalDiasEstancia DESC;

-- Que se está atendiendo más, niños o adultos mayores
SELECT 
    CASE 
        WHEN p.Edad < 18 THEN 'Niños'
        WHEN p.Edad >= 60 THEN 'Adultos Mayores'
        ELSE 'Adultos'
    END AS GrupoEdad,
    COUNT(h.Hospitalizacion_ID) AS TotalAtenciones
FROM Hechos_Hospitalizaciones h
JOIN Dim_Paciente p ON h.Paciente_Key = p.Paciente_Key
WHERE p.Edad < 18 OR p.Edad >= 60
GROUP BY 
    CASE 
        WHEN p.Edad < 18 THEN 'Niños'
        WHEN p.Edad >= 60 THEN 'Adultos Mayores'
        ELSE 'Adultos'
    END
ORDER BY TotalAtenciones DESC;

-- Que doctor realiza más atenciones, mensualmente.
SELECT 
    d.Nombre AS Doctor,
    t.Mes,
    t.Anio,
    COUNT(h.Hospitalizacion_ID) AS TotalAtenciones
FROM Hechos_Hospitalizaciones h
JOIN Dim_Doctor d ON h.Doctor_Key = d.Doctor_Key
JOIN Dim_Tiempo t ON h.Tiempo_Key = t.Tiempo_Key
GROUP BY d.Nombre, t.Mes, t.Anio
ORDER BY TotalAtenciones DESC;

-- Que género es el más atendido por gravedad
SELECT 
    p.Genero,
    di.Gravedad,
    COUNT(h.Hospitalizacion_ID) AS TotalAtenciones
FROM Hechos_Hospitalizaciones h
JOIN Dim_Paciente p ON h.Paciente_Key = p.Paciente_Key
JOIN Dim_Diagnostico di ON h.Diagnostico_Key = di.Diagnostico_Key
WHERE di.Gravedad = 1
GROUP BY p.Genero, di.Gravedad
ORDER BY TotalAtenciones DESC;

-- Que enfermedad es la que mas se atiende los primeros 6 meses
SELECT TOP 1
    di.Descripcion AS Enfermedad,
    COUNT(h.Hospitalizacion_ID) AS TotalAtenciones
FROM Hechos_Hospitalizaciones h
JOIN Dim_Diagnostico di ON h.Diagnostico_Key = di.Diagnostico_Key
JOIN Dim_Tiempo t ON h.Tiempo_Key = t.Tiempo_Key
WHERE t.Mes IN ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio')
GROUP BY di.Descripcion
ORDER BY TotalAtenciones DESC;

-- Cuál es el costo total facturado por mes en el último año
SELECT 
    t.Mes,
    t.Anio,
    SUM(h.Costo_Tratamiento) AS CostoTotalMes
FROM Hechos_Hospitalizaciones h
JOIN Dim_Tiempo t ON h.Tiempo_Key = t.Tiempo_Key
WHERE t.Anio = 2025 -- Asumiendo 2025 como el último año basado en los datos insertados
GROUP BY t.Mes, t.Anio
ORDER BY CostoTotalMes DESC;

-- Cuál es el promedio de estancia (en días) por especialidad médica
SELECT 
    d.Especialidad,
    AVG(CAST(h.Dias_Estancia AS FLOAT)) AS PromedioEstancia
FROM Hechos_Hospitalizaciones h
JOIN Dim_Doctor d ON h.Doctor_Key = d.Doctor_Key
GROUP BY d.Especialidad
ORDER BY PromedioEstancia DESC;

-- Cuáles son los 5 diagnósticos más comunes en el hospital
SELECT TOP 5
    di.Descripcion AS Diagnostico,
    COUNT(h.Hospitalizacion_ID) AS Frecuencia
FROM Hechos_Hospitalizaciones h
JOIN Dim_Diagnostico di ON h.Diagnostico_Key = di.Diagnostico_Key
GROUP BY di.Descripcion
ORDER BY Frecuencia DESC;
