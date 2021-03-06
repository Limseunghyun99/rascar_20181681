# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time



class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        self.car.steering.turning_max = 50

    def drive_parking(self):
        self.car.drive_parking()

    def side_parking(self):
        self.adequate_time = 1
        self.car.steering.turn(70)
        self.car.accelerator.go_forward(30)
        time.sleep(0.5)
        self.car.steering.turn(90)
        self.car.accelerator.go_backward(30)
        time.sleep(0.6)
        self.car.accelerator.rightLarge()
        time.sleep(self.adequate_time)
        self.car.accelerator.stop()

    def from_side_to_road(self):
        self.car.accelerator.leftLarge()
        time.sleep(self.adequate_time)
        self.car.steering.turn(120)
        self.car.accelerator.go_forward
        time.sleep(0.5)

    def line_tracing(self):
        if self.car.line_detector.read_digital() == [0, 0, 1, 0, 0]:
            self.car.accelerator.go_forward(70)

        elif self.car.line_detector.read_digital() == [1, 1, 1, 1, 0]:
            self.car.steering.turn_left(60)
            self.car.accelerator.go_forward(70)

        elif self.car.line_detector.read_digital() == [1, 0, 0, 0, 0]:
            self.car.steering.turn_left(60)
            self.car.accelerator.go_forward(70)

        elif self.car.line_detector.read_digital() == [1, 1, 0, 0, 0]:
            self.car.steering.turn_left(60)
            self.car.accelerator.go_forward(70)

        elif self.car.line_detector.read_digital() == [0, 1, 0, 0, 0]:
            self.car.steering.turn_left(65)
            self.car.accelerator.go_forward(70)

        elif self.car.line_detector.read_digital() == [0, 1, 1, 0, 0]:
            self.car.steering.turn_left(65)
            self.car.accelerator.go_forward(70)

        elif self.car.line_detector.read_digital() == [1, 1, 1, 0, 0]:
            self.car.steering.turn_left(75)
            self.car.accelerator.go_forward(70)

        elif self.car.line_detector.read_digital() == [0, 0, 1, 1, 0]:
            self.car.steering.turn_right(96)
            self.car.accelerator.go_forward(70)

        elif self.car.line_detector.read_digital() == [0, 0, 1, 1, 1]:
            self.car.steering.turn_right(95)
            self.car.accelerator.go_forward(70)

        elif self.car.line_detector.read_digital() == [0, 0, 0, 1, 0]:
            self.car.steering.turn_right(100)
            self.car.accelerator.go_forward(70)

        elif self.car.line_detector.read_digital() == [0, 0, 0, 1, 1]:
            self.car.steering.turn_right(105)
            self.car.accelerator.go_forward(70)

        elif self.car.line_detector.read_digital() == [0, 0, 0, 0, 1]:
            self.car.steering.turn_right(110)
            self.car.accelerator.go_forward(70)
            time.sleep(0.1)

        elif self.car.line_detector.read_digital() == [0, 1, 1, 1, 0]:
            self.car.steering.turn(90)
            self.car.accelerator.go_forward(70)

        elif self.car.line_detector.read_digital() == [1, 0, 0, 1, 1]:
            self.car.steering.turn_right(110)
            self.car.accelerator.go_forward(60)

        elif self.car.line_detector.read_digital() == [1, 0, 1, 1, 1]:
            self.car.steering.turn_right(110)
            self.car.accelerator.go_forward(50)

        elif self.car.line_detector.read_digital() == [0, 1, 1, 1, 1]:
            self.car.steering.turn(70)
            self.car.accelerator.go_forward(50)

        elif self.car.line_detector.read_digital() == [0, 0, 0, 0, 0]:
            self.car.steering.turn(120)
            self.car.accelerator.go_backward(50)
            #time.sleep(0.2)
            #self.car.steering.turn(80)
            #self.car.accelerator.go_forward(70)
            #time.sleep(0.18)
            #self.car.accelerator.stop()

        elif self.car.line_detector.read_digital() == [1, 1, 1, 1, 1] :
            self.car.accelerator.stop()

    def avoidence(self):
        self.car.accelerator.stop()
        self.car.steering.turn(60)
        self.car.accelerator.go_forward(70)
        time.sleep(0.8)
        while self.car.line_detector.read_digital() != [1, 0, 0, 0, 0]:
            self.car.accelerator.go_forward(70)
        self.car.steering.turn(120)
        self.car.accelerator.go_forward(70)
        time.sleep(1.8)
        while self.car.line_detector.read_digital()[4] == 0:
            self.car.accelerator.go_forward(70)

    def car_startup(self):
        self.car.accelerator.go_forward(60)
        while True:
            print("tracking: ", self.car.line_detector.read_digital())
            distance = self.car.distance_detector.get_distance()
            print("distance: ", distance)
            print("")
            temp = []

            self.line_tracing()
            # prevent distance value error
            for i in range(3):
                distance = self.car.distance_detector.get_distance()
                temp.append(distance)
                temp.sort()

            # 장애물 회피
            if 0 < temp[2] < 30:
                self.avoidence()

            # 신호등
            if self.car.color_getter.red_signal():
                self.car.accelerator.stop()
                time.sleep(1)
            
            time.sleep(0.1)





if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
