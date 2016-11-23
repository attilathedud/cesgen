# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../designer/design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(425, 454)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(425, 454))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background: url(:/background/background.png)"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblCreation = QtGui.QLabel(self.centralwidget)
        self.lblCreation.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lblCreation.setStyleSheet(_fromUtf8("background: rgba(16, 255, 33, 127);\n"
"padding: 10px;\n"
"border-radius: 4px;"))
        self.lblCreation.setObjectName(_fromUtf8("lblCreation"))
        self.verticalLayout.addWidget(self.lblCreation)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.leProjectName = QtGui.QLineEdit(self.centralwidget)
        self.leProjectName.setObjectName(_fromUtf8("leProjectName"))
        self.verticalLayout_2.addWidget(self.leProjectName)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.leDirectory = QtGui.QLineEdit(self.centralwidget)
        self.leDirectory.setObjectName(_fromUtf8("leDirectory"))
        self.horizontalLayout.addWidget(self.leDirectory)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnDirectoryChoose = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDirectoryChoose.sizePolicy().hasHeightForWidth())
        self.btnDirectoryChoose.setSizePolicy(sizePolicy)
        self.btnDirectoryChoose.setStyleSheet(_fromUtf8("padding: 5px;"))
        self.btnDirectoryChoose.setObjectName(_fromUtf8("btnDirectoryChoose"))
        self.horizontalLayout.addWidget(self.btnDirectoryChoose)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leIncludeCssDirectory = QtGui.QLineEdit(self.centralwidget)
        self.leIncludeCssDirectory.setObjectName(_fromUtf8("leIncludeCssDirectory"))
        self.gridLayout.addWidget(self.leIncludeCssDirectory, 1, 1, 1, 1)
        self.chkIncludeOptions = QtGui.QCheckBox(self.centralwidget)
        self.chkIncludeOptions.setObjectName(_fromUtf8("chkIncludeOptions"))
        self.gridLayout.addWidget(self.chkIncludeOptions, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.chkIncludeBgScripts = QtGui.QCheckBox(self.centralwidget)
        self.chkIncludeBgScripts.setObjectName(_fromUtf8("chkIncludeBgScripts"))
        self.gridLayout.addWidget(self.chkIncludeBgScripts, 3, 0, 1, 1)
        self.chkIncludeImgs = QtGui.QCheckBox(self.centralwidget)
        self.chkIncludeImgs.setChecked(True)
        self.chkIncludeImgs.setObjectName(_fromUtf8("chkIncludeImgs"))
        self.gridLayout.addWidget(self.chkIncludeImgs, 2, 0, 1, 1)
        self.chkIncludeCss = QtGui.QCheckBox(self.centralwidget)
        self.chkIncludeCss.setChecked(True)
        self.chkIncludeCss.setObjectName(_fromUtf8("chkIncludeCss"))
        self.gridLayout.addWidget(self.chkIncludeCss, 1, 0, 1, 1)
        self.leIncludeImgsDirectory = QtGui.QLineEdit(self.centralwidget)
        self.leIncludeImgsDirectory.setObjectName(_fromUtf8("leIncludeImgsDirectory"))
        self.gridLayout.addWidget(self.leIncludeImgsDirectory, 2, 1, 1, 1)
        self.chkIncludeContentScripts = QtGui.QCheckBox(self.centralwidget)
        self.chkIncludeContentScripts.setObjectName(_fromUtf8("chkIncludeContentScripts"))
        self.gridLayout.addWidget(self.chkIncludeContentScripts, 3, 1, 1, 1)
        self.chkIncludeLayouts = QtGui.QCheckBox(self.centralwidget)
        self.chkIncludeLayouts.setObjectName(_fromUtf8("chkIncludeLayouts"))
        self.gridLayout.addWidget(self.chkIncludeLayouts, 4, 0, 1, 1)
        self.btnCssDirectoryChoose = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCssDirectoryChoose.sizePolicy().hasHeightForWidth())
        self.btnCssDirectoryChoose.setSizePolicy(sizePolicy)
        self.btnCssDirectoryChoose.setStyleSheet(_fromUtf8("padding: 5px;"))
        self.btnCssDirectoryChoose.setObjectName(_fromUtf8("btnCssDirectoryChoose"))
        self.gridLayout.addWidget(self.btnCssDirectoryChoose, 1, 2, 1, 1)
        self.btnImgDirectoryChoose = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnImgDirectoryChoose.sizePolicy().hasHeightForWidth())
        self.btnImgDirectoryChoose.setSizePolicy(sizePolicy)
        self.btnImgDirectoryChoose.setStyleSheet(_fromUtf8("padding: 5px;"))
        self.btnImgDirectoryChoose.setObjectName(_fromUtf8("btnImgDirectoryChoose"))
        self.gridLayout.addWidget(self.btnImgDirectoryChoose, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.chkPermStorage = QtGui.QCheckBox(self.centralwidget)
        self.chkPermStorage.setObjectName(_fromUtf8("chkPermStorage"))
        self.gridLayout_2.addWidget(self.chkPermStorage, 2, 0, 1, 1)
        self.chkPermContextMenus = QtGui.QCheckBox(self.centralwidget)
        self.chkPermContextMenus.setObjectName(_fromUtf8("chkPermContextMenus"))
        self.gridLayout_2.addWidget(self.chkPermContextMenus, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.chkPermNewTab = QtGui.QCheckBox(self.centralwidget)
        self.chkPermNewTab.setObjectName(_fromUtf8("chkPermNewTab"))
        self.gridLayout_2.addWidget(self.chkPermNewTab, 1, 0, 1, 1)
        self.chkPermNotifications = QtGui.QCheckBox(self.centralwidget)
        self.chkPermNotifications.setObjectName(_fromUtf8("chkPermNotifications"))
        self.gridLayout_2.addWidget(self.chkPermNotifications, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.btnGenerate = QtGui.QPushButton(self.centralwidget)
        self.btnGenerate.setStyleSheet(_fromUtf8("padding: 15px;"))
        self.btnGenerate.setObjectName(_fromUtf8("btnGenerate"))
        self.verticalLayout.addWidget(self.btnGenerate)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Chrome Extension Skeleton Generator", None))
        self.lblCreation.setText(_translate("MainWindow", "Skeleton Generated.", None))
        self.label_2.setText(_translate("MainWindow", "Name", None))
        self.label.setText(_translate("MainWindow", "Directory", None))
        self.btnDirectoryChoose.setText(_translate("MainWindow", "...", None))
        self.chkIncludeOptions.setText(_translate("MainWindow", "Include options pages", None))
        self.label_3.setText(_translate("MainWindow", "Directory of Files to Import", None))
        self.chkIncludeBgScripts.setText(_translate("MainWindow", "Include background scripts", None))
        self.chkIncludeImgs.setText(_translate("MainWindow", "Include imgs", None))
        self.chkIncludeCss.setText(_translate("MainWindow", "Include css", None))
        self.chkIncludeContentScripts.setText(_translate("MainWindow", "Include content-scripts", None))
        self.chkIncludeLayouts.setText(_translate("MainWindow", "Include layouts", None))
        self.btnCssDirectoryChoose.setText(_translate("MainWindow", "...", None))
        self.btnImgDirectoryChoose.setText(_translate("MainWindow", "...", None))
        self.chkPermStorage.setText(_translate("MainWindow", "Storage", None))
        self.chkPermContextMenus.setText(_translate("MainWindow", "Context Menus", None))
        self.label_4.setText(_translate("MainWindow", "Permissions", None))
        self.chkPermNewTab.setText(_translate("MainWindow", "New Tab", None))
        self.chkPermNotifications.setText(_translate("MainWindow", "Notifications", None))
        self.btnGenerate.setText(_translate("MainWindow", "Generate", None))

import design_resources
