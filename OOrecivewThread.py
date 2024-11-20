import os
import can
import math
from functools import reduce
from PySide6.QtCore import QObject, QThread, Signal, Slot
import threading

def initialize(color): 
    print("initializing: ", color)
    color.green()
# To make the example simpler, I've put all threading scripts here on followup.py
class Threads:
    def __init__(self, color):
        self.color = color

    def thread_launch_followup_initialize(self):
        t1 = threading.Thread(target=initialize, args=[self.color])
        t1.start()

# Including this object here which will run in another thread.
#
# As I use PySide2 I changed
#   "pyqtSignal" -> "Signal"
#   "pyqtSlot"   -> "Slot"
class Change_green(QObject):
    setgreen = Signal()
    setred = Signal()

    @Slot()
    def green(self):
        self.setgreen.emit()
        print("clicked on green")



class CAN_Comms():

    def __init__(self):
        os.system('sudo ip link set can0 down')
        os.system('ifconfig')
        os.system('sudo ip link set can0 type can bitrate 1000000')
        os.system('sudo ifconfig can0 up')
        self.can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')# socketcan_native
        self.msg = self.can0.recv(10.0)

    def update_CAN(self):
        self.msg = self.can0.recv(10.0)
        return self.msg #then check msg arbritation in main the id

    def get_0x360(self):
        print("id: 0x360 Message data: ",list(self.msg.data))
        data_lst = []
        lst_0x360 = ['RPM', 'Manifold Pressure (kPa)', 'Throttle Position (%)', 'Coolant Pressure (kPa)']
        msgpos1 = 0
        msgpos2 = 1
        for channel in lst_0x360:
            bin_array = list(self.msg.data)
            out1 = "{0:b}".format(int(bin_array[msgpos1]))
            out2 = "{0:b}".format(int(bin_array[msgpos2]))
            bin_current_msg = str(out1)+str(out2)
            out = int(bin_current_msg, 2)
            #------raw data conversion------#
            if msgpos1 == 2 or msgpos1 == 4:
                out = out*0.1
            elif msgpos1 == 6:
                out = out*0.1 - 101.3 #raw data conversion (-101.3 for gauge pressure)
            temp = [out, channel]
            data_lst.append(temp) ####
            msgpos1 += 2
            msgpos2 += 2
        print("End of 0x360")
        return(data_lst)
    
    def get_0x361(self):
        print("id: 0x361 Message data: ",list(self.msg.data))
        data_lst = []
        lst_0x361 = ['Fuel Pressure (kPa)', 'Oil Pressure (kPa)', 'Engine Demand (%)', 'Wastegate Pressure (kPa)']
        msgpos1 = 0
        msgpos2 = 1
        for channel in lst_0x361:
            bin_array = list(self.msg.data)
            out1 = "{0:b}".format(int(bin_array[msgpos1]))
            out2 = "{0:b}".format(int(bin_array[msgpos2]))
            bin_current_msg = str(out1)+str(out2)
            out = int(bin_current_msg, 2)
            if msgpos1 == 4:
                out = out/10
            temp = [out, channel]
            data_lst.append(temp)
            msgpos1 += 2
            msgpos2 += 2
        print("End of 0x361")
        return(data_lst)
    
    def get_0x370(self):    
        print("id: 0x370 Message data: ",list(self.msg.data))
        data_lst = []
        lst_0x370 = ['Vehicle Speed (km/h)', ' Intake Cam Angle 1 (degree)', ' Intake Cam Angle 2 (degree)']
        msgpos1 = 0
        msgpos2 = 1
        for channel in lst_0x370:
            bin_array = list(self.msg.data)
            out1 = "{0:b}".format(int(bin_array[msgpos1]))
            out2 = "{0:b}".format(int(bin_array[msgpos2]))
            bin_current_msg = str(out1)+str(out2)
            out = int(bin_current_msg, 2)
            out = out/10 #raw data conversion
            temp = [out, channel]
            data_lst.append(temp)
            msgpos1 += 2
            msgpos2 += 2
        print("End of 0x370")
        return(data_lst)
    
    def get_0x372(self):
        print("id: 0x372 Message data: ",list(self.msg.data))
        data_lst = []
        lst_0x372 = ['Voltage (V)']
        msgpos1 = 0
        msgpos2 = 1
        for channel in lst_0x372:
            bin_array = list(self.msg.data)
            out1 = "{0:b}".format(int(bin_array[msgpos1]))
            out2 = "{0:b}".format(int(bin_array[msgpos2]))
            bin_current_msg = str(out1)+str(out2)
            out = int(bin_current_msg, 2)
            #------raw data conversion------#
            temp = [out*0.1, channel]
            data_lst.append(temp)
            msgpos1 += 2
            msgpos2 += 2
        print("End of 0x372")
        return(data_lst)

    def get_0x3E0(self):
        print("id: 0x3E0 Message data: ",list(self.msg.data))
        data_lst = []
        lst_0x3E0 = ['Coolant Temperature (K)', 'Air Temperature (K)', 'Fuel Temperature (K)', 'Oil Temperature (K)']
        msgpos1 = 0
        msgpos2 = 1
        for channel in lst_0x3E0:
            bin_array = list(self.msg.data)
            out1 = "{0:b}".format(int(bin_array[msgpos1]))
            out2 = "{0:b}".format(int(bin_array[msgpos2]))
            bin_current_msg = str(out1)+str(out2)
            out = int(bin_current_msg, 2)
            out = out/10 #raw data conversion
            temp = [out, channel]
            data_lst.append(temp)
            msgpos1 += 2
            msgpos2 += 2
        print("End of 0x3E0")
        return(data_lst)

    def get_0x3E2(self):
        print("id: 0x3E2 Message data: ",list(self.msg.data))
        data_lst = []
        lst_0x3E2 = ['Fuel Level (L)']
        msgpos1 = 0
        msgpos2 = 1
        for channel in lst_0x3E2:
            bin_array = list(self.msg.data)
            out1 = "{0:b}".format(int(bin_array[msgpos1]))
            out2 = "{0:b}".format(int(bin_array[msgpos2]))
            bin_current_msg = str(out1)+str(out2)
            out = int(bin_current_msg, 2)
            out = out/10 #raw data conversion
            temp = [out, channel]
            data_lst.append(temp)
            msgpos1 += 2
            msgpos2 += 2
        print("End of 0x3E2")
        return(data_lst)

    def get_0x470(self):
        print("id: 0x470 Message data: ",list(self.msg.data))
        data_lst = []
        lst_0x470 = ['Gear Selector Position (enum)', 'Gear - Can be cobined with selector pos (enum)']
        msgpos = 6
        for channel in lst_0x470:
            bin_array = list(self.msg.data)
            out1 = "{0:b}".format(int(bin_array[msgpos]))
            bin_current_msg = str(out1)
            out = int(bin_current_msg, 2)
            #out = out/10 #raw data conversion says Haltech Special Values on protocol info
            temp = [out, channel]
            data_lst.append(temp)
            msgpos += 1
            #msgpos2 += 2
        print("End of 0x470")
        return(data_lst)

    def get_0x471(self):
        print("id: 0x471 Message data: ",list(self.msg.data))
        data_lst = []
        lst_0x471 = ['Injection Pressure Differential (kPa)', 'Accelerator Pedal Position (%)', 'Exhaust Manifold Pressure (kPa)']
        msgpos1 = 0
        msgpos2 = 1
        for channel in lst_0x471:
            bin_array = list(self.msg.data)
            out1 = "{0:b}".format(int(bin_array[msgpos1]))
            out2 = "{0:b}".format(int(bin_array[msgpos2]))
            bin_current_msg = str(out1)+str(out2)
            out = int(bin_current_msg, 2)
            out = out/10 #raw data conversion
            temp = [out, channel]
            data_lst.append(temp)
            msgpos1 += 2
            msgpos2 += 2
        print("End of 0x471")
        return(data_lst)

    def get_0x476(self):
        print("id: 0x476 Message data: ",list(self.msg.data))
        data_lst = []
        lst_0x476 = ['Brake Pressure Rear (kPa)', 'Brake Pressure Front Ratio (%)', 'Brake Pressure Rear Ratio (%)', 'Brake Pressure Difference (kPa)']
        msgpos1 = 0
        msgpos2 = 1
        for channel in lst_0x476:
            bin_array = list(self.msg.data)
            out1 = "{0:b}".format(int(bin_array[msgpos1]))
            out2 = "{0:b}".format(int(bin_array[msgpos2]))
            bin_current_msg = str(out1)+str(out2)
            out = int(bin_current_msg, 2)
            out = out/10 #raw data conversion
            temp = [out, channel]
            data_lst.append(temp)
            msgpos1 += 2
            msgpos2 += 2
        print("End of 0x476")
        return(data_lst)
    
    def check_CAN(self, msg, window):
        if msg.arbitration_id == 0x360:
            full_msg = self.get_0x360()
            for item in full_msg:
                data = item[0]
                channel = item[1]
                window.set_labelValue(data,channel)
                print("0x360 works")
	
        if msg.arbitration_id == 0x361:
            full_msg = self.get_0x361()
            for item in full_msg:
                data = item[0]
                channel = item[1]
                window.set_labelValue(data,channel)
                print("0x361 works")
        
        if msg.arbitration_id == 0x370:
            full_msg = self.get_0x370()
            for item in full_msg:
                data = item[0]
                channel = item[1]
                window.set_labelValue(data,channel)
                print("0x370 works")
        
        if msg.arbitration_id == 0x372:
            full_msg = self.get_0x372()
            for item in full_msg:
                data = item[0]
                channel = item[1]
                window.set_labelValue(data,channel)
                print("0x372 works")

        if msg.arbitration_id == 0x3E0:
            full_msg = self.get_0x3E0()
            for item in full_msg:
                data = item[0]
                channel = item[1]
                window.set_labelValue(data,channel)
                print("0x3E0 works")
        
        if msg.arbitration_id == 0x3E2:
            full_msg = self.get_0x3E2()
            for item in full_msg:
                data = item[0]
                channel = item[1]
                window.set_labelValue(data,channel)
                print("0x3E2 works")
        
        if msg.arbitration_id == 0x470:
            full_msg = self.get_0x470()
            for item in full_msg:
                data = item[0]
                channel = item[1]
                window.set_labelValue(data,channel)
                print("0x470 works")

        if msg.arbitration_id == 0x471:
            full_msg = self.get_0x471()
            for item in full_msg:
                data = item[0]
                channel = item[1]
                window.set_labelValue(data,channel)
                print("0x471 works")
        
        if msg.arbitration_id == 0x476:
            full_msg = self.get_0x476()
            for item in full_msg:
                data = item[0]
                channel = item[1]
                window.set_labelValue(data,channel)
                print("0x476 works")
            pass