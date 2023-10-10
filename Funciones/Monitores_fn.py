import pyodbc
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

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

def handle_error(widgets, message):
    QMessageBox.critical(widgets, "Error", f"Ocurrió un error: {message}")

def Obtener_monitores(widgets):
    conn, cursor = connect_to_database()
    try:
        consulta = """{ CALL getMonitores_kpy }"""
        cursor.execute(consulta)

        # Get column names
        column_names = [column[0] for column in cursor.description]
        num_columns = len(column_names)

        # Set table headers
        widgets.monitores_tbl.verticalHeader().setVisible(False)
        widgets.monitores_tbl.setColumnCount(num_columns)
        widgets.monitores_tbl.setHorizontalHeaderLabels(column_names)

        # Populate the table
        row_num = 0
        for row in cursor.fetchall():
            widgets.monitores_tbl.insertRow(row_num)
            for col_num, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                widgets.monitores_tbl.setItem(row_num, col_num, item)
            row_num += 1
    except Exception as e:
        handle_error(widgets, str(e))
    finally:
        close_database_connection(conn)