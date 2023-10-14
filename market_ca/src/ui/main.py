import sys
from random import randint

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtGui import QColor
from PySide6.QtTest import QTest

from src.ui.ui_main_window import Ui_MainWindow

import src.market_ca.ca_logic as ca_logic

speed_rate = {1: 400, 2: 300, 3: 200, 4: 100}


class MainWindow(QMainWindow):
    IS_RUNNING:  bool
    ITERATION = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.table = self.ui.table_widget
        self.rows = self.ui.row_spinbox.value()
        self.columns = self.ui.column_spinbox.value()
        self.__initialize_table()
        self.market_map = self.__create_game_map()
        self.table.clicked.connect(self.set_unit)

        self.ui.start_button.clicked.connect(self.start_game)
        self.ui.stop_button.clicked.connect(self.stop_game)
        self.ui.reset_button.clicked.connect(self.reset_game)

    def __initialize_table(self):
        self.table.setRowCount(self.rows)
        self.table.setColumnCount(self.columns)

        if self.rows == self.ui.row_spinbox.maximum() and self.columns == self.ui.column_spinbox.maximum():
            self.table.horizontalHeader().setStretchLastSection(True)
            self.table.verticalHeader().setStretchLastSection(True)
        else:
            self.table.horizontalHeader().setStretchLastSection(False)
            self.table.verticalHeader().setStretchLastSection(False)

    def __create_game_map(self):
        return ca_logic.create_map(self.rows, self.columns)

    def __display_on_table(self):
        for row in range(self.rows):
            for column in range(self.columns):
                item_color = QTableWidgetItem()
                color = ca_logic.get_color_unit(self.market_map[row][column].unit)
                item_color.setBackground(QColor(color))
                self.table.setItem(row, column, item_color)

    def set_unit(self):
        row = self.table.currentRow()
        column = self.table.currentColumn()

        if self.ui.company_radio.isChecked():
            if self.market_map[row][column].unit is None:
                self.market_map[row][column].unit = ca_logic.create_unit(ca_logic.UNIT_TYPE['Company'], row, column)
                item_color = QTableWidgetItem()
                color = ca_logic.get_color_unit(self.market_map[row][column].unit)
                item_color.setBackground(QColor(color))
                self.table.setItem(row, column, item_color)
        elif self.ui.client_radio.isChecked():
            if self.market_map[row][column].unit is None:
                self.market_map[row][column].unit = ca_logic.create_unit(ca_logic.UNIT_TYPE['Client'], row, column)
                item_color = QTableWidgetItem()
                color = ca_logic.get_color_unit(self.market_map[row][column].unit)
                item_color.setBackground(QColor(color))
                self.table.setItem(row, column, item_color)

    def __change_ui_elements_status(self, is_enabled):
        self.ui.start_button.setEnabled(is_enabled)
        self.ui.reset_button.setEnabled(is_enabled)
        self.ui.row_spinbox.setEnabled(is_enabled)
        self.ui.column_spinbox.setEnabled(is_enabled)
        self.ui.company_radio.setEnabled(is_enabled)
        self.ui.client_radio.setEnabled(is_enabled)
        self.ui.client_spinbox.setEnabled(is_enabled)
        self.table.setEnabled(is_enabled)
        self.ui.replenish_checkbox.setEnabled(is_enabled)

    def __process_game(self):
        game_status = ca_logic.check_game_status()
        if game_status is not None:
            self.ui.end_message_line_edit.setText(game_status)
            return False

        ca_logic.handle_unit_actions(self.market_map)

        self.ITERATION += 1
        if self.ui.replenish_checkbox.isChecked() and self.ITERATION % 40 == 0:
            self.generate_units(ca_logic.UNIT_TYPE['Client'], randint(3, 10))

        self.__display_on_table()

        return True

    def start_game(self):
        self.__change_ui_elements_status(False)

        self.IS_RUNNING = True

        while self.IS_RUNNING:
            self.IS_RUNNING = self.__process_game()
            self.ui.iteration_line_edit.setText(str(self.ITERATION))
            QTest.qWait(speed_rate.get(self.ui.speed_rate_spinbox.value()))
        self.stop_game()

    def generate_units(self, unit_type, percent):
        ca_logic.generate_units(unit_type, self.market_map,
                                percent, self.rows, self.columns)

    def stop_game(self):
        self.__change_ui_elements_status(True)
        self.IS_RUNNING = False

    def reset_game(self):
        ca_logic.clear_objects(self.market_map)

        self.rows = self.ui.row_spinbox.value()
        self.columns = self.ui.column_spinbox.value()

        self.market_map = self.__create_game_map()
        self.generate_units(ca_logic.UNIT_TYPE['Client'], self.ui.client_spinbox.value())

        self.__initialize_table()
        self.__display_on_table()

        self.ITERATION = 0
        self.ui.iteration_line_edit.setText(str(self.ITERATION))
        self.ui.end_message_line_edit.setText('')


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
