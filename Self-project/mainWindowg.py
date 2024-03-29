# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 568)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 1100, 571))
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 571))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        self.treeWidget.setMinimumSize(QtCore.QSize(178, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(178, 571))
        self.treeWidget.setStyleSheet("background-color:#eeeeee;\n"
"border:outset;\n"
"color:#215b63;")
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.treeWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.treeWidget.setIndentation(25)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setObjectName("treeWidget")
        
        self.treeWidget.headerItem().setIcon(0, icon)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon1)
        item_0.setFlags(QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/images/paper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_1.setBackground(0, brush)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        '''
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setIcon(0, icon1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setIcon(0, icon1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setIcon(0, icon1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setIcon(0, icon1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        '''
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setDefaultSectionSize(91)
        self.content = QtWidgets.QWidget(self.splitter)
        self.content.setEnabled(True)
        self.content.setStyleSheet("background-color:#f4f9f4;\n"
"")
        self.content.setObjectName("content")
        self.label2 = QtWidgets.QLabel(self.content)
        self.label2.setGeometry(QtCore.QRect(290, 110, 301, 191))
        self.label2.setStyleSheet("border-image: url(:/newPrefix/images/welcome.png);")
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.label1 = QtWidgets.QLabel(self.content)
        self.label1.setGeometry(QtCore.QRect(330, 310, 221, 31))
        self.label1.setStyleSheet("font: 16pt \"隶书\";\n"
"color:#6ba083;")
        self.label1.setObjectName("label1")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.treeWidget.itemClicked['QTreeWidgetItem*','int'].connect(MainWindow.test)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HRD-Guy"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "HRD-Guy"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Mange my work"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Send invatation"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Team List"))
        #self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "Delete HR Guys"))
        #self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "Mange HR Guys"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "Update my info"))
        '''
       
        '''
        #self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label1.setText(_translate("MainWindow", "HRD-Guys"))

import img_rc
