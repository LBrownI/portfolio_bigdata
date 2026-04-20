import questionary # pip install questionary
import sys
import datetime
import os

# Empezé primero a hacer la lógica para navegar el menu con numeros (1,2,3,0), pero después decidí usar "questionary" para tener un
# menu CLI en lo posible más fluido que como lo estaba haciendo... De esta forma el usuario sólo trndrá que usar las flechas y la tecla 
# ENTER para navegar. Adicionalmente, intenté colocar emojis para que se vea "bonito" pero me dejó mal la lógica, tuve que colocar 
# "in option" en lugar de "option ==", me arrepiento, pero no lo voy a cambiar.

# ⚠️ El programa no contempla borrar/eliminar un jugador del equipo porque no se pidió.

# diccionario de diccionarios
jugadores = {} 

# lista de diccionarios
partidos = [] 

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_instrucciones():
    limpiar_pantalla()
    print("🏀 SISTEMA DE GESTIÓN BASKET USS 🏀")
    print("===================================")
    print("Instrucciones de navegación:")
    print("  • Usa las FLECHAS (↑ ↓) para moverte por los menús.")
    print("  • Presiona ENTER para seleccionar una opción.")
    print("  • En las listas de jugadores, usa ESPACIO para marcar.")
    print("======================================================\n")
    input("Presiona ENTER para comenzar...")

def menu_principal():
    while True:
        limpiar_pantalla()
        opcion = questionary.select(
            "MENU INICIAL",
            choices=[
                "1. 📓​ REGISTRO DE EQUIPO",
                "2. 📝​ REGISTRO DE PARTIDO",
                "0. 🔚​ SALIR"
            ]
        ).ask()

        if "REGISTRO DE EQUIPO" in opcion:
            menu_equipo()
        elif "REGISTRO DE PARTIDO" in opcion:
            menu_partidos()
        elif "SALIR" in opcion:
            print("\nSaliendo del programa....")
            sys.exit(0)

def menu_equipo():
    while True:
        limpiar_pantalla()
        opcion = questionary.select(
            "MENU DE EQUIPO",
            choices=[
                "1. ⛹️​ AÑADIR NUEVO JUGADOR",
                "2. 📋​ VER LISTADO DE JUGADORES",
                "3. 🔎​ BUSCAR DATOS DE JUGADOR",
                "0. ↩️​ VOLVER ATRÁS"
            ]
        ).ask()

        if "AÑADIR NUEVO JUGADOR" in opcion:
            while True:
                nro = questionary.text("Ingrese el número de camiseta (único):").ask()
                
                if not nro.isdigit():
                    print("\n❌ El número debe ser un valor entero. Inténtalo de nuevo.\n")
                    continue
                    
                nro = int(nro)
                if nro in jugadores:
                    print("\n❌ Ese número de camiseta ya está registrado. Inténtalo de nuevo.\n")
                    continue
                
                nombre = questionary.text("Ingrese el nombre completo:").ask().title()
                posicion = questionary.select(
                    "Seleccione la posición:",
                    choices=["base", "alero", "escolta", "ala-pivot", "pivot"]
                ).ask()
                
                jugadores[nro] = {"nombre": nombre, "posicion": posicion}
                print(f"\n✅ Jugador {nombre} añadido.\n")
                input("Presiona ENTER para continuar...")
                break

        elif "VER LISTADO" in opcion:
            limpiar_pantalla()
            print("--- PLANTILLA DEL EQUIPO ---")
            if not jugadores:
                print("No hay jugadores registrados.")
            else:
                for nro, datos in jugadores.items():
                    print(f"#{nro} | {datos['nombre']} | {datos['posicion'].capitalize()}")
            input("\nPresiona ENTER para volver...")

        elif "BUSCAR DATOS" in opcion:
            limpiar_pantalla()
            nro_buscar = questionary.text("Ingrese el número de camiseta a buscar:").ask()
            if nro_buscar.isdigit() and int(nro_buscar) in jugadores:
                datos = jugadores[int(nro_buscar)]
                print(f"\n✅ JUGADOR ENCONTRADO:\nNombre: {datos['nombre']}\nPosición: {datos['posicion'].capitalize()}\n")
            else:
                print("\n❌ Jugador no encontrado.\n")
            input("Presiona ENTER para volver...")

        elif "VOLVER ATRÁS" in opcion:
            break

