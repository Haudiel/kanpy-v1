# ///////////////////////////////////////////////////////////////
# NUEVO KANVAN
#
# PAGINA PRINCIPAL DE LA APLICACIÓN
#
# INDICE:
#   1. LIBRERIAS
#   2. WIDGETS GLOBAL
#   3. BARRA DE TITULO | USAR "FALSE" PARA MAC OR LINUX
#   4. NOMBRE DE LA APP
#   5. APLICAR TEXTO
#   6. TOGGLE MENU
#   7. SET UI DEFINITIONS
#   8. QTableWidget PARAMETERS
#   9. FUNCIONALIDAD DE BOTONES
#       9.1 LEFT MENUS
#       9.2 LOGIN
#       9.3 MONITORES
#       9.4 CHECKLIST
#       9.5 LABEL CONEXION
#       9.6 LABEL BATERIA
#       9.7 RADIO BUTTONS
#   10. EXTRA LEFT BOX
#   11. EXTRA RIGHT BOX
#   12. SHOW APP
#   13. SET CUSTOM THEME
#   14. SET THEME AND HACKS
#   15. SET HOME PAGE AND SELECT MENU
#   16. FUNCION DE BUTTON CLICK
#       16.1 BOTONES PAGE
#       16.2 BOTONES DEL LOGIN
#       16.3 BOTONES MONITORES
#       16.4 BOTONES CHECKLIST
#   17. RESIZE EVENTS
#   18. MOUSE CLICK EVENTS
# ///////////////////////////////////////////////////////////////

# 1. LIBRERIAS
import sys
import os
import platform
import psutil
import pyodbc
from modules import *
from modules import Settings
from Funciones.Login_fn import Obtener_Empleado, Obtener_vehiculos, ObtenerLicencias,Obtener_estado_bateria, Guardar_itemSelected
from Funciones.Monitores_fn import Obtener_monitores
from Funciones.Checklist_fn import Obtener_checklist, radio_button_clicked, guardar_valores
from widgets import *
os.environ["QT_FONT_DPI"] = "96"

# 2. WIDGETS GLOBAL
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        self.selected_item = None

        # 3. BARRA DE TITULO | USAR "FALSE" PARA MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # 4. NOMBRE DE LA APP
        title = "Kanpy"
        description = "Kanpy - new kanvan - python project"

        # 5. APLICAR TEXTO
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # 6. TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # 7. SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

    # 9. FUNCIONALIDAD DE BOTONES
        # 9.1 LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)

        # 9.2 LOGIN
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
        widgets.aceptar_btn.clicked.connect(lambda: Obtener_Empleado(widgets))
        widgets.aceptar_btn.clicked.connect(lambda: ObtenerLicencias(widgets))
        widgets.motrec_btn.setVisible(False)
        widgets.motrec_btn.clicked.connect(self.buttonClick)
        widgets.vehiculos_tbl.setVisible(False)
        widgets.vehiculos_tbl.itemClicked.connect(lambda item: Guardar_itemSelected(widgets, item))

        # 9.3 MONITORES
        widgets.monitores_btn.clicked.connect(self.buttonClick)
        widgets.monitores_btn.clicked.connect(lambda: Obtener_monitores(widgets))
        widgets.monitores_btn.setVisible(False)

        # 9.4 CHECKLIST
        widgets.checklist_btn.clicked.connect(self.buttonClick)
        widgets.checklist_btn.clicked.connect(lambda: Obtener_checklist(widgets))

        # 9.5 LABEL CONEXION
        network_status = "Online" if psutil.net_if_stats().get("Wi-Fi") else "Offline"
        widgets.conexion_lbl.setText(f"Red: {network_status}")

        # 9.6 LABEL BATERIA
        bateria = Obtener_estado_bateria()
        widgets.bateria_lbl.setText(f"Bateria: {bateria}")

        # 9.7 RADIO BUTTONS
        for group_index in range(1, 16):
            group_name = f'Q{group_index}'
            button_group = getattr(widgets, group_name, None)
            if button_group:
                button_group.buttonClicked.connect(lambda button, widgets=widgets, group_index=group_index: radio_button_clicked(widgets, group_index, button))

        # 9.8 HOROMETRO
        for i in range(10):
                    button_name = f'btn_h_{i}'
                    button = getattr(widgets, button_name, None)
                    if button:
                        button.clicked.connect(self.buttonClick)
        widgets.horometro_btn.setVisible(False)
        widgets.horometro_btn.clicked.connect(self.buttonClick)
        widgets.horometro_btn.clicked.connect(guardar_valores)
        widgets.haceptar_btn.clicked.connect(self.buttonClick)
        widgets.hborrar_btn.clicked.connect(self.buttonClick)

        # 10. EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # 11. EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # 12. SHOW APP
        self.show()

        # 13. SET CUSTOM THEME
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # 14. SET THEME AND HACKS
        if useCustomTheme:
            UIFunctions.theme(self, themeFile, True)
            AppFunctions.setThemeHack(self)

        # 15. SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # 16. FUNCION DE BUTTON CLICK
    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        # 16.1 BOTONES PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 16.2 BOTONES DEL LOGIN
        if btnName.startswith("num_btn"):
            number = btnName.split("_")[-1]
            current_text = widgets.employeeID_tbx.text()
            widgets.employeeID_tbx.setText(current_text + number)

        if btnName == "borrar_btn":
            widgets.employeeID_tbx.clear()

        if btnName == "aceptar_btn":
            empleado_id = widgets.employeeID_tbx.text()
            print(f'Empleado ID guardado en la variable: {empleado_id}')

        if btnName == "motrec_btn":
            Obtener_vehiculos(widgets)

        # 16.3 BOTONES MONITORES
        if btnName == "monitores_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.monitores_page)

        # 16.4 BOTONES CHECKLIST
        if btnName == "checklist_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.checklist_page)

        # 16.5 BOTONES HOROMETRO
        if btnName == "horometro_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.horometro_page)

        if btnName.startswith("btn_h"):
            number = btnName.split("_")[-1]
            current_text = widgets.horometro_tbx.text()
            widgets.horometro_tbx.setText(current_text + number)

        if btnName == 'hborrar_btn':
            widgets.horometro_tbx.clear()

        if btnName == "haceptar_btn":
            horometro = widgets.horometro_tbx.text()
            print(horometro)

        print(f'Button "{btnName}" pressed!')

    # 17. RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # 18. MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def handle_error(self, message):
        QMessageBox.critical(self, "Error", f"Ocurrió un error: {message}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
