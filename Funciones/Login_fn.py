import psutil
import pyodbc
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QHeaderView, QTableWidgetItem, QMessageBox
from modules.notification_widget import NotificationWidget

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

def handle_error(notification_widget, message):
    notification_widget.show_notification(f"Error: {message}")

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
                    error_message = f"El empleado {empleado_id} tiene datos de imagen no válidos."
                    notification_widget = NotificationWidget(error_message)
                    notification_widget.show()
            else:
                error_message = f"El empleado {empleado_id} no tiene una imagen asociada."
                notification_widget = NotificationWidget(error_message)
                notification_widget.show()

        else:
            error_message = f"No se encontró ningún empleado con el número {empleado_id}"
            notification_widget = NotificationWidget(error_message)
            notification_widget.show()
    except Exception as e:
        error_message = "Ocurrió un error: " + str(e)
        notification_widget = NotificationWidget(error_message)
        notification_widget.show()
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

        vehiculo = widgets.selected_item
        print("vehiculooos", vehiculo)
        print(f'Elemento seleccionado: {widgets.selected_item}')

        # Habilitar el botón checklist_btn
        widgets.monitores_btn.setVisible(True)
        return vehiculo
    else:
        # No se seleccionó ningún elemento, deshabilitar el botón
        widgets.monitores_btn.setVisible(False)
        return None

def ObtenerLicencias(widgets):
    empleado_id = widgets.employeeID_tbx.text()
    conn, cursor = connect_to_database()
    try:
        consulta = """\
                { CALL getLicenciasChoferes_kpy (@employee=?) }
                """
        params = (empleado_id, )
        cursor.execute(consulta, params)
        resultado = cursor.fetchall()

        populate_tableLic(widgets, resultado)
    except Exception as e:
        handle_error(widgets, str(e))
    finally:
        close_database_connection(conn)

def populate_tableLic(widgets, resultado):
    num_filas = len(resultado)
    num_columnas = 3  # Number of columns to display: Tipo, Expira, Dias Vigencia

    widgets.licencias_tbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    widgets.licencias_tbl.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    widgets.licencias_tbl.verticalHeader().setVisible(False)

    # Set the number of rows and columns in the table
    widgets.licencias_tbl.setRowCount(num_filas)
    widgets.licencias_tbl.setColumnCount(num_columnas)

    # Define the header labels for the displayed columns
    header_labels = ['Tipo', 'Expira', 'Dias Vigencia']
    widgets.licencias_tbl.setHorizontalHeaderLabels(header_labels)

    for row_index, row_data in enumerate(resultado):
        tipo = row_data[6]  # The 7th element in the row corresponds to 'Tipo'
        expira = row_data[5]  # The 6th element in the row corresponds to 'Expira'
        dias_vigencia = row_data[7]  # The 8th element in the row corresponds to 'Dias Vigencia'

        # Populate the table with data
        widgets.licencias_tbl.setItem(row_index, 0, QTableWidgetItem(tipo))
        widgets.licencias_tbl.setItem(row_index, 1, QTableWidgetItem(expira))
        widgets.licencias_tbl.setItem(row_index, 2, QTableWidgetItem(str(dias_vigencia)))

