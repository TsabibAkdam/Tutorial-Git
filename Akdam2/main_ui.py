# Form implementation generated from reading ui file 'myprofile.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.labelNama = QtWidgets.QLabel(parent=Form)
        self.labelNama.setGeometry(QtCore.QRect(60, 150, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.labelNama.setFont(font)
        self.labelNama.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelNama.setObjectName("labelNama")
        self.labelDesk = QtWidgets.QLabel(parent=Form)
        self.labelDesk.setGeometry(QtCore.QRect(10, 190, 381, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.labelDesk.setFont(font)
        self.labelDesk.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDesk.setObjectName("labelDesk")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(140, 270, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gambar = QtWidgets.QLabel(parent=Form)
        self.gambar.setGeometry(QtCore.QRect(160, 10, 81, 131))
        self.gambar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.gambar.setText("")
        self.gambar.setPixmap(QtGui.QPixmap("D:/vscode/LTI/first_ui/my_profile.png"))
        self.gambar.setScaledContents(True)
        self.gambar.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gambar.setObjectName("gambar")
        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 220, 381, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Let\'s Connect and Explore! 🚀"))
        self.labelNama.setText(_translate("Form", "Nama : Tsabib Akdam Alkarny"))
        self.labelDesk.setText(_translate("Form", "Welcome to my profile! I am a lifelong learner who loves exploring new things."))
        self.label.setText(_translate("Form", "© 2024 Tsabib Akdam"))
        self.pushButton.setText(_translate("Form", "Instagram"))
        self.pushButton_2.setText(_translate("Form", "Youtube"))
        self.pushButton_3.setText(_translate("Form", "Tiktok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())