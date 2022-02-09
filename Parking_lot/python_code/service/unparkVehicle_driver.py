from service.outputFormaters import *
from service.__print import Print__

def unparkVehicle_driver(stream,parking_lot):
    no_plate = stream[1]
    
    unbooked = False
    for floor in parking_lot.floors_data:
        slotSize = parking_lot.slots
        for i in range(0,slotSize):
            if floor.slots_data[i]:     
                if floor.slots_data[i].ticket_id == no_plate:
                    
                        output_unparked(floor.slots_data[i])
                        
                        floor.slots_data[i] = None
                        unbooked = True
                        break
        
        if unbooked:
                break

    if unbooked == False:
        Print__("Invalid Ticket")   