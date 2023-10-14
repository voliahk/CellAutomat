# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(837, 742)
        MainWindow.setMinimumSize(QSize(816, 675))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(270, 501))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 261, 451))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.start_button = QPushButton(self.layoutWidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(55, 55))
        self.start_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.start_button)

        self.stop_button = QPushButton(self.layoutWidget)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(55, 55))
        self.stop_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.stop_button)

        self.verticalSpacer = QSpacerItem(20, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.reset_button = QPushButton(self.layoutWidget)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setMinimumSize(QSize(55, 55))
        self.reset_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.reset_button)

        self.horizontalLayout_row = QHBoxLayout()
        self.horizontalLayout_row.setObjectName(u"horizontalLayout_row")
        self.row_label = QLabel(self.layoutWidget)
        self.row_label.setObjectName(u"row_label")
        self.row_label.setEnabled(False)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.row_label.setFont(font1)

        self.horizontalLayout_row.addWidget(self.row_label)

        self.horizontalSpacer_4 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_row.addItem(self.horizontalSpacer_4)

        self.row_spinbox = QSpinBox(self.layoutWidget)
        self.row_spinbox.setObjectName(u"row_spinbox")
        self.row_spinbox.setFont(font1)
        self.row_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.row_spinbox.setMinimum(5)
        self.row_spinbox.setMaximum(26)
        self.row_spinbox.setValue(26)

        self.horizontalLayout_row.addWidget(self.row_spinbox)


        self.verticalLayout.addLayout(self.horizontalLayout_row)

        self.horizontalLayout_column = QHBoxLayout()
        self.horizontalLayout_column.setObjectName(u"horizontalLayout_column")
        self.column_label = QLabel(self.layoutWidget)
        self.column_label.setObjectName(u"column_label")
        self.column_label.setEnabled(False)
        self.column_label.setFont(font1)

        self.horizontalLayout_column.addWidget(self.column_label)

        self.horizontalSpacer_5 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_column.addItem(self.horizontalSpacer_5)

        self.column_spinbox = QSpinBox(self.layoutWidget)
        self.column_spinbox.setObjectName(u"column_spinbox")
        self.column_spinbox.setFont(font1)
        self.column_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.column_spinbox.setMinimum(5)
        self.column_spinbox.setMaximum(26)
        self.column_spinbox.setValue(26)

        self.horizontalLayout_column.addWidget(self.column_spinbox)


        self.verticalLayout.addLayout(self.horizontalLayout_column)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_company = QHBoxLayout()
        self.horizontalLayout_company.setObjectName(u"horizontalLayout_company")
        self.company_label = QLabel(self.layoutWidget)
        self.company_label.setObjectName(u"company_label")
        self.company_label.setEnabled(False)
        self.company_label.setFont(font1)

        self.horizontalLayout_company.addWidget(self.company_label)

        self.horizontalSpacer_7 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_company.addItem(self.horizontalSpacer_7)

        self.company_radio = QRadioButton(self.layoutWidget)
        self.company_radio.setObjectName(u"company_radio")
        self.company_radio.setFont(font1)
        self.company_radio.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_company.addWidget(self.company_radio)


        self.verticalLayout_2.addLayout(self.horizontalLayout_company)

        self.horizontalLayout_client = QHBoxLayout()
        self.horizontalLayout_client.setObjectName(u"horizontalLayout_client")
        self.client_label = QLabel(self.layoutWidget)
        self.client_label.setObjectName(u"client_label")
        self.client_label.setEnabled(False)
        self.client_label.setFont(font1)

        self.horizontalLayout_client.addWidget(self.client_label)

        self.horizontalSpacer_6 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_client.addItem(self.horizontalSpacer_6)

        self.client_spinbox = QSpinBox(self.layoutWidget)
        self.client_spinbox.setObjectName(u"client_spinbox")
        self.client_spinbox.setFont(font1)
        self.client_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.client_spinbox.setMinimum(0)
        self.client_spinbox.setMaximum(75)
        self.client_spinbox.setValue(0)

        self.horizontalLayout_client.addWidget(self.client_spinbox)

        self.client_radio = QRadioButton(self.layoutWidget)
        self.client_radio.setObjectName(u"client_radio")
        self.client_radio.setFont(font1)
        self.client_radio.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_client.addWidget(self.client_radio)


        self.verticalLayout_2.addLayout(self.horizontalLayout_client)

        self.horizontalLayout_replenish = QHBoxLayout()
        self.horizontalLayout_replenish.setObjectName(u"horizontalLayout_replenish")
        self.replenish_label = QLabel(self.layoutWidget)
        self.replenish_label.setObjectName(u"replenish_label")
        self.replenish_label.setEnabled(False)
        self.replenish_label.setFont(font1)

        self.horizontalLayout_replenish.addWidget(self.replenish_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_replenish.addItem(self.horizontalSpacer_2)

        self.replenish_checkbox = QCheckBox(self.layoutWidget)
        self.replenish_checkbox.setObjectName(u"replenish_checkbox")
        self.replenish_checkbox.setFont(font1)

        self.horizontalLayout_replenish.addWidget(self.replenish_checkbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_replenish)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.layoutWidget1 = QWidget(self.groupBox_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 501, 621))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(358, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.speed_rate_label = QLabel(self.layoutWidget1)
        self.speed_rate_label.setObjectName(u"speed_rate_label")
        self.speed_rate_label.setEnabled(False)
        self.speed_rate_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.speed_rate_label)

        self.speed_rate_spinbox = QSpinBox(self.layoutWidget1)
        self.speed_rate_spinbox.setObjectName(u"speed_rate_spinbox")
        self.speed_rate_spinbox.setFont(font1)
        self.speed_rate_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.speed_rate_spinbox.setMinimum(1)
        self.speed_rate_spinbox.setMaximum(4)
        self.speed_rate_spinbox.setValue(4)

        self.horizontalLayout_3.addWidget(self.speed_rate_spinbox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.table_widget = QTableWidget(self.layoutWidget1)
        if (self.table_widget.columnCount() < 26):
            self.table_widget.setColumnCount(26)
        if (self.table_widget.rowCount() < 26):
            self.table_widget.setRowCount(26)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.viewport().setProperty("cursor", QCursor(Qt.CrossCursor))
        self.table_widget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.table_widget.setAutoScroll(True)
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_widget.setRowCount(26)
        self.table_widget.setColumnCount(26)
        self.table_widget.horizontalHeader().setVisible(False)
        self.table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.table_widget.horizontalHeader().setMinimumSectionSize(19)
        self.table_widget.horizontalHeader().setDefaultSectionSize(19)
        self.table_widget.horizontalHeader().setHighlightSections(False)
        self.table_widget.horizontalHeader().setStretchLastSection(False)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.verticalHeader().setMinimumSectionSize(19)
        self.table_widget.verticalHeader().setDefaultSectionSize(19)
        self.table_widget.verticalHeader().setHighlightSections(False)
        self.table_widget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.table_widget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(358, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.iteration_label = QLabel(self.layoutWidget1)
        self.iteration_label.setObjectName(u"iteration_label")
        self.iteration_label.setEnabled(False)
        self.iteration_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.iteration_label)

        self.iteration_line_edit = QLineEdit(self.layoutWidget1)
        self.iteration_line_edit.setObjectName(u"iteration_line_edit")
        self.iteration_line_edit.setEnabled(False)
        self.iteration_line_edit.setFont(font1)
        self.iteration_line_edit.setCursor(QCursor(Qt.ForbiddenCursor))

        self.horizontalLayout_2.addWidget(self.iteration_line_edit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.end_message_line_edit = QLineEdit(self.layoutWidget1)
        self.end_message_line_edit.setObjectName(u"end_message_line_edit")
        self.end_message_line_edit.setEnabled(False)
        self.end_message_line_edit.setFont(font1)
        self.end_message_line_edit.setCursor(QCursor(Qt.ForbiddenCursor))

        self.verticalLayout_4.addWidget(self.end_message_line_edit)


        self.horizontalLayout.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 837, 34))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.row_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u043e\u043a", None))
        self.column_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043e\u043d\u043e\u043a", None))
        self.company_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u044f:", None))
        self.company_radio.setText("")
        self.client_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442\u043e\u0432 (%):", None))
        self.client_radio.setText("")
        self.replenish_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u043f\u043e\u043b\u043d\u044f\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432:", None))
        self.replenish_checkbox.setText("")
        self.groupBox_2.setTitle("")
        self.speed_rate_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c:", None))
        self.iteration_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u0435\u0440\u0430\u0446\u0438\u044f:", None))
    # retranslateUi
