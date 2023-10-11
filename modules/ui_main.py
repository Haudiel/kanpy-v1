# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1100, 700))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid #6272a4;\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {\n"
"	background-color: rgb("
                        "40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/logo_MW.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #6272a4; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {\n"
"	background-color: #6272a4;\n"
"	color: rgb(255, 255,"
                        " 255);\n"
"}\n"
"#bottomMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {\n"
"	background-color: #6272a4;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRight"
                        "Info { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{\n"
"	background-color: #6272a4\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#e"
                        "xtraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {\n"
"	background-color: #6272a4;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-colo"
                        "r: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: #6272a4; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {\n"
"	background-color: #6272a4;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* //////////////////////////////////////////////////////////////////////////////"
                        "///////////////////\n"
"QTableWidget */\n"
"QTableWidget {\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: #6272a4;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHe"
                        "aderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
""
                        "    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #6272a4;\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    bo"
                        "rder-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"	background: #6272a4;\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-r"
                        "adius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* //////////////////////////////////////////////////////////////////////////////////////////////"
                        "///\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-righ"
                        "t-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: #6272a4;\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: #6272a4;\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #6272a4;\n"
"}\n"
"QSlider::handle:horizontal:"
                        "pressed {\n"
"    background-color: #6272a4;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: #6272a4;\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: #6272a4;\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #6272a4;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {\n"
"	color: #6272a4;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: #6272a4;\n"
"}\n"
"QCommandLinkButton:hover {\n"
"	color: #6272a4;\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {\n"
"	color: #6272a"
                        "4;\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy1.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy1)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy1.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy1)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy1.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy1)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.gridLayout_9 = QGridLayout(self.home)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_3 = QFrame(self.home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.monitores_btn = QPushButton(self.frame_3)
        self.monitores_btn.setObjectName(u"monitores_btn")
        self.monitores_btn.setMinimumSize(QSize(100, 25))
        self.monitores_btn.setMaximumSize(QSize(150, 50))

        self.gridLayout_3.addWidget(self.monitores_btn, 1, 1, 1, 1)

        self.vehiculos_tbl = QTableWidget(self.frame_3)
        self.vehiculos_tbl.setObjectName(u"vehiculos_tbl")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.vehiculos_tbl.sizePolicy().hasHeightForWidth())
        self.vehiculos_tbl.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.vehiculos_tbl, 0, 0, 1, 2)


        self.gridLayout_5.addLayout(self.gridLayout_3, 1, 0, 1, 2)

        self.motrec_btn = QPushButton(self.frame_3)
        self.motrec_btn.setObjectName(u"motrec_btn")
        self.motrec_btn.setMinimumSize(QSize(100, 25))
        self.motrec_btn.setMaximumSize(QSize(150, 50))

        self.gridLayout_5.addWidget(self.motrec_btn, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.frame_3, 1, 1, 2, 1)

        self.frame_2 = QFrame(self.home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(407, 255))
        self.frame_2.setMaximumSize(QSize(16777215, 300))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.nombre_lbl = QLabel(self.frame_2)
        self.nombre_lbl.setObjectName(u"nombre_lbl")
        self.nombre_lbl.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.nombre_lbl, 0, 0, 1, 2)

        self.photo_lbl = QLabel(self.frame_2)
        self.photo_lbl.setObjectName(u"photo_lbl")
        self.photo_lbl.setMinimumSize(QSize(180, 190))
        self.photo_lbl.setMaximumSize(QSize(180, 190))

        self.gridLayout_12.addWidget(self.photo_lbl, 1, 0, 1, 1)

        self.licencias_tbl = QTableWidget(self.frame_2)
        self.licencias_tbl.setObjectName(u"licencias_tbl")
        sizePolicy4.setHeightForWidth(self.licencias_tbl.sizePolicy().hasHeightForWidth())
        self.licencias_tbl.setSizePolicy(sizePolicy4)

        self.gridLayout_12.addWidget(self.licencias_tbl, 1, 1, 1, 1)


        self.gridLayout_9.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setTabletTracking(False)
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.employeeID_tbx = QLineEdit(self.frame)
        self.employeeID_tbx.setObjectName(u"employeeID_tbx")
        self.employeeID_tbx.setMinimumSize(QSize(205, 66))
        self.employeeID_tbx.setMaximumSize(QSize(450, 80))

        self.gridLayout_11.addWidget(self.employeeID_tbx, 1, 0, 1, 3)

        self.empleado_lbl = QLabel(self.frame)
        self.empleado_lbl.setObjectName(u"empleado_lbl")
        self.empleado_lbl.setMinimumSize(QSize(205, 66))
        self.empleado_lbl.setMaximumSize(QSize(450, 80))

        self.gridLayout_11.addWidget(self.empleado_lbl, 0, 0, 1, 3)

        self.num_btn_5 = QPushButton(self.frame)
        self.num_btn_5.setObjectName(u"num_btn_5")
        self.num_btn_5.setMinimumSize(QSize(65, 66))
        self.num_btn_5.setMaximumSize(QSize(150, 80))

        self.gridLayout_11.addWidget(self.num_btn_5, 3, 1, 1, 1)

        self.num_btn_1 = QPushButton(self.frame)
        self.num_btn_1.setObjectName(u"num_btn_1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.num_btn_1.sizePolicy().hasHeightForWidth())
        self.num_btn_1.setSizePolicy(sizePolicy5)
        self.num_btn_1.setMinimumSize(QSize(65, 66))
        self.num_btn_1.setMaximumSize(QSize(150, 80))

        self.gridLayout_11.addWidget(self.num_btn_1, 2, 0, 1, 1)

        self.num_btn_3 = QPushButton(self.frame)
        self.num_btn_3.setObjectName(u"num_btn_3")
        self.num_btn_3.setMinimumSize(QSize(65, 66))
        self.num_btn_3.setMaximumSize(QSize(150, 80))

        self.gridLayout_11.addWidget(self.num_btn_3, 2, 2, 1, 1)

        self.num_btn_9 = QPushButton(self.frame)
        self.num_btn_9.setObjectName(u"num_btn_9")
        self.num_btn_9.setMinimumSize(QSize(65, 66))
        self.num_btn_9.setMaximumSize(QSize(150, 80))

        self.gridLayout_11.addWidget(self.num_btn_9, 4, 2, 1, 1)

        self.num_btn_6 = QPushButton(self.frame)
        self.num_btn_6.setObjectName(u"num_btn_6")
        self.num_btn_6.setMinimumSize(QSize(65, 66))
        self.num_btn_6.setMaximumSize(QSize(150, 80))

        self.gridLayout_11.addWidget(self.num_btn_6, 3, 2, 1, 1)

        self.borrar_btn = QPushButton(self.frame)
        self.borrar_btn.setObjectName(u"borrar_btn")
        self.borrar_btn.setMinimumSize(QSize(135, 66))
        self.borrar_btn.setMaximumSize(QSize(300, 80))

        self.gridLayout_11.addWidget(self.borrar_btn, 5, 1, 1, 2)

        self.num_btn_8 = QPushButton(self.frame)
        self.num_btn_8.setObjectName(u"num_btn_8")
        self.num_btn_8.setMinimumSize(QSize(65, 66))
        self.num_btn_8.setMaximumSize(QSize(150, 80))

        self.gridLayout_11.addWidget(self.num_btn_8, 4, 1, 1, 1)

        self.aceptar_btn = QPushButton(self.frame)
        self.aceptar_btn.setObjectName(u"aceptar_btn")
        self.aceptar_btn.setMinimumSize(QSize(205, 66))
        self.aceptar_btn.setMaximumSize(QSize(450, 80))

        self.gridLayout_11.addWidget(self.aceptar_btn, 6, 0, 1, 3)

        self.num_btn_0 = QPushButton(self.frame)
        self.num_btn_0.setObjectName(u"num_btn_0")
        self.num_btn_0.setMinimumSize(QSize(65, 66))
        self.num_btn_0.setMaximumSize(QSize(150, 80))

        self.gridLayout_11.addWidget(self.num_btn_0, 5, 0, 1, 1)

        self.num_btn_2 = QPushButton(self.frame)
        self.num_btn_2.setObjectName(u"num_btn_2")
        self.num_btn_2.setMinimumSize(QSize(65, 66))
        self.num_btn_2.setMaximumSize(QSize(150, 80))

        self.gridLayout_11.addWidget(self.num_btn_2, 2, 1, 1, 1)

        self.num_btn_7 = QPushButton(self.frame)
        self.num_btn_7.setObjectName(u"num_btn_7")
        self.num_btn_7.setMinimumSize(QSize(65, 66))
        self.num_btn_7.setMaximumSize(QSize(150, 80))

        self.gridLayout_11.addWidget(self.num_btn_7, 4, 0, 1, 1)

        self.num_btn_4 = QPushButton(self.frame)
        self.num_btn_4.setObjectName(u"num_btn_4")
        self.num_btn_4.setMinimumSize(QSize(65, 66))
        self.num_btn_4.setMaximumSize(QSize(150, 80))

        self.gridLayout_11.addWidget(self.num_btn_4, 3, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame, 0, 0, 2, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.home)
        self.monitores_page = QWidget()
        self.monitores_page.setObjectName(u"monitores_page")
        self.gridLayout_7 = QGridLayout(self.monitores_page)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, -1, 6)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.monitorI_lbl = QLabel(self.monitores_page)
        self.monitorI_lbl.setObjectName(u"monitorI_lbl")
        self.monitorI_lbl.setMinimumSize(QSize(280, 66))
        self.monitorI_lbl.setMaximumSize(QSize(280, 66))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.monitorI_lbl.setFont(font4)
        self.monitorI_lbl.setStyleSheet(u"QLabel { font-size: 48px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }")

        self.gridLayout_6.addWidget(self.monitorI_lbl, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.monitores_tbl = QTableWidget(self.monitores_page)
        self.monitores_tbl.setObjectName(u"monitores_tbl")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.monitores_tbl.sizePolicy().hasHeightForWidth())
        self.monitores_tbl.setSizePolicy(sizePolicy6)
        self.monitores_tbl.setMinimumSize(QSize(400, 453))
        self.monitores_tbl.setMaximumSize(QSize(400, 600))

        self.gridLayout_6.addWidget(self.monitores_tbl, 1, 0, 2, 1)

        self.monitor_lbl = QLabel(self.monitores_page)
        self.monitor_lbl.setObjectName(u"monitor_lbl")
        sizePolicy6.setHeightForWidth(self.monitor_lbl.sizePolicy().hasHeightForWidth())
        self.monitor_lbl.setSizePolicy(sizePolicy6)
        self.monitor_lbl.setMinimumSize(QSize(280, 66))
        self.monitor_lbl.setMaximumSize(QSize(280, 66))

        self.gridLayout_6.addWidget(self.monitor_lbl, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 4, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 2)

        self.checklist_btn = QPushButton(self.monitores_page)
        self.checklist_btn.setObjectName(u"checklist_btn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.checklist_btn.sizePolicy().hasHeightForWidth())
        self.checklist_btn.setSizePolicy(sizePolicy7)
        self.checklist_btn.setMinimumSize(QSize(150, 50))
        self.checklist_btn.setMaximumSize(QSize(150, 50))

        self.gridLayout_7.addWidget(self.checklist_btn, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.monitores_page)
        self.checklist_page = QWidget()
        self.checklist_page.setObjectName(u"checklist_page")
        self.gridLayout_4 = QGridLayout(self.checklist_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.radioButton_41 = QRadioButton(self.checklist_page)
        self.Q10 = QButtonGroup(MainWindow)
        self.Q10.setObjectName(u"Q10")
        self.Q10.addButton(self.radioButton_41)
        self.radioButton_41.setObjectName(u"radioButton_41")
        self.radioButton_41.setMaximumSize(QSize(100, 35))
        self.radioButton_41.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_41, 11, 3, 1, 1)

        self.radioButton_33 = QRadioButton(self.checklist_page)
        self.Q15 = QButtonGroup(MainWindow)
        self.Q15.setObjectName(u"Q15")
        self.Q15.addButton(self.radioButton_33)
        self.radioButton_33.setObjectName(u"radioButton_33")
        self.radioButton_33.setMaximumSize(QSize(100, 35))
        self.radioButton_33.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_33, 16, 2, 1, 1)

        self.radioButton_43 = QRadioButton(self.checklist_page)
        self.Q12 = QButtonGroup(MainWindow)
        self.Q12.setObjectName(u"Q12")
        self.Q12.addButton(self.radioButton_43)
        self.radioButton_43.setObjectName(u"radioButton_43")
        self.radioButton_43.setMaximumSize(QSize(100, 35))
        self.radioButton_43.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_43, 13, 3, 1, 1)

        self.radioButton_21 = QRadioButton(self.checklist_page)
        self.Q3 = QButtonGroup(MainWindow)
        self.Q3.setObjectName(u"Q3")
        self.Q3.addButton(self.radioButton_21)
        self.radioButton_21.setObjectName(u"radioButton_21")
        self.radioButton_21.setMaximumSize(QSize(100, 35))
        self.radioButton_21.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_21, 3, 2, 1, 1)

        self.pregunta_2 = QLabel(self.checklist_page)
        self.pregunta_2.setObjectName(u"pregunta_2")

        self.gridLayout_4.addWidget(self.pregunta_2, 1, 0, 1, 1)

        self.pregunta_13 = QLabel(self.checklist_page)
        self.pregunta_13.setObjectName(u"pregunta_13")

        self.gridLayout_4.addWidget(self.pregunta_13, 14, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.checklist_page)
        self.Q2 = QButtonGroup(MainWindow)
        self.Q2.setObjectName(u"Q2")
        self.Q2.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMaximumSize(QSize(100, 35))
        self.radioButton_2.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_2, 1, 1, 1, 1)

        self.radioButton_29 = QRadioButton(self.checklist_page)
        self.Q11 = QButtonGroup(MainWindow)
        self.Q11.setObjectName(u"Q11")
        self.Q11.addButton(self.radioButton_29)
        self.radioButton_29.setObjectName(u"radioButton_29")
        self.radioButton_29.setMaximumSize(QSize(100, 35))
        self.radioButton_29.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_29, 12, 2, 1, 1)

        self.radioButton_27 = QRadioButton(self.checklist_page)
        self.Q9 = QButtonGroup(MainWindow)
        self.Q9.setObjectName(u"Q9")
        self.Q9.addButton(self.radioButton_27)
        self.radioButton_27.setObjectName(u"radioButton_27")
        self.radioButton_27.setMaximumSize(QSize(100, 35))
        self.radioButton_27.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_27, 10, 2, 1, 1)

        self.pregunta_8 = QLabel(self.checklist_page)
        self.pregunta_8.setObjectName(u"pregunta_8")

        self.gridLayout_4.addWidget(self.pregunta_8, 9, 0, 1, 1)

        self.pregunta_15 = QLabel(self.checklist_page)
        self.pregunta_15.setObjectName(u"pregunta_15")

        self.gridLayout_4.addWidget(self.pregunta_15, 16, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.checklist_page)
        self.Q2.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMaximumSize(QSize(100, 35))
        self.radioButton_3.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_3, 1, 2, 1, 1)

        self.radioButton_45 = QRadioButton(self.checklist_page)
        self.Q14 = QButtonGroup(MainWindow)
        self.Q14.setObjectName(u"Q14")
        self.Q14.addButton(self.radioButton_45)
        self.radioButton_45.setObjectName(u"radioButton_45")
        self.radioButton_45.setMaximumSize(QSize(100, 35))
        self.radioButton_45.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_45, 15, 3, 1, 1)

        self.radioButton_39 = QRadioButton(self.checklist_page)
        self.Q8 = QButtonGroup(MainWindow)
        self.Q8.setObjectName(u"Q8")
        self.Q8.addButton(self.radioButton_39)
        self.radioButton_39.setObjectName(u"radioButton_39")
        self.radioButton_39.setMaximumSize(QSize(100, 35))
        self.radioButton_39.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_39, 9, 3, 1, 1)

        self.radioButton_26 = QRadioButton(self.checklist_page)
        self.Q8.addButton(self.radioButton_26)
        self.radioButton_26.setObjectName(u"radioButton_26")
        self.radioButton_26.setMaximumSize(QSize(100, 35))
        self.radioButton_26.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_26, 9, 2, 1, 1)

        self.radioButton_8 = QRadioButton(self.checklist_page)
        self.Q3.addButton(self.radioButton_8)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setMaximumSize(QSize(100, 35))
        self.radioButton_8.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_8, 3, 1, 1, 1)

        self.pregunta_1 = QLabel(self.checklist_page)
        self.pregunta_1.setObjectName(u"pregunta_1")

        self.gridLayout_4.addWidget(self.pregunta_1, 0, 0, 1, 1)

        self.radioButton_25 = QRadioButton(self.checklist_page)
        self.Q7 = QButtonGroup(MainWindow)
        self.Q7.setObjectName(u"Q7")
        self.Q7.addButton(self.radioButton_25)
        self.radioButton_25.setObjectName(u"radioButton_25")
        self.radioButton_25.setMaximumSize(QSize(100, 35))
        self.radioButton_25.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_25, 8, 2, 1, 1)

        self.radioButton_34 = QRadioButton(self.checklist_page)
        self.Q3.addButton(self.radioButton_34)
        self.radioButton_34.setObjectName(u"radioButton_34")
        self.radioButton_34.setMaximumSize(QSize(100, 35))
        self.radioButton_34.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_34, 3, 3, 1, 1)

        self.radioButton_28 = QRadioButton(self.checklist_page)
        self.Q10.addButton(self.radioButton_28)
        self.radioButton_28.setObjectName(u"radioButton_28")
        self.radioButton_28.setMaximumSize(QSize(100, 35))
        self.radioButton_28.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_28, 11, 2, 1, 1)

        self.radioButton_15 = QRadioButton(self.checklist_page)
        self.Q10.addButton(self.radioButton_15)
        self.radioButton_15.setObjectName(u"radioButton_15")
        self.radioButton_15.setMaximumSize(QSize(100, 35))
        self.radioButton_15.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_15, 11, 1, 1, 1)

        self.radioButton_7 = QRadioButton(self.checklist_page)
        self.Q1 = QButtonGroup(MainWindow)
        self.Q1.setObjectName(u"Q1")
        self.Q1.addButton(self.radioButton_7)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setMaximumSize(QSize(100, 35))
        self.radioButton_7.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_7, 0, 3, 1, 1)

        self.radioButton_10 = QRadioButton(self.checklist_page)
        self.Q5 = QButtonGroup(MainWindow)
        self.Q5.setObjectName(u"Q5")
        self.Q5.addButton(self.radioButton_10)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setMaximumSize(QSize(100, 35))
        self.radioButton_10.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_10, 6, 1, 1, 1)

        self.radioButton_42 = QRadioButton(self.checklist_page)
        self.Q11.addButton(self.radioButton_42)
        self.radioButton_42.setObjectName(u"radioButton_42")
        self.radioButton_42.setMaximumSize(QSize(100, 35))
        self.radioButton_42.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_42, 12, 3, 1, 1)

        self.radioButton_35 = QRadioButton(self.checklist_page)
        self.Q4 = QButtonGroup(MainWindow)
        self.Q4.setObjectName(u"Q4")
        self.Q4.addButton(self.radioButton_35)
        self.radioButton_35.setObjectName(u"radioButton_35")
        self.radioButton_35.setMaximumSize(QSize(100, 35))
        self.radioButton_35.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_35, 4, 3, 1, 1)

        self.radioButton_24 = QRadioButton(self.checklist_page)
        self.Q6 = QButtonGroup(MainWindow)
        self.Q6.setObjectName(u"Q6")
        self.Q6.addButton(self.radioButton_24)
        self.radioButton_24.setObjectName(u"radioButton_24")
        self.radioButton_24.setMaximumSize(QSize(100, 35))
        self.radioButton_24.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_24, 7, 2, 1, 1)

        self.radioButton_5 = QRadioButton(self.checklist_page)
        self.Q1.addButton(self.radioButton_5)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_5, 0, 1, 1, 1)

        self.radioButton_6 = QRadioButton(self.checklist_page)
        self.Q1.addButton(self.radioButton_6)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setMaximumSize(QSize(100, 35))
        self.radioButton_6.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_6, 0, 2, 1, 1)

        self.radioButton_22 = QRadioButton(self.checklist_page)
        self.Q4.addButton(self.radioButton_22)
        self.radioButton_22.setObjectName(u"radioButton_22")
        self.radioButton_22.setMaximumSize(QSize(100, 35))
        self.radioButton_22.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_22, 4, 2, 1, 1)

        self.radioButton_30 = QRadioButton(self.checklist_page)
        self.Q12.addButton(self.radioButton_30)
        self.radioButton_30.setObjectName(u"radioButton_30")
        self.radioButton_30.setMaximumSize(QSize(100, 35))
        self.radioButton_30.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_30, 13, 2, 1, 1)

        self.radioButton_37 = QRadioButton(self.checklist_page)
        self.Q6.addButton(self.radioButton_37)
        self.radioButton_37.setObjectName(u"radioButton_37")
        self.radioButton_37.setMaximumSize(QSize(100, 35))
        self.radioButton_37.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_37, 7, 3, 1, 1)

        self.radioButton_20 = QRadioButton(self.checklist_page)
        self.Q13 = QButtonGroup(MainWindow)
        self.Q13.setObjectName(u"Q13")
        self.Q13.addButton(self.radioButton_20)
        self.radioButton_20.setObjectName(u"radioButton_20")
        self.radioButton_20.setMaximumSize(QSize(100, 35))
        self.radioButton_20.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_20, 14, 1, 1, 1)

        self.pregunta_4 = QLabel(self.checklist_page)
        self.pregunta_4.setObjectName(u"pregunta_4")

        self.gridLayout_4.addWidget(self.pregunta_4, 4, 0, 1, 1)

        self.pregunta_12 = QLabel(self.checklist_page)
        self.pregunta_12.setObjectName(u"pregunta_12")

        self.gridLayout_4.addWidget(self.pregunta_12, 13, 0, 1, 1)

        self.radioButton_14 = QRadioButton(self.checklist_page)
        self.Q9.addButton(self.radioButton_14)
        self.radioButton_14.setObjectName(u"radioButton_14")
        self.radioButton_14.setMaximumSize(QSize(100, 35))
        self.radioButton_14.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_14, 10, 1, 1, 1)

        self.radioButton_19 = QRadioButton(self.checklist_page)
        self.Q15.addButton(self.radioButton_19)
        self.radioButton_19.setObjectName(u"radioButton_19")
        self.radioButton_19.setMaximumSize(QSize(100, 35))
        self.radioButton_19.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_19, 16, 1, 1, 1)

        self.radioButton_44 = QRadioButton(self.checklist_page)
        self.Q13.addButton(self.radioButton_44)
        self.radioButton_44.setObjectName(u"radioButton_44")
        self.radioButton_44.setMaximumSize(QSize(100, 35))
        self.radioButton_44.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_44, 14, 3, 1, 1)

        self.pregunta_9 = QLabel(self.checklist_page)
        self.pregunta_9.setObjectName(u"pregunta_9")

        self.gridLayout_4.addWidget(self.pregunta_9, 10, 0, 1, 1)

        self.radioButton_16 = QRadioButton(self.checklist_page)
        self.Q11.addButton(self.radioButton_16)
        self.radioButton_16.setObjectName(u"radioButton_16")
        self.radioButton_16.setMaximumSize(QSize(100, 35))
        self.radioButton_16.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_16, 12, 1, 1, 1)

        self.radioButton_18 = QRadioButton(self.checklist_page)
        self.Q14.addButton(self.radioButton_18)
        self.radioButton_18.setObjectName(u"radioButton_18")
        self.radioButton_18.setMaximumSize(QSize(100, 35))
        self.radioButton_18.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_18, 15, 1, 1, 1)

        self.pregunta_6 = QLabel(self.checklist_page)
        self.pregunta_6.setObjectName(u"pregunta_6")

        self.gridLayout_4.addWidget(self.pregunta_6, 7, 0, 1, 1)

        self.pregunta_14 = QLabel(self.checklist_page)
        self.pregunta_14.setObjectName(u"pregunta_14")

        self.gridLayout_4.addWidget(self.pregunta_14, 15, 0, 1, 1)

        self.radioButton_31 = QRadioButton(self.checklist_page)
        self.Q13.addButton(self.radioButton_31)
        self.radioButton_31.setObjectName(u"radioButton_31")
        self.radioButton_31.setMaximumSize(QSize(100, 35))
        self.radioButton_31.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_31, 14, 2, 1, 1)

        self.radioButton_40 = QRadioButton(self.checklist_page)
        self.Q9.addButton(self.radioButton_40)
        self.radioButton_40.setObjectName(u"radioButton_40")
        self.radioButton_40.setMaximumSize(QSize(100, 35))
        self.radioButton_40.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_40, 10, 3, 1, 1)

        self.radioButton_9 = QRadioButton(self.checklist_page)
        self.Q4.addButton(self.radioButton_9)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setMaximumSize(QSize(100, 35))
        self.radioButton_9.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_9, 4, 1, 1, 1)

        self.radioButton_12 = QRadioButton(self.checklist_page)
        self.Q7.addButton(self.radioButton_12)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setMaximumSize(QSize(100, 35))
        self.radioButton_12.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_12, 8, 1, 1, 1)

        self.radioButton_32 = QRadioButton(self.checklist_page)
        self.Q14.addButton(self.radioButton_32)
        self.radioButton_32.setObjectName(u"radioButton_32")
        self.radioButton_32.setMaximumSize(QSize(100, 35))
        self.radioButton_32.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_32, 15, 2, 1, 1)

        self.radioButton_46 = QRadioButton(self.checklist_page)
        self.Q15.addButton(self.radioButton_46)
        self.radioButton_46.setObjectName(u"radioButton_46")
        self.radioButton_46.setMaximumSize(QSize(100, 35))
        self.radioButton_46.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_46, 16, 3, 1, 1)

        self.pregunta_7 = QLabel(self.checklist_page)
        self.pregunta_7.setObjectName(u"pregunta_7")

        self.gridLayout_4.addWidget(self.pregunta_7, 8, 0, 1, 1)

        self.radioButton_36 = QRadioButton(self.checklist_page)
        self.Q5.addButton(self.radioButton_36)
        self.radioButton_36.setObjectName(u"radioButton_36")
        self.radioButton_36.setMaximumSize(QSize(100, 35))
        self.radioButton_36.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_36, 6, 3, 1, 1)

        self.pregunta_3 = QLabel(self.checklist_page)
        self.pregunta_3.setObjectName(u"pregunta_3")

        self.gridLayout_4.addWidget(self.pregunta_3, 3, 0, 1, 1)

        self.pregunta_10 = QLabel(self.checklist_page)
        self.pregunta_10.setObjectName(u"pregunta_10")

        self.gridLayout_4.addWidget(self.pregunta_10, 11, 0, 1, 1)

        self.radioButton_11 = QRadioButton(self.checklist_page)
        self.Q6.addButton(self.radioButton_11)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setMaximumSize(QSize(100, 35))
        self.radioButton_11.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_11, 7, 1, 1, 1)

        self.radioButton_38 = QRadioButton(self.checklist_page)
        self.Q7.addButton(self.radioButton_38)
        self.radioButton_38.setObjectName(u"radioButton_38")
        self.radioButton_38.setMaximumSize(QSize(100, 35))
        self.radioButton_38.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_38, 8, 3, 1, 1)

        self.pregunta_5 = QLabel(self.checklist_page)
        self.pregunta_5.setObjectName(u"pregunta_5")

        self.gridLayout_4.addWidget(self.pregunta_5, 6, 0, 1, 1)

        self.radioButton_4 = QRadioButton(self.checklist_page)
        self.Q2.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setMaximumSize(QSize(100, 35))
        self.radioButton_4.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_4, 1, 3, 1, 1)

        self.radioButton_23 = QRadioButton(self.checklist_page)
        self.Q5.addButton(self.radioButton_23)
        self.radioButton_23.setObjectName(u"radioButton_23")
        self.radioButton_23.setMaximumSize(QSize(100, 35))
        self.radioButton_23.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(130, 94, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_23, 6, 2, 1, 1)

        self.radioButton_17 = QRadioButton(self.checklist_page)
        self.Q12.addButton(self.radioButton_17)
        self.radioButton_17.setObjectName(u"radioButton_17")
        self.radioButton_17.setMaximumSize(QSize(100, 35))
        self.radioButton_17.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_17, 13, 1, 1, 1)

        self.radioButton_13 = QRadioButton(self.checklist_page)
        self.Q8.addButton(self.radioButton_13)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setMaximumSize(QSize(100, 35))
        self.radioButton_13.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(98, 130, 94);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}")

        self.gridLayout_4.addWidget(self.radioButton_13, 9, 1, 1, 1)

        self.pregunta_11 = QLabel(self.checklist_page)
        self.pregunta_11.setObjectName(u"pregunta_11")

        self.gridLayout_4.addWidget(self.pregunta_11, 12, 0, 1, 1)

        self.horometro_btn = QPushButton(self.checklist_page)
        self.horometro_btn.setObjectName(u"horometro_btn")
        self.horometro_btn.setMaximumSize(QSize(100, 35))

        self.gridLayout_4.addWidget(self.horometro_btn, 17, 3, 1, 1)

        self.stackedWidget.addWidget(self.checklist_page)
        self.horometro_page = QWidget()
        self.horometro_page.setObjectName(u"horometro_page")
        self.gridLayout_2 = QGridLayout(self.horometro_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_5 = QFrame(self.horometro_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.h_5 = QPushButton(self.frame_5)
        self.h_5.setObjectName(u"h_5")
        self.h_5.setMinimumSize(QSize(90, 66))
        self.h_5.setMaximumSize(QSize(90, 66))

        self.gridLayout.addWidget(self.h_5, 3, 2, 1, 1)

        self.h_4 = QPushButton(self.frame_5)
        self.h_4.setObjectName(u"h_4")
        self.h_4.setMinimumSize(QSize(90, 66))
        self.h_4.setMaximumSize(QSize(90, 66))

        self.gridLayout.addWidget(self.h_4, 3, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.h_9 = QPushButton(self.frame_5)
        self.h_9.setObjectName(u"h_9")
        self.h_9.setMinimumSize(QSize(90, 66))
        self.h_9.setMaximumSize(QSize(90, 66))

        self.gridLayout.addWidget(self.h_9, 4, 3, 1, 1)

        self.h_3 = QPushButton(self.frame_5)
        self.h_3.setObjectName(u"h_3")
        self.h_3.setMinimumSize(QSize(90, 66))
        self.h_3.setMaximumSize(QSize(90, 66))

        self.gridLayout.addWidget(self.h_3, 2, 3, 1, 1)

        self.h_7 = QPushButton(self.frame_5)
        self.h_7.setObjectName(u"h_7")
        self.h_7.setMinimumSize(QSize(90, 66))
        self.h_7.setMaximumSize(QSize(90, 66))

        self.gridLayout.addWidget(self.h_7, 4, 1, 1, 1)

        self.h_8 = QPushButton(self.frame_5)
        self.h_8.setObjectName(u"h_8")
        self.h_8.setMinimumSize(QSize(90, 66))
        self.h_8.setMaximumSize(QSize(90, 66))

        self.gridLayout.addWidget(self.h_8, 4, 2, 1, 1)

        self.h_1 = QPushButton(self.frame_5)
        self.h_1.setObjectName(u"h_1")
        self.h_1.setMinimumSize(QSize(90, 66))
        self.h_1.setMaximumSize(QSize(90, 66))

        self.gridLayout.addWidget(self.h_1, 2, 1, 1, 1)

        self.h_0 = QPushButton(self.frame_5)
        self.h_0.setObjectName(u"h_0")
        self.h_0.setMinimumSize(QSize(90, 66))
        self.h_0.setMaximumSize(QSize(90, 66))

        self.gridLayout.addWidget(self.h_0, 5, 1, 1, 1)

        self.haceptar_btn = QPushButton(self.frame_5)
        self.haceptar_btn.setObjectName(u"haceptar_btn")
        self.haceptar_btn.setMinimumSize(QSize(284, 66))
        self.haceptar_btn.setMaximumSize(QSize(284, 66))

        self.gridLayout.addWidget(self.haceptar_btn, 6, 1, 1, 3)

        self.hborrar_btn = QPushButton(self.frame_5)
        self.hborrar_btn.setObjectName(u"hborrar_btn")
        self.hborrar_btn.setMinimumSize(QSize(188, 66))
        self.hborrar_btn.setMaximumSize(QSize(188, 66))

        self.gridLayout.addWidget(self.hborrar_btn, 5, 2, 1, 2)

        self.horometro_tbx = QLineEdit(self.frame_5)
        self.horometro_tbx.setObjectName(u"horometro_tbx")
        self.horometro_tbx.setMinimumSize(QSize(284, 66))
        self.horometro_tbx.setMaximumSize(QSize(284, 66))

        self.gridLayout.addWidget(self.horometro_tbx, 1, 1, 1, 3)

        self.h_2 = QPushButton(self.frame_5)
        self.h_2.setObjectName(u"h_2")
        self.h_2.setMinimumSize(QSize(90, 66))
        self.h_2.setMaximumSize(QSize(90, 66))

        self.gridLayout.addWidget(self.h_2, 2, 2, 1, 1)

        self.h_6 = QPushButton(self.frame_5)
        self.h_6.setObjectName(u"h_6")
        self.h_6.setMinimumSize(QSize(90, 66))
        self.h_6.setMaximumSize(QSize(90, 66))

        self.gridLayout.addWidget(self.h_6, 3, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_6, 7, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 4, 1, 1)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 7, 4, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout)


        self.gridLayout_2.addWidget(self.frame_5, 1, 0, 1, 1)

        self.label_3 = QLabel(self.horometro_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.horometro_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy1.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy1)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.bateria_lbl = QLabel(self.bottomBar)
        self.bateria_lbl.setObjectName(u"bateria_lbl")

        self.horizontalLayout_5.addWidget(self.bateria_lbl)

        self.conexion_lbl = QLabel(self.bottomBar)
        self.conexion_lbl.setObjectName(u"conexion_lbl")

        self.horizontalLayout_5.addWidget(self.conexion_lbl)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Kanpy - new kanvan - python project", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.monitores_btn.setText(QCoreApplication.translate("MainWindow", u"Monitores", None))
        self.motrec_btn.setText(QCoreApplication.translate("MainWindow", u"MOTREC", None))
        self.nombre_lbl.setText("")
        self.photo_lbl.setText("")
        self.empleado_lbl.setText(QCoreApplication.translate("MainWindow", u"EMPLEADO:", None))
        self.num_btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.num_btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.num_btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.num_btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.num_btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.borrar_btn.setText(QCoreApplication.translate("MainWindow", u"BORRAR", None))
        self.num_btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.aceptar_btn.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
        self.num_btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.num_btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.num_btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.num_btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.monitorI_lbl.setText("")
        self.monitor_lbl.setText(QCoreApplication.translate("MainWindow", u"MONITORES:", None))
        self.checklist_btn.setText(QCoreApplication.translate("MainWindow", u"Checklist", None))
        self.radioButton_41.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.radioButton_33.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.radioButton_43.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.radioButton_21.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.pregunta_2.setText("")
        self.pregunta_13.setText("")
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.radioButton_29.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.radioButton_27.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.pregunta_8.setText("")
        self.pregunta_15.setText("")
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.radioButton_45.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.radioButton_39.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.radioButton_26.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pregunta_1.setText("")
        self.radioButton_25.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.radioButton_34.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.radioButton_28.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.radioButton_15.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.radioButton_42.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.radioButton_35.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.radioButton_24.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.radioButton_22.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.radioButton_30.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.radioButton_37.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.radioButton_20.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pregunta_4.setText("")
        self.pregunta_12.setText("")
        self.radioButton_14.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.radioButton_19.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.radioButton_44.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.pregunta_9.setText("")
        self.radioButton_16.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.radioButton_18.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pregunta_6.setText("")
        self.pregunta_14.setText("")
        self.radioButton_31.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.radioButton_40.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.radioButton_32.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.radioButton_46.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.pregunta_7.setText("")
        self.radioButton_36.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.pregunta_3.setText("")
        self.pregunta_10.setText("")
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.radioButton_38.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.pregunta_5.setText("")
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.radioButton_23.setText(QCoreApplication.translate("MainWindow", u"NOK", None))
        self.radioButton_17.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pregunta_11.setText("")
        self.horometro_btn.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.h_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.h_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.h_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.h_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.h_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.h_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.h_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.h_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.haceptar_btn.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
        self.hborrar_btn.setText(QCoreApplication.translate("MainWindow", u"BORRAR", None))
        self.h_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.h_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"HOROMETRO:", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: IT Systems", None))
        self.bateria_lbl.setText("")
        self.conexion_lbl.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

