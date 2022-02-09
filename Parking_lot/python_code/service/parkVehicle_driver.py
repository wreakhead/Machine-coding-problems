from models.parking_lot_model import parkingSlot
from service.outputFormaters import *
from service.__print import Print__


def createTicket(parking_lot,level,i,register_no,color,floor):

    new_ticket = parking_lot.ID+"_"+str(level)+"_"+str(i+1)
    new_slot = parkingSlot(register_no,type,color,new_ticket)
    floor.slots_data[i] = new_slot
    output_parked(new_ticket)


def parkVehicle_driver(stream,parking_lot):
    type = stream[1]
    register_no = stream[2]
    color = stream[3]

    
    booked = False
    for floor in parking_lot.floors_data:
        slotSize = parking_lot.slots
        
        if type == 'CAR':
            for i in range(3,slotSize):
                 
                    if floor.slots_data[i] == None:
                        createTicket(parking_lot,floor.level,i,register_no,color,floor)
                        
                        booked = True
                        break
        elif type == 'TRUCK':    
            if floor.slots_data[0] == None:
                        createTicket(parking_lot,floor.level,0,register_no,color,floor)
                        
                        booked = True
                        
        elif type == 'BIKE':
            for i in range(1,3):
                
                    if floor.slots_data[i] == None:
                        createTicket(parking_lot,floor.level,i,register_no,color,floor)
                        
                        booked = True
                        break
        else:
            booked =True
            Print__("Invalid vehicle")
            break

        if booked:
                break

    if booked == False:
        Print__("Parking Lot Full")        