def menu_partidos():
    while True:
        limpiar_pantalla()
        opcion = questionary.select(
            "MENU DE PARTIDOS",
            choices=[
                "1. 🏀​ REGISTRAR NUEVO PARTIDO",
                "2. 🔎 BUSCAR PARTIDO POR RIVAL",
                "3. 📖​ VER HISTORIAL DE PARTIDOS",
                "0. ↩️ VOLVER ATRÁS"
            ]
        ).ask()

        if "REGISTRAR NUEVO PARTIDO" in opcion:
            registrar_partido()
            
        elif "BUSCAR PARTIDO" in opcion:
            limpiar_pantalla()
            if not partidos:
                print("No hay partidos registrados aún.")
            else:
                rival_buscado = questionary.text("Ingrese el nombre del equipo rival:").ask().title()
                fecha_buscada = questionary.text("Ingrese la fecha del partido (ej. DD-MM-YYYY):").ask()
                
                encontrados = [p for p in partidos if p['rival'] == rival_buscado and p['fecha'] == fecha_buscada]
                
                if encontrados:
                    print(f"\n--- PARTIDOS CONTRA {rival_buscado} EL {fecha_buscada} ---")
                    opciones_partidos = []
                    for i, p in enumerate(encontrados):
                        resultado = f"Resultado: {p['puntos_favor']} - {p['puntos_contra']}"
                        opciones_partidos.append(f"{i+1}. {resultado}")
                    
                    opciones_partidos.append("0. ↩️ Volver atrás")
                    
                    seleccion = questionary.select(
                        "Selecciona un partido para ver el detalle de los jugadores:",
                        choices=opciones_partidos
                    ).ask()
                    
                    if not seleccion.startswith("0"):
                        idx = int(seleccion.split(".")[0]) - 1
                        partido_elegido = encontrados[idx]
                        
                        limpiar_pantalla()
                        print(f"=== DETALLE VS {partido_elegido['rival']} ({partido_elegido['fecha']}) ===")
                        print(f"MARCADOR: {partido_elegido['puntos_favor']} - {partido_elegido['puntos_contra']}\n")
                        
                        for i, stats in enumerate(partido_elegido['estadisticas_jugadores']):
                            rol = "TITULAR" if i < 5 else "RESERVA"
                            nombre = jugadores[stats['nro']]['nombre']
                            pts = (stats['dobles'] * 2) + (stats['triples'] * 3)
                            print(f"#{stats['nro']} {nombre} ({rol}) | Pts: {pts} | Dob: {stats['dobles']} | Tri: {stats['triples']} | Faltas: {stats['faltas']}")
                else:
                    print(f"\n❌ No se encontraron partidos contra {rival_buscado} en la fecha {fecha_buscada}.")
            
            input("\nPresiona ENTER para volver...")

        elif "VER HISTORIAL" in opcion:
            limpiar_pantalla()
            if not partidos:
                print("\nNo hay partidos registrados.")
            else:
                print("--- HISTORIAL DE PARTIDOS ---")
                for i, p in enumerate(partidos):
                    print(f"{i+1}. {p['fecha']} | vs {p['rival']} | {p['puntos_favor']} - {p['puntos_contra']}")
            
            input("\nPresiona ENTER para volver...")

        elif "VOLVER ATRÁS" in opcion:
            break

