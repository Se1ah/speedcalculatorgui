import sys

from PyQt6.QtWidgets import (
    QComboBox,
    QWidget,
    QGridLayout,
    QLabel, QLineEdit,
    QPushButton,
    QApplication,
)


class SpeedCalculator(QWidget):
    unit = ""

    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        distance_label = QLabel("Distance")
        self.distance_line_edit = QLineEdit()
        time_label = QLabel("Time (hours)")
        self.time_line_edit = QLineEdit()
        self.output_label = QLabel()
        self.combo = QComboBox()
        self.combo.addItems(['Metric (Km)', 'Imperial (Miles)'])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.get_speed)

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(self.combo, 1, 2)
        grid.addWidget(calculate_button, 2, 1, 1, 1)
        grid.addWidget(self.output_label, 3, 1, 1, 3)

        self.setLayout(grid)

    def get_speed(self):
        try:
            delta_x = float(self.distance_line_edit.text())
            delta_t = float(self.time_line_edit.text())
            avg_speed = delta_x / delta_t
            if self.combo.currentText() == 'Metric (Km)':
                avg_speed = round(avg_speed, 2)
                self.unit = "Km/h"
            if self.combo.currentText() == 'Imperial (Miles)':
                avg_speed = round(avg_speed * 0.621371, 2)
                self.unit = "Mph"
            self.output_label.setText(f"Average speed is {avg_speed} {self.unit}")
            print(f"Average speed is {avg_speed} {self.unit}")
        except ValueError:
            print("Value error")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
