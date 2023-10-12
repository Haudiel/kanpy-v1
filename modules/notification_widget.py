import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class NotificationWidget(QWidget):
    def __init__(self, message):
        super().__init__()

        # Establecer propiedades de la ventana de notificación
        self.setGeometry(100, 100, 300, 100)
        self.setWindowTitle("Notificación")

        # Diseño de la ventana de notificación
        layout = QVBoxLayout()

        # Etiqueta para mostrar el mensaje de notificación
        self.message_label = QLabel(message)
        layout.addWidget(self.message_label)

        # Botón para cerrar la notificación
        close_button = QPushButton("Cerrar")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])

    # Crear una instancia de la ventana de notificación
    notification = NotificationWidget("Este es un mensaje de notificación personalizado.")
    notification.show()

    sys.exit(app.exec_())
