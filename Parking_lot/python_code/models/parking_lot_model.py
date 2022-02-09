
class parkingLot:

    def __init__(self,ID,floors,slots):
        self.ID = ID
        self.floors = floors
        self.slots = slots
        self.booked = 0
        self.floors_data = []
        self.createParkingLot(slots)

    def isFull(self):
        return self.booked == self.slots

    def floorDetail(self,floor_level):
        return self.floors_data[floor_level-1]

    def createParkingLot(self,slots):
        for lvl in range(1,self.floors+1):
            new_floor = floor(lvl,slots)
            self.floors_data.append(new_floor)



class floor:

    def __init__(self,level,slots):
        self.level = level
        self.truck_slot = 1
        self.bike_slot = 2
        self.car_slot = slots-3
        self.slots_data = [None]*slots

class parkingSlot:

    def __init__(self,register_no,type,color,ticket_id):
        self.register_no = register_no
        self.type = type
        self.color = color
        self.ticket_id= ticket_id




                


        