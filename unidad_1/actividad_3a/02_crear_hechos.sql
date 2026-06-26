-- Tabla de Hechos
CREATE TABLE Hechos_Hospitalizaciones (
    Hospitalizacion_ID INT PRIMARY KEY IDENTITY(1,1),
    Paciente_Key INT REFERENCES Dim_Paciente(Paciente_Key),
    Doctor_Key INT REFERENCES Dim_Doctor(Doctor_Key),
    Diagnostico_Key INT REFERENCES Dim_Diagnostico(Diagnostico_Key),
    Tiempo_Key INT REFERENCES Dim_Tiempo(Tiempo_Key),
    Dias_Estancia INT,
    Costo_Tratamiento DECIMAL(18,2)
);
