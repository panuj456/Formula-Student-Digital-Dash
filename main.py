import time
import sys
import OOreceive as rec
import CANpyqt5displays as dis
from PyQt5.QtCore import QTimer #QTimer
	
'''	
# Functioning Demonstration
app = dis.QApplication(dis.sys.argv)
window = dis.MainWindow()
CAN_line = rec.CAN_Comms(window)
msg = CAN_line.update_CAN()
CAN_line.main(CAN_line)  
flag = False
mainIterationNum = 0
while flag == False:
	#CAN_line.update_CAN()
	CAN_line.main(CAN_line)
	print("Main loop ", mainIterationNum, " complete") 
	
	window.display_update()
	app.exec() #problem lies here
	window.show()
	mainIterationNum += 1	
'''
	
#27-11-24 new code to test 'https://stackoverflow.com/questions/41819082/updating-pyqt-label'
def main():
	app = dis.QApplication(dis.sys.argv)
	window = dis.MainWindow()

	CAN_line = rec.CAN_Comms(window)
	msg = CAN_line.update_CAN()
	CAN_line.main(CAN_line)  
	flag = False
	mainIterationNum = 0

	timer = QTimer()
	#timer.timeout.connect(CAN_line.main(CAN_line))
	timer.setSingleShot(False)
	timer.start(1000)
	timer.timeout.connect(CAN_line.run)

	
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()


