import PyQt5 #pip install PyQt5
import sys

#27/11/24
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        #self.text = text
        self.setWindowTitle("Digital Dash")
        self.setGeometry(0, 0, 480, 320) 
        #widget = QLabel(self.text)
        #font = widget.font()
        #font.setPointSize(10)
        #widget.setFont(font)
        #widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        #self.setCentralWidget(widget)

        #------update GUI code-----#
        self.i = 0
        default = "N/A"
        # add QLabel
        #self.qLbl = QLabel('Not yet initialized')
        #self.setCentralWidget(self.qLbl

        self.setup_txt(default)
        
        '''
        self.timer = QTimer()  #from python guis tutorial on threading refer and adjust ltr
        self.timer.setInterval(1000)
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.recurring_timer, self.display_update)
        self.timer.start()
        '''
        
    def recurring_timer(self):  #from python guis tutorial on threading refer and adjust ltr
        self.counter +=1
        #self.l.setText("Counter: %d" % self.counter)
        '''
        # make QTimer
        self.qTimer = QTimer()
        # set interval to 1 s
        self.qTimer.setInterval(1000) # 1000 ms = 1 s
        # connect timeout signal to signal handler
        self.qTimer.timeout.connect(self.getSensorValue)
        # start timer
        self.qTimer.start()
        '''

    def setup_txt(self,default):
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
        self.show() #sets the main window to the screen size "https://stackoverflow.com/questions/41819082/updating-pyqt-label"
            

    def set_labelValue(self,data,channel):
        # function called in OOrecieve.py 
        if channel == 'Manifold Pressure (kPa)':
            self.qLbl_ManifoldPressure.setText(str(data))
        if channel == 'RPM':
            self.qLbl_RPM.setText(str(data))
        if channel == 'Throttle Position (%)':
            self.qLbl_TPS.setText(str(data))
        if channel == 'Voltage (V)':
            self.qLbl_Voltage.setText(str(data))
            self.qLbl_Voltage.update()
            self.qLbl_Voltage.repaint()
        if channel == 'Vehicle Speed (km/h)':
            self.qLbl_VehicleSpeed.setText(str(data))
        if channel == 'Fuel Pressure (kPa)':
            self.qLbl_FuelPressure.setText(str(data))
        if channel == 'Coolant Temperature (K)':
            self.qLbl_CoolantTemp.setText(str(data))
        if channel == 'Air Temperature (K)':
            self.qLbl_AirTemp.setText(str(data))
        if channel == 'Fuel Temperature (K)':
            self.qLbl_FuelTemp.setText(str(data))
        if channel == 'Gear Selector Position (enum)':
            self.qLbl_GearSelePos.setText(str(data))
        if channel == 'Gear - Can be cobined with selector pos (enum)':
            self.qLbl_Gear.setText(str(data))
    
    '''   
    def execute_this_fn(self):  #from python guis tutorial on threading refer and adjust ltr
        print("Hello!")

    def oh_no(self): #from python guis tutorial on threading refer and adjust ltr
        # Pass the function to execute
        worker = Worker(self.execute_this_fn) # Any other args, kwargs are passed to the run function

        # Execute
        self.threadpool.start(worker)
    '''        

    def display_update(self):
        self.show()
        #self.qLbl_Voltage.repaint() #not the problem
            
        #self.processEvents()
            

#design displays without specified values, only layouts and getting screen positioning correct, then in main, use the CAN data in form of parameters to make the gauages change to match CAN values
