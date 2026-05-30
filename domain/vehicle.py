from uuid import uuid4
from enum import Enum

class Vehicle:
    class vehicleType(Enum):
        CAR = "car"
        TRUCK = "truck"
        MOTORCYCLE = "motorcycle"
    def __init__(self,licen_plate:str,v_type:vehicleType):
        self.id = str(uuid4()) 
        self.type = v_type
        self.license_plate = licen_plate
    def __str__(self):
        return f"Vehicle ID: {self.id}, License Plate: {self.license_plate}, Type: {self.type.value}"