import pyodbc



def connect_to_database():
    server = '172.19.128.18'
    database = 'KanbanPy'
    username = 'sa'
    password = 'PhyTo2k3'
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        raise ValueError(f"Unable to connect to the database: {str(e)}")

def close_database_connection(conn):
    try:
        conn.close()
    except Exception as e:
        print(f"Error while closing the database connection: {str(e)}")

def insert_data(Chofer, PuedeCircular, Vehiculo, Turno, Duracion, AlarmaReversa, AsientoCinturon, Extintor, Claxon, ProteccionPila, FrenoMano, FrenoPedal, Fugas, ParrillaMastilCuchillas, Llantas, Luces, Palancas, Retrovisor, GanchoMotrec, TableroMontacargas, Horometro, Pregunta16, Pregunta17, Pregunta18, Pregunta19, Pregunta20):
    conn, cursor = connect_to_database()

    try:
        cursor.execute("{CALL setChecklist_kpy(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}",
               (Chofer, PuedeCircular, Vehiculo, Turno, Duracion,
                AlarmaReversa, AsientoCinturon, Extintor, Claxon, ProteccionPila, FrenoMano, FrenoPedal, Fugas,
                ParrillaMastilCuchillas, Llantas, Luces, Palancas, Retrovisor, GanchoMotrec, TableroMontacargas,
                Horometro, Pregunta16, Pregunta17, Pregunta18, Pregunta19, Pregunta20))
        conn.commit()
    except Exception as e:
        print(f"Ocurrió un error: " + str(e))
    finally:
        close_database_connection(conn)
