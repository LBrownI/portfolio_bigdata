### Data preparada (interpolación de promedios)
             RUT       Nombre Apellido P. Sexo  Edad        Ciudad  Promedio
0   21.344.556-7      Martina       Lagos    F    18  Puerto Montt       6.5
1   20.988.123-k     Benjamín     Oyarzún    M    19        Osorno       5.8
2   22.112.443-4        Sofía    Cárdenas    F    17        Castro       6.2
3   21.554.332-1        Mateo      Vargas    M    18  Puerto Varas       4.5
4   20.776.554-9    Florencia       Muñoz    F    20         Ancud       5.9
5   21.221.998-0        Lucas     Paredes    M    18     Frutillar       6.8
6   22.443.112-5     Isabella  Barrientos    F    17       Quellón       5.4
7   20.332.887-6      Joaquín     Aguilar    M    21    Llanquihue       6.1
8   21.665.443-2     Agustina    Espinoza    F    18       Calbuco       4.9
9   21.332.776-k     Catalina       Rivas    F    18        Castro       6.1
10  22.554.110-3    Valentina       Ulloa    F    17       Chonchi       6.7
11  21.887.223-4       Matías       Gómez    M    18  Puerto Montt       5.5
12  20.443.998-1        Elena    Guerrero    F    20        Osorno       6.0
13  21.990.554-7        Tomás   Almonacid    M    18        Castro       4.2
14  22.221.334-0       Josefa  Villarroel    F    17  Puerto Varas       6.9
15  20.665.112-8        Diego        Jara    M    19         Ancud       5.7
16  21.443.887-5       Emilia    Gallardo    F    18     Frutillar       6.3
17  20.887.443-2  Maximiliano     Cárcamo    M    20       Quellón       5.1
18  22.332.110-k      Isidora     Bórquez    F    17    Llanquihue       6.6
19  21.112.665-4       Felipe   Arriagada    M    18       Calbuco       4.8
20  20.554.332-9    Antonella    Saldivia    F    19     Purranque       5.6
21  21.776.998-1       Samuel    Carrasco    M    18       Chonchi       6.4
22  22.665.221-7     Fernanda   Henríquez    F    17  Puerto Montt       5.3
23  20.221.554-3    Francisco    Orellana    M    21        Osorno       5.9
24  21.332.776-k     Catalina       Rivas    F    18        Castro       6.1
25  21.990.554-7        Tomás   Almonacid    M    18        Castro       4.2
26  22.112.887-4        Maite    Figueroa    F    17         Ancud       6.8
27  21.554.665-1     Benjamín       Leiva    M    18     Frutillar       5.0
28  20.776.332-9    Constanza        Mena    F    20       Quellón       5.2
29  21.221.443-0      Vicente        Pino    M    18    Llanquihue       5.4

### Alumnos mayores de 20 en Puerto Montt
Empty DataFrame
Columns: [RUT, Nombre, Apellido P., Sexo, Edad, Ciudad, Promedio]
Index: []

### Alumnas (Sexo Femenino)
             RUT     Nombre Apellido P. Sexo  Edad        Ciudad  Promedio
0   21.344.556-7    Martina       Lagos    F    18  Puerto Montt       6.5
2   22.112.443-4      Sofía    Cárdenas    F    17        Castro       6.2
4   20.776.554-9  Florencia       Muñoz    F    20         Ancud       5.9
6   22.443.112-5   Isabella  Barrientos    F    17       Quellón       5.4
8   21.665.443-2   Agustina    Espinoza    F    18       Calbuco       4.9
9   21.332.776-k   Catalina       Rivas    F    18        Castro       6.1
10  22.554.110-3  Valentina       Ulloa    F    17       Chonchi       6.7
12  20.443.998-1      Elena    Guerrero    F    20        Osorno       6.0
14  22.221.334-0     Josefa  Villarroel    F    17  Puerto Varas       6.9
16  21.443.887-5     Emilia    Gallardo    F    18     Frutillar       6.3
18  22.332.110-k    Isidora     Bórquez    F    17    Llanquihue       6.6
20  20.554.332-9  Antonella    Saldivia    F    19     Purranque       5.6
22  22.665.221-7   Fernanda   Henríquez    F    17  Puerto Montt       5.3
24  21.332.776-k   Catalina       Rivas    F    18        Castro       6.1
26  22.112.887-4      Maite    Figueroa    F    17         Ancud       6.8
28  20.776.332-9  Constanza        Mena    F    20       Quellón       5.2

Cantidad de alumnos en Quellón: 3

### Alumnas de nombre Catalina o Sara
             RUT    Nombre Apellido P. Sexo  Edad  Ciudad  Promedio
9   21.332.776-k  Catalina       Rivas    F    18  Castro       6.1
24  21.332.776-k  Catalina       Rivas    F    18  Castro       6.1

### Alumnos de ciudades que comienzan con 'P'
             RUT     Nombre Apellido P. Sexo  Edad        Ciudad  Promedio
0   21.344.556-7    Martina       Lagos    F    18  Puerto Montt       6.5
3   21.554.332-1      Mateo      Vargas    M    18  Puerto Varas       4.5
11  21.887.223-4     Matías       Gómez    M    18  Puerto Montt       5.5
14  22.221.334-0     Josefa  Villarroel    F    17  Puerto Varas       6.9
20  20.554.332-9  Antonella    Saldivia    F    19     Purranque       5.6
22  22.665.221-7   Fernanda   Henríquez    F    17  Puerto Montt       5.3

[SUCCESS] Datos guardados en alumnos_limpio.csv