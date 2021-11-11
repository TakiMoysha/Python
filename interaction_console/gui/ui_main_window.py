from qt_core import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        # MainWindow.resize(605, 480)
        MainWindow.setMinimumSize(960, 540)

        self.centralwidget = QFrame(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStatusTip("Hello world!")
        MainWindow.setStatusBar(self.statusbar)

        self.actionHi_Mark = QAction(MainWindow)
        self.actionHi_Mark.setObjectName(u"actionHi_Mark")

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menuMenu_Bar = QMenu(self.menubar)
        self.menuMenu_Bar.setObjectName(u"menuMenu_Bar")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu_Bar.menuAction())
        self.menuMenu_Bar.addSeparator()
        self.menuMenu_Bar.addAction(self.actionHi_Mark)
        self.menuMenu_Bar.addSeparator()

        # Main Content
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.logoutBox = QTextBrowser()

        self.horizontalLayout = QHBoxLayout()
        self.commandInput = QTextEdit()
        self.insertCommandButton = QPushButton(text="Push")
        self.insertCommandButton.setMaximumSize(42, 42)
        self.horizontalLayout.addWidget(self.commandInput)
        self.horizontalLayout.addWidget(self.insertCommandButton)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.commandInput.setMaximumHeight(30)
        self.commandInput.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.logoutBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Final tasks
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionHi_Mark.setText(QCoreApplication.translate("MainWindow", u"Hi, Mark", None))
        self.menuMenu_Bar.setTitle(QCoreApplication.translate("MainWindow", u"Menu Bar", None))
    # retranslateUi

