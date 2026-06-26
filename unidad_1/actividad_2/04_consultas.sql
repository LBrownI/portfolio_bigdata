SELECT P.Genero, S.Ciudad, SUM(V.Monto_Total) AS Ingresos_Totales
FROM
    Hechos_Ventas V
    JOIN Dim_Pelicula P ON V.FK_Pelicula = P.ID_Pelicula
    JOIN Dim_Sucursal S ON V.FK_Sucursal = S.ID_Sucursal
GROUP BY
    P.Genero,
    S.Ciudad;