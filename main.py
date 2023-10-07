# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform

import psutil
import pyodbc

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        self.selected_item = None

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Kanpy"
        description = "Kanpy - new kanvan - python project"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)

        # KANPY - BUTTONS - LOGIN
        widgets.num_btn_0.clicked.connect(self.buttonClick)
        widgets.num_btn_1.clicked.connect(self.buttonClick)
        widgets.num_btn_2.clicked.connect(self.buttonClick)
        widgets.num_btn_3.clicked.connect(self.buttonClick)
        widgets.num_btn_4.clicked.connect(self.buttonClick)
        widgets.num_btn_5.clicked.connect(self.buttonClick)
        widgets.num_btn_6.clicked.connect(self.buttonClick)
        widgets.num_btn_7.clicked.connect(self.buttonClick)
        widgets.num_btn_8.clicked.connect(self.buttonClick)
        widgets.num_btn_9.clicked.connect(self.buttonClick)
        widgets.borrar_btn.clicked.connect(self.buttonClick)
        widgets.aceptar_btn.clicked.connect(self.consultar_BD)
        widgets.motrec_btn.setVisible(False)
        widgets.motrec_btn.clicked.connect(self.buttonClick)
        widgets.vehiculos_tbl.setVisible(False)
        widgets.cheklist_btn.clicked.connect(self.buttonClick)
        widgets.cheklist_btn.clicked.connect(self.obtener_checklist)
        widgets.cheklist_btn.setVisible(False)

        # LABEL CONEXION
        network_status = "Online" if psutil.net_if_stats().get("Wi-Fi") else "Offline"
        widgets.conexion_lbl.setText(f"Red: {network_status}")

        # LABEL BATERIA
        bateria = self.obtener_estado_bateria()
        widgets.bateria_lbl.setText(f"Bateria: {bateria}")

        widgets.vehiculos_tbl.itemClicked.connect(self.guardar_itemSelected)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "cheklist_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.checklist_page)

        if btnName.startswith("num_btn"):
            # Extract the number from the button's name
            number = btnName.split("_")[-1]
            current_text = widgets.employeeID_tbx.text()
            widgets.employeeID_tbx.setText(current_text + number)

        if btnName == "borrar_btn":
            widgets.employeeID_tbx.clear()

        if btnName == "aceptar_btn":
            empleado_id = widgets.employeeID_tbx.text()
            print(f'Empleado ID guardado en la variable: {empleado_id}')

        if btnName == "motrec_btn":
            self.obtener_vehiculos()

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def consultar_BD(self):
        empleado_id = widgets.employeeID_tbx.text()
        print(empleado_id)
        server = '172.19.128.18'
        database = 'MasterLabel'
        username = 'sa'
        password = 'PhyTo2k3'

        try:
            conn = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
            cursor = conn.cursor()
            consulta = """\
                    { CALL sp_Emp_ConsultaFotoEmpleado (@empleado=?) }
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

                    # Check if the pixmap was successfully created
                    if not pixmap.isNull():
                        widgets.photo_lbl.setPixmap(pixmap)
                        widgets.photo_lbl.setScaledContents(True)

                        widgets.motrec_btn.setVisible(True)
                        widgets.vehiculos_tbl.setVisible(True)
                    else:
                        QMessageBox.warning(self, "Resultado de la Consulta",
                                            f"El empleado {empleado_id} tiene datos de imagen no válidos.")
                else:
                    QMessageBox.warning(self, "Resultado de la Consulta",
                                        f"El empleado {empleado_id} no tiene una imagen asociada.")
            else:
                QMessageBox.warning(self, "Resultado de la Consulta",
                                    f"No se encontró ningún empleado con el número {empleado_id}")
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error: {str(e)}")

    def obtener_vehiculos(self):
        server = '172.19.128.18'
        database = 'MasterLabel'
        username = 'sa'
        password = 'PhyTo2k3'

        try:
            conn = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
            cursor = conn.cursor()
            consulta = """\
                            { CALL sp_Kb_ConsultaVehiculosSurtidores }
                            """
            cursor.execute(consulta)
            resultado = cursor.fetchall()

            widgets.vehiculos_tbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            widgets.vehiculos_tbl.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            widgets.vehiculos_tbl.verticalHeader().setVisible(False)

            # Configurar el número de filas y columnas en la tabla
            num_filas = 11
            num_columnas = 10
            widgets.vehiculos_tbl.setRowCount(num_filas)
            widgets.vehiculos_tbl.setColumnCount(num_columnas)

            # Llenar la tabla con los IDs de los vehículos en orden de fila y columna
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

            conn.close()

        except Exception as e:
            print(f"Ocurrió un error: {str(e)}")

    def obtener_estado_bateria(self):
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

    def guardar_itemSelected(self, item):
        # Verificar si el elemento es un QTableWidgetItem
        if isinstance(item, QTableWidgetItem):
            # Guardar el elemento seleccionado en la variable
            self.selected_item = item.text()
            print(f'Elemento seleccionado: {self.selected_item}')

            # Habilitar el botón checklist_btn
            widgets.cheklist_btn.setVisible(True)
        else:
            # No se seleccionó ningún elemento, deshabilitar el botón
            widgets.cheklist_btn.setVisible(False)

    def obtener_checklist(self):
        server = '172.19.128.18'
        database = 'MasterLabel'
        username = 'sa'
        password = 'PhyTo2k3'

        try:
            conn = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
            cursor = conn.cursor()
            consulta = "SELECT pregunta FROM ChecklistVehiculosPreguntas"
            cursor.execute(consulta)
            resultado = cursor.fetchall()

            conn.close()

            for i, pregunta in enumerate(resultado):
                label_name = f"pregunta_{i + 1}"
                label_widget = getattr(widgets, label_name, None)
                if label_widget:
                    label_widget.setText(pregunta[0].replace("\n", " ").replace("\r", " "))

        except Exception as e:
            print(f"Ocurrió un error: {str(e)}")

    def respuesta_seleccionada(self):
        sender = self.sender()
        group_name = sender.objectName()  # Nombre del grupo de botones (por ejemplo, "Q1", "Q2", ...)
        respuesta = sender.text()
        self.respuestas[group_name] = respuesta

    def comprobar_respuestas(self):
        for pregunta, respuesta in self.respuestas.items():
            pregunta_numero = pregunta.split("Q")[1]
            print(f"Pregunta {pregunta_numero}: Respuesta seleccionada: {respuesta}")

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
