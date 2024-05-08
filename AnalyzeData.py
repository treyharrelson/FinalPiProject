import serial

# This reads the Serial Input coming from the Arduino, appending the velocities to a list.
class SerialReader:

    def __init__(self, port, baudrate):
        self.arduino_data = serial.Serial(port, baudrate)
        self.x_velocity = 0
        self.y_velocity = 0
        self.z_velocity = 0
        self.reps = 0
        self.running = False

    def start_running(self):
        self.running = True
        
    def read_data(self):
        consecutive_neg = 0
        consecutive_pos = 0
        eccentric = False
        check_rep_counter = 0
        while self.running:
            # doesn't start until there is data there
            while self.arduino_data.inWaiting()==0:
                pass
            dataPacket = self.arduino_data.readline().decode().strip()
            velocities = dataPacket.split(",")
            if len(velocities)==3:
                self.x_velocity = float(velocities[0])
                self.y_velocity = float(velocities[1])
                self.z_velocity = float(velocities[2])
                
                if self.z_velocity > 0:
                    consecutive_pos += 1
                    consecutive_neg = 0
                elif self.z_velocity < 0:
                    consecutive_neg += 1
                    consecutive_pos = 0

                if check_rep_counter == 1:
                    value_to_check = self.z_velocity
                if check_rep_counter == 11:
                    if abs(self.z_velocity - value_to_check) > .5:
                        self.reps += 1
                    check_rep_counter = 0

                # 10 consecutive values in the same direction will count as a rep
                if consecutive_pos == 10 and not eccentric:
                    #self.reps += 1
                    consecutive_pos = 0
                    eccentric = True
                if consecutive_neg == 10 and eccentric:
                    consecutive_neg = 0
                    eccentric = False
                
                print(f"Z={self.z_velocity}  reps={self.reps}  {eccentric}  {check_rep_counter}")
                check_rep_counter += 1

            


    def stop_running(self):
        self.running = False


# s = SerialReader('COM5', 115200)
# s.start_running()
# s.read_data()


