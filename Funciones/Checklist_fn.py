import pyodbc
from PySide6.QtWidgets import QMessageBox

valores_seleccionados = [None] * 15

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

def Obtener_checklist(widgets):
    conn, cursor = connect_to_database()
    try:
        consulta = """{ CALL getPreguntasChecklistVehiculos_kpy }"""
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        print(resultado)
        for i, pregunta in enumerate(resultado):
            label_name = f"pregunta_{i + 1}"
            label_widget = getattr(widgets, label_name, None)
            if label_widget:
                label_widget.setText(pregunta[0].replace("\n", " ").replace("\r", " "))
    except Exception as e:
        handle_error(widgets, str(e))
    finally:
        close_database_connection(conn)

def radio_button_clicked(widgets, group_index, button):
    group_name = f'Q{group_index}'
    selected_value = button.text()  # Aquí obtienes el valor del botón seleccionado
    valores_seleccionados[group_index - 1] = selected_value

    # Identificar en qué grupo se encuentra el botón seleccionado
    group_name = button.group().objectName()
    print(f"Botón seleccionado en el Grupo {group_name}: {button.text()}")

    todos_seleccionados = all(
        getattr(widgets, f'Q{group_index}').checkedButton() is not None
        for group_index in range(1, 16)
    )

    # Muestra u oculta el botón "horometro_btn"
    widgets.horometro_btn.setVisible(todos_seleccionados)

def guardar_valores():
    print("Valores seleccionados:", valores_seleccionados)

