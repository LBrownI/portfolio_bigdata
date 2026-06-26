-- Llenar Dimensión Paciente
INSERT INTO Dim_Paciente (Nombre, Edad, Genero, Ciudad, Tipo_Seguro)
VALUES 
('Carlos Mendoza', 10, 'Masculino', 'Madrid', 'Privado'),
('Lucía Ramos', 75, 'Femenino', 'Barcelona', 'Público'),
('Jorge Díaz', 45, 'Masculino', 'Valencia', 'Privado'),
('María Castro', 80, 'Femenino', 'Sevilla', 'Público'),
('Sofía Vargas', 8, 'Femenino', 'Bilbao', 'Privado');

-- Llenar Dimensión Doctor
INSERT INTO Dim_Doctor (Nombre, Especialidad)
VALUES 
('Dr. Roberto Fernández', 'Cardiología'),
('Dra. Laura González', 'Pediatría'),
('Dr. Miguel Herrero', 'Neurología'),
('Dra. Elena Ruiz', 'Traumatología'),
('Dr. Pablo Iglesias', 'Medicina General');

-- Llenar Dimensión Diagnostico
INSERT INTO Dim_Diagnostico (Codigo_Enfermedad, Descripcion, Gravedad)
VALUES 
('I21', 'Infarto agudo de miocardio', 1),
('J03', 'Amigdalitis aguda', 0),
('S06', 'Traumatismo intracraneal', 1),
('G40', 'Epilepsia', 1),
('J12', 'Neumonía viral', 1);

-- Llenar Dimensión Tiempo
INSERT INTO Dim_Tiempo (Tiempo_Key, Fecha, Mes, Anio)
VALUES 
(20250110, '2025-01-10', 'Enero', 2025),
(20250215, '2025-02-15', 'Febrero', 2025),
(20250320, '2025-03-20', 'Marzo', 2025),
(20250425, '2025-04-25', 'Abril', 2025),
(20250530, '2025-05-30', 'Mayo', 2025),
(20250615, '2025-06-15', 'Junio', 2025);

-- Llenar Hechos_Hospitalizaciones
INSERT INTO Hechos_Hospitalizaciones (Paciente_Key, Doctor_Key, Diagnostico_Key, Tiempo_Key, Dias_Estancia, Costo_Tratamiento)
VALUES 
(2, 1, 1, 20250110, 10, 15000.00), -- Adulto mayor, Cardiología
(1, 2, 2, 20250215, 3, 1200.00),  -- Niño, Pediatría
(3, 4, 3, 20250320, 15, 25000.00), -- Adulto, Traumatología
(4, 3, 4, 20250425, 7, 8500.00),   -- Adulto mayor, Neurología
(5, 2, 5, 20250530, 5, 3000.00),   -- Niño, Pediatría
(2, 1, 1, 20250615, 12, 18000.00), -- Adulto mayor, Cardiología
(1, 5, 2, 20250110, 2, 800.00),    -- Niño, Medicina General
(3, 1, 1, 20250215, 8, 11000.00),  -- Adulto, Cardiología
(4, 3, 4, 20250320, 6, 7500.00),   -- Adulto mayor, Neurología
(5, 5, 5, 20250425, 4, 2500.00);   -- Niño, Medicina General
