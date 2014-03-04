import sys
from PySide import QtGui


app=QtGui.QApplication(sys.argv)

class VentanaBoton(QtGui.QDialog):
	def __init__(self):
		super(VentanaBoton, self).__init__()



		btn = QtGui.QPushButton(self)
		btn.setText("Presioname")
		btn.setGeometry(100,0, 100, 100)
		btn.clicked.connect(self.mensajear)


		btn2 = QtGui.QPushButton(self)
		btn2.setText("Presioname")
		btn2.setGeometry(100,110, 100, 100)
		btn2.clicked.connect(self.mensajear2)


		btn3 = QtGui.QPushButton(self)
		btn3.setText("Presioname")
		btn3.setGeometry(100,220, 100, 100)
		btn3.clicked.connect(self.mensajear3)

		btn4 = QtGui.QPushButton(self)
		btn4.setText("Presioname")
		btn4.setGeometry(100,330, 100, 100)
		btn4.clicked.connect(self.mensajear3)

		btn5 = QtGui.QPushButton(self)
		btn5.setText("Presioname")
		btn5.setGeometry(100,440, 100, 100)
		btn5.clicked.connect(self.mensajear3)



	def mensajear(self):
		print("Me presionaste")
		QtGui.QMessageBox.information(self, "Titulo", "informacion!!")

	def mensajear2(self):
		print("Me presionaste")
		QtGui.QMessageBox.information(self, "Titulo", "question!!")

	def mensajear3(self):
		print("Me presionaste")
		QtGui.QMessageBox.information(self, "Titulo", "information!")

	def mensajear4(self):
		print("Me presionaste")
		QtGui.QMessageBox.information(self, "Titulo", "warning!")

	def mensajear5(self):
		print("Me presionaste")
		QtGui.QMessageBox.information(self, "Titulo", "informacion!")







vent = VentanaBoton()
vent.show()

sys.exit(app.exec_())

