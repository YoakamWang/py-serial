import serial

"""
   This is the testing for data tranfer 
   through serial port..
"""


class TestSerial(object):
    STRGLO = ""  # The read data
    BOOL = True  # The read flag
    ser = ""  # The serial object

    def __init__(self, portx, bps, timeout):
        self.port = portx
        self.bps = bps
        self.timeout = timeout

    def readData(self):
        # global STRGLO, BOOL
        ret, self.ser = self.openPort()
        while self.BOOL:
            if self.ser.in_waiting:
                STRGLO = self.ser.read(self.ser.in_waiting).decode("UTF-8")
                return STRGLO

    def openPort(self):
        # global ser
        ret = False
        try:
            self.ser = serial.Serial(self.port, self.bps, self.timeout)
            if (self.ser.isOpen()):
                ret = True
                # threading.Thread(target=readData,args=(ser,)).start()
        except Exception as e:
            print("------ERROR-----", e)
        return ret, self.ser

    def closePort(self):
        # global BOOL
        self.BOOL = False
        self.ser.close()

    def writePort(self, text):
        result = self.ser.write(text.encode(b""))
        return result


def main():
    testSerial = TestSerial("COM3", 9600, None)
    ret, ser = testSerial.openPort()
    if (ret == True):
        count = testSerial.writePort("test date")
        print("write date successfully!!")
        output = testSerial.readData()
        print("The output is: ", output)
        testSerial.closePort(ser)


if __name__ == "__main__":
    main()