def registrar_partido():
    limpiar_pantalla()
    if len(jugadores) < 5:
        print("❌ Necesitas al menos 5 jugadores registrados para iniciar un partido.")
        input("Presiona ENTER para volver...")
        return

    rival = questionary.text("Nombre del equipo rival:").ask().title()
    fecha = questionary.text("Ingrese la fecha del partido (ej. DD-MM-YYYY):").ask()

    opciones_todos = [f"{nro} - {datos['nombre']}" for nro, datos in jugadores.items()]
    
    while True:
        seleccionados = questionary.checkbox(
            "Selecciona TODOS los jugadores convocados para el partido (Mínimo 5) Use ESPACIO para marcar:",
            choices=opciones_todos
        ).ask()

        if not seleccionados or len(seleccionados) < 5:
            print("\n❌ Debes seleccionar al menos 5 jugadores. Inténtalo de nuevo.\n")
        else:
            break

    titulares = []
    if len(seleccionados) == 5:
        titulares = seleccionados
    else:
        while True:
            titulares = questionary.checkbox(
                f"Has convocado a {len(seleccionados)} jugadores. Selecciona EXACTAMENTE 5 TITULARES:",
                choices=seleccionados
            ).ask()
            
            if len(titulares) == 5:
                break
            print("\n❌ Error: Debes seleccionar exactamente 5 jugadores. Inténtalo de nuevo.\n")

    stats_partido = []
    
    for t in titulares:
        nro = int(t.split(" - ")[0])
        stats_partido.append({'nro': nro, 'dobles': 0, 'triples': 0, 'faltas': 0})
        
    for r in seleccionados:
        if r not in titulares:
            nro = int(r.split(" - ")[0])
            stats_partido.append({'nro': nro, 'dobles': 0, 'triples': 0, 'faltas': 0})

    simular_partido_en_vivo(rival, fecha, stats_partido)

def simular_partido_en_vivo(rival, fecha, stats_partido):
    while True:
        limpiar_pantalla()
        print(f"=== PARTIDO: USS vs {rival} | FECHA: {fecha} ===\n")
        
        total_puntos_equipo = 0
        for i, p in enumerate(stats_partido):
            nombre = jugadores[p['nro']]['nombre']
            rol = "TITULAR" if i < 5 else "RESERVA"
            
            pts = (p['dobles'] * 2) + (p['triples'] * 3)
            total_puntos_equipo += pts
            
            rayas_dobles = "/" * p['dobles']
            rayas_triples = "/" * p['triples']
            rayas_faltas = "/" * p['faltas']
            
            print(f"#{p['nro']} {nombre} ({rol})")
            print(f"    Dobles:  {rayas_dobles:<10} = {p['dobles'] * 2} Pts")
            print(f"    Triples: {rayas_triples:<10} = {p['triples'] * 3} Pts")
            print(f"    Faltas:  {rayas_faltas:<10} = {p['faltas']} Faltas")
            print("-" * 40)
            
        print(f">>> PUNTOS TOTALES DEL EQUIPO: {total_puntos_equipo} <<<\n")

        opciones_accion = ["Anotar Doble", "Anotar Triple", "Registrar Falta", "FINALIZAR PARTIDO"]
        accion = questionary.select("REGISTRO DEL PARTIDO", choices=opciones_accion).ask()

        if accion == "FINALIZAR PARTIDO":
            confirmar = questionary.confirm("⚠️ Estás seguro que quieres finalizar el partido?").ask()
            
            if not confirmar:
                continue

            while True:
                puntos_rival = questionary.text("Cuántos puntos anotó el equipo rival?").ask()
                if puntos_rival.isdigit():
                    break
                print("❌ Por favor, ingrese un número válido.")
            
            nuevo_partido = {
                "fecha": fecha,
                "rival": rival,
                "puntos_favor": total_puntos_equipo,
                "puntos_contra": int(puntos_rival),
                "estadisticas_jugadores": stats_partido
            }
            partidos.append(nuevo_partido)
            print("\n✅ Partido guardado com exito.")
            input("Presiona ENTER para volver al menú principal...")
            break

        jugador_accion = questionary.select(
            "Qué jugador?", 
            choices=[f"{p['nro']} - {jugadores[p['nro']]['nombre']}" for p in stats_partido]
        ).ask()
        
        nro_seleccionado = int(jugador_accion.split(" - ")[0])

        for p in stats_partido:
            if p['nro'] == nro_seleccionado:
                if accion == "Anotar Doble":
                    p['dobles'] += 1
                elif accion == "Anotar Triple":
                    p['triples'] += 1
                elif accion == "Registrar Falta":
                    p['faltas'] += 1
                break

if __name__ == "__main__":
    mostrar_instrucciones()
    menu_principal()