# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VideoPlayer(object):
    def setupUi(self, VideoPlayer):
        VideoPlayer.setObjectName("VideoPlayer")
        VideoPlayer.resize(800, 605)
        self.centralwidget = QtWidgets.QWidget(VideoPlayer)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 160, 541, 241))
        self.label.setMinimumSize(QtCore.QSize(0, 221))
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap("C:/Users/SalmanTrader/OneDrive/Pictures/CS Logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.rdbtnSort = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbtnSort.setGeometry(QtCore.QRect(270, 120, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rdbtnSort.setFont(font)
        self.rdbtnSort.setStyleSheet("QLabel {\n"
"        color: white;\n"
"        background-color: rgba(52, 73, 94, 200);  /* Semi-transparent background color */\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        border: 1px solid rgba(0, 0, 0, 50);  /* Semi-transparent border */\n"
"        box-shadow: 2px 2px 5px rgba(0, 0, 0, 50);  /* Shadow effect */\n"
"    }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("webcam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rdbtnSort.setIcon(icon)
        self.rdbtnSort.setObjectName("rdbtnSort")
        self.MainHeadinglbl = QtWidgets.QLabel(self.centralwidget)
        self.MainHeadinglbl.setGeometry(QtCore.QRect(300, 0, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.MainHeadinglbl.setFont(font)
        self.MainHeadinglbl.setStyleSheet("QLabel {\n"
"        color: white;\n"
"        background-color: rgba(52, 73, 94, 200);  /* Semi-transparent background color */\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        border: 1px solid rgba(0, 0, 0, 50);  /* Semi-transparent border */\n"
"        box-shadow: 2px 2px 5px rgba(0, 0, 0, 50);  /* Shadow effect */\n"
"    }")
        self.MainHeadinglbl.setObjectName("MainHeadinglbl")
        self.btnBrowse_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse_2.setGeometry(QtCore.QRect(270, 70, 111, 31))
        self.btnBrowse_2.setStyleSheet("QPushButton {\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"            stop:0 rgba(231, 76, 60, 255), stop:1 rgba(192, 57, 43, 255));\n"
"        border: 1px solid #c0392b;\n"
"        color: white;\n"
"        padding: 10px 20px;\n"
"        border-radius: 5px;\n"
"        icon-size: 32px;  /* Adjust the icon size as needed */\n"
"        icon-color: white;  /* Set the icon color */\n"
"        icon-alignment: center;  /* Center the icon */\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"            stop:0 rgba(192, 57, 43, 255), stop:1 rgba(231, 76, 60, 255));\n"
"        border: 1px solid #e74c3c;\n"
"        color: white;\n"
"        padding: 10px 20px;\n"
"        border-radius: 5px;\n"
"        box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.3);\n"
"    }\n"
"    \n"
"    QPushButton:pressed {\n"
"        background-color: rgba(192, 57, 43, 255);\n"
"        border: 1px solid #c0392b;\n"
"        color: white;\n"
"        padding: 10px 20px;\n"
"        border-radius: 5px;\n"
"    }")
        self.btnBrowse_2.setFlat(False)
        self.btnBrowse_2.setObjectName("btnBrowse_2")
        self.Speedlbl = QtWidgets.QLabel(self.centralwidget)
        self.Speedlbl.setGeometry(QtCore.QRect(70, 430, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Speedlbl.setFont(font)
        self.Speedlbl.setStyleSheet("QLabel {\n"
"        color: white;\n"
"        background-color: rgba(52, 73, 94, 200);  /* Semi-transparent background color */\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        border: 1px solid rgba(0, 0, 0, 50);  /* Semi-transparent border */\n"
"        box-shadow: 2px 2px 5px rgba(0, 0, 0, 50);  /* Shadow effect */\n"
"    }")
        self.Speedlbl.setObjectName("Speedlbl")
        self.availableCameras = QtWidgets.QComboBox(self.centralwidget)
        self.availableCameras.setGeometry(QtCore.QRect(630, 80, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.availableCameras.setFont(font)
        self.availableCameras.setObjectName("availableCameras")
        self.availableFilters = QtWidgets.QComboBox(self.centralwidget)
        self.availableFilters.setGeometry(QtCore.QRect(630, 420, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.availableFilters.setFont(font)
        self.availableFilters.setObjectName("availableFilters")
        self.Speedslider = QtWidgets.QSlider(self.centralwidget)
        self.Speedslider.setGeometry(QtCore.QRect(150, 430, 160, 22))
        self.Speedslider.setMinimumSize(QtCore.QSize(160, 0))
        self.Speedslider.setMaximumSize(QtCore.QSize(160, 22))
        self.Speedslider.setStyleSheet("QLabel {\n"
"        color: white;\n"
"        background-color: rgba(52, 73, 94, 200);  /* Semi-transparent background color */\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        border: 1px solid rgba(0, 0, 0, 50);  /* Semi-transparent border */\n"
"        box-shadow: 2px 2px 5px rgba(0, 0, 0, 50);  /* Shadow effect */\n"
"    }")
        self.Speedslider.setMinimum(-2)
        self.Speedslider.setMaximum(2)
        self.Speedslider.setPageStep(1)
        self.Speedslider.setOrientation(QtCore.Qt.Horizontal)
        self.Speedslider.setObjectName("Speedslider")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(640, 170, 22, 211))
        self.verticalSlider.setStyleSheet("QLabel {\n"
"        color: white;\n"
"        background-color: rgba(52, 73, 94, 200);  /* Semi-transparent background color */\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        border: 1px solid rgba(0, 0, 0, 50);  /* Semi-transparent border */\n"
"        box-shadow: 2px 2px 5px rgba(0, 0, 0, 50);  /* Shadow effect */\n"
"    }")
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.Speedlbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.Speedlbl_2.setGeometry(QtCore.QRect(670, 250, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Speedlbl_2.setFont(font)
        self.Speedlbl_2.setStyleSheet("QLabel {\n"
"        color: white;\n"
"        background-color: rgba(52, 73, 94, 200);  /* Semi-transparent background color */\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        border: 1px solid rgba(0, 0, 0, 50);  /* Semi-transparent border */\n"
"        box-shadow: 2px 2px 5px rgba(0, 0, 0, 50);  /* Shadow effect */\n"
"    }")
        self.Speedlbl_2.setObjectName("Speedlbl_2")
        self.lblDataSource_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblDataSource_2.setGeometry(QtCore.QRect(490, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblDataSource_2.setFont(font)
        self.lblDataSource_2.setStyleSheet("QLabel {\n"
"        color: white;\n"
"        background-color: rgba(52, 73, 94, 200);  /* Semi-transparent background color */\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        border: 1px solid rgba(0, 0, 0, 50);  /* Semi-transparent border */\n"
"        box-shadow: 2px 2px 5px rgba(0, 0, 0, 50);  /* Shadow effect */\n"
"    }")
        self.lblDataSource_2.setObjectName("lblDataSource_2")
        self.btnRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.btnRefresh.setGeometry(QtCore.QRect(520, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnRefresh.setFont(font)
        self.btnRefresh.setStyleSheet("QPushButton {\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"            stop:0 rgba(39, 174, 96, 255), stop:1 rgba(46, 204, 113, 255));\n"
"        border: 1px solid #27ae60;\n"
"        color: white;\n"
"        padding: 8px 16px;\n"
"        border-radius: 5px;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"            stop:0 rgba(22, 160, 133, 255), stop:1 rgba(39, 174, 96, 255));\n"
"        border: 1px solid #2ecc71;\n"
"        color: white;\n"
"        padding: 8px 16px;\n"
"        border-radius: 5px;\n"
"        box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.3);\n"
"    }\n"
"    \n"
"    QPushButton:pressed {\n"
"        background-color: rgba(39, 174, 96, 255);\n"
"        border: 1px solid #27ae60;\n"
"        color: white;\n"
"        padding: 8px 16px;\n"
"        border-radius: 5px;\n"
"    }")
        self.btnRefresh.setAutoDefault(True)
        self.btnRefresh.setObjectName("btnRefresh")
        self.lblDataSource = QtWidgets.QLabel(self.centralwidget)
        self.lblDataSource.setGeometry(QtCore.QRect(40, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblDataSource.setFont(font)
        self.lblDataSource.setStyleSheet("QLabel {\n"
"        color: white;\n"
"        background-color: rgba(52, 73, 94, 200);  /* Semi-transparent background color */\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        border: 1px solid rgba(0, 0, 0, 50);  /* Semi-transparent border */\n"
"        box-shadow: 2px 2px 5px rgba(0, 0, 0, 50);  /* Shadow effect */\n"
"    }")
        self.lblDataSource.setObjectName("lblDataSource")
        self.lblDataSource_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblDataSource_3.setGeometry(QtCore.QRect(560, 420, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblDataSource_3.setFont(font)
        self.lblDataSource_3.setStyleSheet("QLabel {\n"
"        color: white;\n"
"        background-color: rgba(52, 73, 94, 200);  /* Semi-transparent background color */\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        border: 1px solid rgba(0, 0, 0, 50);  /* Semi-transparent border */\n"
"        box-shadow: 2px 2px 5px rgba(0, 0, 0, 50);  /* Shadow effect */\n"
"    }")
        self.lblDataSource_3.setObjectName("lblDataSource_3")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setGeometry(QtCore.QRect(180, 70, 81, 31))
        self.btnBrowse.setStyleSheet("QPushButton {\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"            stop:0 rgba(255, 168, 0, 255), stop:1 rgba(255, 87, 34, 255));\n"
"        border: 2px solid #d35400;\n"
"        color: white;\n"
"        padding: 8px 16px;\n"
"        border-radius: 10px;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"            stop:0 rgba(255, 138, 0, 255), stop:1 rgba(255, 71, 26, 255));\n"
"        border: 2px solid #d35400;\n"
"        color: white;\n"
"        padding: 8px 16px;\n"
"        border-radius: 10px;\n"
"        box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.3);\n"
"    }\n"
"    \n"
"    QPushButton:pressed {\n"
"        background-color: rgba(255, 87, 34, 255);\n"
"        border: 2px solid #d35400;\n"
"        color: white;\n"
"        padding: 8px 16px;\n"
"        border-radius: 10px;\n"
"    }")
        self.btnBrowse.setFlat(False)
        self.btnBrowse.setObjectName("btnBrowse")
        VideoPlayer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VideoPlayer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuVideo_Player = QtWidgets.QMenu(self.menubar)
        self.menuVideo_Player.setObjectName("menuVideo_Player")
        self.menuImage_Player = QtWidgets.QMenu(self.menubar)
        self.menuImage_Player.setObjectName("menuImage_Player")
        VideoPlayer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VideoPlayer)
        self.statusbar.setObjectName("statusbar")
        VideoPlayer.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuVideo_Player.menuAction())
        self.menubar.addAction(self.menuImage_Player.menuAction())

        self.retranslateUi(VideoPlayer)
        QtCore.QMetaObject.connectSlotsByName(VideoPlayer)

    def retranslateUi(self, VideoPlayer):
        _translate = QtCore.QCoreApplication.translate
        VideoPlayer.setWindowTitle(_translate("VideoPlayer", "VideoPlayer"))
        self.rdbtnSort.setText(_translate("VideoPlayer", "Webcam"))
        self.MainHeadinglbl.setText(_translate("VideoPlayer", "Video Player"))
        self.btnBrowse_2.setText(_translate("VideoPlayer", "Capture Video"))
        self.Speedlbl.setText(_translate("VideoPlayer", "Speed"))
        self.Speedlbl_2.setText(_translate("VideoPlayer", "Grey Scale"))
        self.lblDataSource_2.setText(_translate("VideoPlayer", "Select Camera"))
        self.btnRefresh.setText(_translate("VideoPlayer", "Clear Video"))
        self.lblDataSource.setText(_translate("VideoPlayer", "Import Video"))
        self.lblDataSource_3.setText(_translate("VideoPlayer", "Filters"))
        self.btnBrowse.setText(_translate("VideoPlayer", "Browse"))
        self.menuVideo_Player.setTitle(_translate("VideoPlayer", "Video Player"))
        self.menuImage_Player.setTitle(_translate("VideoPlayer", "Image Player"))