class DroneMotor():
    def __init__(self, quantity, KV):
        self.quantity = quantity
        self.KV = KV
        self.weight = 12
    def description(self):
        desc = f'This drone has  {self.quantity} motors'
        return desc

    def carriage(self):
        print(f" This drone can carry weight not bigger than {self.weight} kg.")

    def voltage(self):
        volt = f"The power of the motors is {self.KV} KV."
        return volt
    def transportation(self, goods):
        if goods <= self.weight:
            print('Drone is ready for transportation.')
        else:
            print('You cant load more than drone could carry')
drone = DroneMotor('4', '3.7')
print(drone.description())
print(drone.voltage())
drone.transportation(15)
drone.carriage()
drone.transportation(10)
drone.carriage()






