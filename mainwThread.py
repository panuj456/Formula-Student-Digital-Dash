'''TO NICK, I need to learn how to do threading potentially for this to work, so this no work'''
import followup
from PySide6 import QtWidgets
from PySide6 import QtCore 
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import QThread, Signal, QObject, Slot, Qt, QTimer

import sys
import OOrecivewThread as rec
import CANpyqt5displayswThread as dis
# write code as update screen every button click then use qtimer to instigate a "button click" every single second

class Ui(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		layout = QVBoxLayout()
		self.setLayout(layout)
		self.setWindowTitle("My App")
		self.setGeometry(0, 0, 480, 320) 
		#widget = QLabel(self.text)
		#font = widget.font()
		#font.setPointSize(10)
		#widget.setFont(font)
		#widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		#self.setCentralWidget(widget)

		self.followup_start_button = QPushButton("Start FollowUp (Green)")
		layout.addWidget(self.followup_start_button)

		#------update GUI code-----#
		self.i = 0
		default = "N/A"
		# add QLabel
		#self.qLbl = QLabel('Not yet initialized')
		#self.setCentralWidget(self.qLbl)
		self.qLbl_RPM = QLabel(default,self)
		self.qLbl_RPM.move(300,0)
		self.qLbl_RPM_txt = QLabel("RPM : ",self)
		self.qLbl_RPM_txt.move(10,0)
		self.qLbl_ManifoldPressure = QLabel(default,self)
		self.qLbl_ManifoldPressure.move(300,25)
		self.qLbl_ManifoldPressure_txt = QLabel("Manifold Pressure (kPa) : ",self)
		self.qLbl_ManifoldPressure_txt.move(10,25)
		self.qLbl_TPS = QLabel(default,self) #Throttle Position
		self.qLbl_TPS.move(300,50)
		self.qLbl_TPS_txt = QLabel("Throttle Position (%) : ",self)
		self.qLbl_TPS_txt.move(10,50)
		self.qLbl_FuelPressure = QLabel(default,self)
		self.qLbl_FuelPressure.move(300,75)
		self.qLbl_FuelPressure_txt = QLabel("Fuel Pressure : ",self)
		self.qLbl_FuelPressure_txt.move(10,75)
		self.qLbl_VehicleSpeed = QLabel(default,self)
		self.qLbl_VehicleSpeed.move(300,100)
		self.qLbl_VehicleSpeed_txt = QLabel("Speed (km/h) : ",self)
		self.qLbl_VehicleSpeed_txt.move(10,100)
		self.qLbl_Voltage = QLabel(default,self)
		self.qLbl_Voltage.move(300,125)
		self.qLbl_Voltage_txt = QLabel("Voltage : ",self)
		self.qLbl_Voltage_txt.move(10,125)
		self.qLbl_CoolantTemp = QLabel(default,self)
		self.qLbl_CoolantTemp.move(300,150)
		self.qLbl_CoolantTemp_txt = QLabel("Coolant Temp : ",self)
		self.qLbl_CoolantTemp_txt.move(10,150)
		self.qLbl_AirTemp = QLabel(default,self)
		self.qLbl_AirTemp.move(300,175)
		self.qLbl_AirTemp_txt = QLabel("Air Temp : ",self)
		self.qLbl_AirTemp_txt.move(10,175)
		self.qLbl_FuelTemp = QLabel(default,self) #anything with oil/fuel has oil/fuel
		self.qLbl_FuelTemp.move(300,200)
		self.qLbl_FuelTemp_txt = QLabel("Fuel Temp : ",self)
		self.qLbl_FuelTemp_txt.move(10,200)
		self.qLbl_GearSelePos = QLabel(default,self) #Gear Selector Position
		self.qLbl_GearSelePos.move(300,225)
		self.qLbl_GearSelePos_txt = QLabel("Gear Selection Pos : ",self)
		self.qLbl_GearSelePos_txt.move(10,225)
		self.qLbl_Gear = QLabel(default,self)
		self.qLbl_Gear.move(300,250)
		self.qLbl_Gear_txt = QLabel("Gear : ",self)
		self.qLbl_Gear_txt.move(10,250)

		self.followup_start_button = QPushButton("Start FollowUp (Green)")
		layout.addWidget(self.followup_start_button)


class MainWindow(QMainWindow):
	def __init__(self, CAN_line):
		super(MainWindow, self).__init__()
		#self.text = text
		self.CAN_line = CAN_line


		self.ui = Ui()
		self.show()

		# Define timer.
		self.timer1 = QTimer()
		self.timer1.setInterval(1000)  # msecs 100 = 1/10th sec
		self.timer1.timeout.connect(self.ui.followup_start_button.clicked)
		self.timer1.start() 

		# --------------------------------------------
        # threading module (green)
        # --------------------------------------------

		self.update_screen = rec.update_screen()
		self.update_screen.setgreen.connect(lambda: print("connected green"))
		self.update_screen.setgreen.connect(self.p1_followup_button_color_green)

        # Starts the initialize function in followup.py which calls the Change_green class above
        #
        # After creating the Change_green instance, we initialize the thread
        # from another file here, and pass the instance to the thread, so it
        # can access it from there. 
		self.threads = followup.Threads(self.Change_green)
		self.followup_start_button = self.ui.followup_start_button #focal point/thing that changes colour
		self.followup_start_button.clicked.connect(self.threads.thread_launch_followup_initialize)

		msg = self.CAN_line.update_CAN()
		print(msg)
		CAN_line.check_CAN(msg, window)
        


	def set_labelValue(self,data,channel):
		if channel == 'Manifold Pressure (kPa)':
			self.ui.qLbl_ManifoldPressure.setText(str(data))
		if channel == 'RPM':
			self.ui.qLbl_RPM.setText(str(data))
		if channel == 'Throttle Position (%)':
			self.qLbl_TPS.setText(str(data))
		if channel == 'Voltage (V)':
			self.ui.qLbl_Voltage.setText(str(data))
			#self.qLbl_Voltage.update()
			#self.qLbl_Voltage.repaint()
		if channel == 'Vehicle Speed (km/h)':
			self.ui.qLbl_VehicleSpeed.setText(str(data))
		if channel == 'Fuel Pressure (kPa)':
			self.ui.qLbl_FuelPressure.setText(str(data))
		if channel == 'Coolant Temperature (K)':
			self.qLbl_CoolantTemp.setText(str(data))
		if channel == 'Air Temperature (K)':
			self.ui.qLbl_AirTemp.setText(str(data))
		if channel == 'Fuel Temperature (K)':
			self.ui.qLbl_FuelTemp.setText(str(data))
		if channel == 'Gear Selector Position (enum)':
			self.ui.qLbl_GearSelePos.setText(str(data))
		if channel == 'Gear - Can be cobined with selector pos (enum)':
			self.ui.qLbl_Gear.setText(str(data))
	
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
	app = dis.QApplication(dis.sys.argv)
	window = dis.MainWindow(CAN_line)
	window.show()
	app.exec() #problem lies here
	


