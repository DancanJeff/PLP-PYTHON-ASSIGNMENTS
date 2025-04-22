class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def move(self):
        return "Moving..."
    
    def get_info(self):
        return f"{self.name} moving at {self.speed} km/h"

class Car(Vehicle):
    def __init__(self, name, speed, wheels=4):
        super().__init__(name, speed)
        self.wheels = wheels
    
    def move(self):
        return f" {self.name} is driving on {self.wheels} wheels at {self.speed} km/h"

class Plane(Vehicle):
    def __init__(self, name, speed, altitude):
        super().__init__(name, speed)
        self.altitude = altitude
    
    def move(self):
        return f" {self.name} is flying at altitude {self.altitude}m going {self.speed} km/h"

class Boat(Vehicle):
    def __init__(self, name, speed):
        super().__init__(name, speed)
    
    def move(self):
        return f" {self.name} is sailing at {self.speed} km/h"

# Example usage
if __name__ == "__main__":
    # Create different vehicles
    car = Car("Toyota", 120)
    plane = Plane("Boeing 747", 900, 10000)
    boat = Boat("Titanic", 40)
    
    # Demonstrate polymorphism with a list of vehicles
    vehicles = [car, plane, boat]
    
    # Show how each vehicle moves differently
    print("\nVehicle Movement Demonstration:")
    print("-" * 30)
    for vehicle in vehicles:
        print(vehicle.move())