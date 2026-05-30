from uuid import uuid4
from .parking_slot import ParkingSlot   
from.vehicle import Vehicle
class Floor:
    def __init__(self,floor_number:int):
        self.id = str(uuid4())
        self.floor_number = floor_number
        self.parking_slots:list[ParkingSlot] = []

    def add_slot(self,slot:ParkingSlot):
        self.parking_slots.append(slot)
    def available_slots(self,vehicle_type:Vehicle.vehicleType):
        return [slot for slot in self.parking_slots if not slot.is_occupied and slot.slot_type == vehicle_type]
    def available_slots_count(self,vehicle_type:Vehicle.vehicleType):
        return len(self.available_slots(vehicle_type))
    def __str__(self):
        return f"Floor ID: {self.id}, Floor Number: {self.floor_number}, Parking Slots: {[str(slot) for slot in self.parking_slots]}"