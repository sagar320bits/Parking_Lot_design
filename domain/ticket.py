from uuid import uuid4
from datetime import datetime

class Ticket:
    def __init__(self, vehicle_id: str, parking_slot_id: str):
        self.id = str(uuid4())
        self.vehicle_id = vehicle_id
        self.parking_slot_id = parking_slot_id
        self.entry_time = datetime.now()
        self.active = True
    def deactivate(self):
        self.active = False
    def __str__(self):
        return f"Ticket ID: {self.id}, Vehicle ID: {self.vehicle_id}, Parking Slot ID: {self.parking_slot_id}, Entry Time: {self.entry_time}, Active: {self.active}"