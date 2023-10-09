import psutil
import pyodbc
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMessageBox, QHeaderView, QTableWidgetItem

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

def populate_table(widgets, resultado):
    num_filas = 11
    num_columnas = 10
    widgets.vehiculos_tbl.setRowCount(num_filas)
    widgets.vehiculos_tbl.setColumnCount(num_columnas)

    row_index = 0
    column_index = 0
    for row_data in resultado:
        id_data = row_data[0]  # Suponiendo que el primer valor en el resultado es el ID
        item = QTableWidgetItem(str(id_data))
        widgets.vehiculos_tbl.setItem(row_index, column_index, item)

        column_index += 1
        if column_index >= num_columnas:
            column_index = 0
            row_index += 1


def Obtener_Empleado(widgets):
    empleado_id = widgets.employeeID_tbx.text()
    print(empleado_id)

    conn, cursor = connect_to_database()

    try:
        consulta = """\
                { CALL getEmpleado_kpy (@employee=?) }
                """
        params = (empleado_id,)
        cursor.execute(consulta, params)
        resultado = cursor.fetchone()

        if resultado:
            nombre = resultado.Name
            image_data = resultado.Photo

            if image_data:
                widgets.nombre_lbl.setText(nombre)
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)

                if not pixmap.isNull():
                    widgets.photo_lbl.setPixmap(pixmap)
                    widgets.photo_lbl.setScaledContents(True)

                    widgets.motrec_btn.setVisible(True)
                    widgets.vehiculos_tbl.setVisible(True)
                else:
                    QMessageBox.warning(widgets, "Resultado de la Consulta",
                                        f"El empleado {empleado_id} tiene datos de imagen no válidos.")
            else:
                QMessageBox.warning(widgets, "Resultado de la Consulta",
                                    f"El empleado {empleado_id} no tiene una imagen asociada.")
        else:
            QMessageBox.warning(widgets, "Resultado de la Consulta",
                                f"No se encontró ningún empleado con el número {empleado_id}")
    except Exception as e:
        handle_error(widgets, str(e))
    finally:
        close_database_connection(conn)


def Obtener_vehiculos(widgets):
    conn, cursor = connect_to_database()

    try:
        consulta = """\
                        { CALL getVehiculosSurtidores_kpy }
                        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()

        widgets.vehiculos_tbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        widgets.vehiculos_tbl.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        widgets.vehiculos_tbl.verticalHeader().setVisible(False)

        populate_table(widgets, resultado)
    except Exception as e:
        handle_error(widgets, str(e))
    finally:
        close_database_connection(conn)


def Obtener_estado_bateria():
    battery = psutil.sensors_battery()

    if battery is not None:
        percent = battery.percent
        power_plugged = battery.power_plugged

        if power_plugged:
            return f'La computadora está conectada a la corriente y la batería está al {percent}%'
        else:
            return f'La batería está al {percent}%'
    else:
        return '100%'

def Guardar_itemSelected(widgets, item):
    # Verificar si el elemento es un QTableWidgetItem
    if isinstance(item, QTableWidgetItem):
        # Guardar el elemento seleccionado en la variable
        widgets.selected_item = item.text()
        print(f'Elemento seleccionado: {widgets.selected_item}')

        # Habilitar el botón checklist_btn
        widgets.monitores_btn.setVisible(True)
    else:
        # No se seleccionó ningún elemento, deshabilitar el botón
        widgets.monitores_btn.setVisible(False)