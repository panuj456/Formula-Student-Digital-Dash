'''TO NICK, I need to learn how to do threading potentially for this to work, so this no work'''
import sys
import OOreceive as rec
import CANpyqt5displays as dis

def main(CAN_line):
	msg = CAN_line.update_CAN()
	print(msg)
	if msg.arbitration_id == 0x360:
		full_msg = CAN_line.get_0x360()
		for item in full_msg:
			data = item[0]
			channel = item[1]
			window.set_labelValue(data,channel)
			print("0x360 works")
	
	if msg.arbitration_id == 0x361:
		full_msg = CAN_line.get_0x361()
		for item in full_msg:
			data = item[0]
			channel = item[1]
			window.set_labelValue(data,channel)
			print("0x361 works")
	
	if msg.arbitration_id == 0x370:
		full_msg = CAN_line.get_0x370()
		for item in full_msg:
			data = item[0]
			channel = item[1]
			window.set_labelValue(data,channel)
			print("0x370 works")
	
	if msg.arbitration_id == 0x372:
		full_msg = CAN_line.get_0x372()
		for item in full_msg:
			data = item[0]
			channel = item[1]
			window.set_labelValue(data,channel)
			print("0x372 works")

	if msg.arbitration_id == 0x3E0:
		full_msg = CAN_line.get_0x3E0()
		for item in full_msg:
			data = item[0]
			channel = item[1]
			window.set_labelValue(data,channel)
			print("0x3E0 works")
	
	if msg.arbitration_id == 0x3E2:
		full_msg = CAN_line.get_0x3E2()
		for item in full_msg:
			data = item[0]
			channel = item[1]
			window.set_labelValue(data,channel)
			print("0x3E2 works")
	
	if msg.arbitration_id == 0x470:
		full_msg = CAN_line.get_0x470()
		for item in full_msg:
			data = item[0]
			channel = item[1]
			window.set_labelValue(data,channel)
			print("0x470 works")

	if msg.arbitration_id == 0x471:
		full_msg = CAN_line.get_0x471()
		for item in full_msg:
			data = item[0]
			channel = item[1]
			window.set_labelValue(data,channel)
			print("0x471 works")
	
	if msg.arbitration_id == 0x476:
		full_msg = CAN_line.get_0x476()
		for item in full_msg:
			data = item[0]
			channel = item[1]
			window.set_labelValue(data,channel)
			print("0x476 works")
	
	#window.display_update()		
	print("penis")
	

	#while loop with Qtimer or counter and update labels 
	'''lst_0x360 = rec.CAN_Comms.get_0x360()
	for item in lst_0x360:
		data_pos = 0
		channel_pos = 1
	'''
		#concatenate strings into one data or separate and create another pyQT thing
		#pass
	#lst_0x360 = "TPS"

	
# -----------------Solution Threading ----------#
'''Problem here is that values will update on pyqt app window
but will stop the process of CAN dumping at the same time, so every
'x' press is equivalent to allowing a new message/loop to occur, thus new change in labels
so label changing works just a) order of code was incorrect b) app.exec is an issue.
I need a way of enabling main(CAN_line) to constantly run i.e. the while loop, without needing app.exec to run.
Can be solved via QTimer, Threading (beyond my scope rn), or making the system sleep or use '''
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
		window.show()


