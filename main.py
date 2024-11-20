import time
import sys
import OOreceive as rec
import CANpyqt5displays as dis


	#while loop with Qtimer or counter and update labels 
'''lst_0x360 = rec.CAN_Comms.get_0x360()
		for item in lst_0x360:
		data_pos = 0
		channel_pos = 1
	'''
		#concatenate strings into one data or separate and create another pyQT thing
		#pass
	#lst_0x360 = "TPS"

	
# -----------------Solution 1 ----------#
'''Problem here is that values will update on pyqt app window
but will stop the process of CAN dumping at the same time, so every
'x' press is equivalent to allowing a new message/loop to occur, thus new change in labels
so label changing works just a) order of code was incorrect b) app.exec is an issue.
I need a way of enabling main(CAN_line) to constantly run i.e. the while loop, without needing app.exec to run.
Can be solved via QTimer, Threading (beyond my scope rn), or making the system sleep or use '''
'''
if __name__ == '__main__':
	CAN_line = rec.CAN_Comms()
	msg = CAN_line.update_CAN()
	app = dis.QApplication(dis.sys.argv)
	window = dis.MainWindow() #can put app in here
	window = rec.main(CAN_line, window) #main returns window after label update loop
	window.display_update()
	
	flag = False
	while flag == False:
		window = rec.main(CAN_line)
		window.display_update()
		#app.exec() #problem lies here
		window.show()
		sys.exit(app.exec())
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
# -----------------Solution 2 ----------#
#this should just cause multiple opens and closes of the app window, but with updated values
if __name__ == '__main__':
	CAN_line = rec.CAN_Comms()
	msg = CAN_line.update_CAN()
	main(CAN_line)
	app = dis.QApplication(dis.sys.argv)
	window = dis.MainWindow()
	
	flag = False
	while flag == False:
		main(CAN_line)
		app.exec() #problem lies here
		time.sleep(0.5)
		window.show()
		sys.exit(app.exec_)
'''

'''
# -----------------Solution Last ----------#
#apparently this solution is apparently clapped, but should work
CAN_line = rec.CAN_Comms()
msg = CAN_line.update_CAN()
main(CAN_line)
app = dis.QApplication(dis.sys.argv)
window = dis.MainWindow()


flag = False
while flag == False:
	main(CAN_line)
	app.exec()	#problem lies here
	app = dis.QApplication.processEvents()
	time.sleep(1)
	window.show()
	#sys.exit(app) #uncomment this if not working
'''
